# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

## Prerequisites
- Python 3.11+
- Node.js 18+
- Docker (for local development)
- Access to Neon Serverless Postgres
- Access to Qdrant Cloud
- OpenAI API key (for translation and Claude subagents)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd physical-AI-humanoid-robotics
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration
```

### 4. Database Setup
```bash
# From backend directory
python -m src.scripts.init_db
```

### 5. Vector Database Setup
```bash
# Initialize Qdrant collection for textbook content
python -m src.scripts.init_vector_db
```

### 6. Content Setup
```bash
# Import textbook chapters (run from backend directory)
python -m src.scripts.import_chapters
```

## Running the Application

### Development Mode
```bash
# Terminal 1: Start backend
cd backend
python -m src.main

# Terminal 2: Start frontend
cd frontend
npm start
```

### Production Mode
```bash
# Build frontend
cd frontend
npm run build

# Start backend with production settings
cd backend
gunicorn src.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## API Endpoints
- `GET /api/chapters`: List all textbook chapters
- `GET /api/chapters/{slug}`: Get specific chapter content
- `POST /api/chat`: Chatbot interaction endpoint
- `POST /api/auth/login`: User authentication
- `POST /api/auth/register`: User registration
- `POST /api/translate`: Content translation endpoint

## Configuration
Environment variables required:
- `DATABASE_URL`: Neon Serverless Postgres connection string
- `QDRANT_URL`: Qdrant Cloud endpoint
- `OPENAI_API_KEY`: For translation and Claude integration
- `BETTER_AUTH_SECRET`: Authentication secret
- `ENCRYPTION_KEY`: For data encryption