from datetime import datetime, timedelta
from typing import Optional
import uuid
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..models.user import User
from ..database.config import DATABASE_URL
from ..config.settings import settings

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Initialize security schemes
security = HTTPBearer()


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against its hash."""
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        """Generate a hash for a plain password."""
        return pwd_context.hash(password)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate a user by email and password."""
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not self.verify_password(password, user.password_hash):
            return None
        return user

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        """Create a JWT access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        to_encode.update({"exp": expire, "type": "access"})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encoded_jwt

    def create_refresh_token(self, data: dict):
        """Create a JWT refresh token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=settings.refresh_token_expire_days)
        to_encode.update({"exp": expire, "type": "refresh"})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encoded_jwt

    def get_current_user(self, token: str = Depends(security)) -> User:
        """Get the current user from the access token."""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token.credentials, settings.secret_key, algorithms=[settings.algorithm])
            user_id: str = payload.get("sub")
            token_type: str = payload.get("type")

            if user_id is None or token_type != "access":
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = self.db.query(User).filter(User.id == uuid.UUID(user_id)).first()
        if user is None:
            raise credentials_exception
        return user

    def register_user(self, email: str, password: str, name: str) -> User:
        """Register a new user."""
        # Check if user already exists
        existing_user = self.db.query(User).filter(User.email == email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists"
            )

        # Hash the password
        hashed_password = self.get_password_hash(password)

        # Create new user
        user = User(
            email=email,
            password_hash=hashed_password,
            name=name
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def update_user_last_activity(self, user: User):
        """Update the user's last activity timestamp."""
        user.last_activity_at = datetime.utcnow()
        # Set data retention date to 5 years from now if not already set
        if not user.data_retention_until:
            user.data_retention_until = datetime.utcnow() + timedelta(days=365*5)
        self.db.commit()


# Dependency to get the current user
def get_current_user(db: Session = Depends(get_db)):
    """Dependency to get the current user from the access token."""
    auth_service = AuthService(db)
    return auth_service.get_current_user


# Helper function to get auth service
def get_auth_service(db: Session = Depends(get_db)):
    """Dependency to get the auth service."""
    return AuthService(db)