# Physical AI & Humanoid Robotics Textbook Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-12-09

## Active Technologies

- Python 3.11
- FastAPI
- Docusaurus
- Neon Serverless Postgres
- Qdrant Cloud
- Better-Auth
- Claude SDK
- JavaScript/TypeScript
- Markdown

## Project Structure

```text
backend/
├── src/
│   ├── models/
│   │   ├── user.py
│   │   ├── textbook_chapter.py
│   │   ├── user_progress.py
│   │   └── chatbot_session.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── rag_service.py
│   │   ├── translation_service.py
│   │   ├── personalization_service.py
│   │   └── content_service.py
│   ├── api/
│   │   ├── auth_routes.py
│   │   ├── textbook_routes.py
│   │   ├── chatbot_routes.py
│   │   └── translation_routes.py
│   └── main.py
└── tests/

frontend/
├── src/
│   ├── components/
│   │   ├── TextbookViewer/
│   │   ├── Chatbot/
│   │   ├── Personalization/
│   │   └── Translation/
│   ├── pages/
│   │   ├── Chapter/
│   │   ├── Dashboard/
│   │   └── Auth/
│   └── services/
│       ├── api_client.js
│       └── auth_client.js
├── docusaurus.config.js
├── sidebars.js
└── static/

docs/
├── setup.md
├── deployment.md
└── api-reference.md
```

## Commands

### Backend Development
```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend server
python -m src.main

# Run tests
pytest
```

### Frontend Development
```bash
# Install dependencies
npm install

# Run development server
npm start

# Build for production
npm run build
```

### Database Operations
```bash
# Initialize database
python -m src.scripts.init_db

# Initialize vector database
python -m src.scripts.init_vector_db

# Import textbook chapters
python -m src.scripts.import_chapters
```

## Code Style

### Python
- Follow PEP 8 guidelines
- Use type hints for all function signatures
- Write docstrings for all public functions and classes
- Use async/await for I/O operations

### JavaScript
- Use TypeScript where possible
- Follow Airbnb JavaScript Style Guide
- Use functional components with hooks in React
- Write JSDoc for exported functions

### Markdown
- Use consistent heading hierarchy
- Include alt text for all images
- Use relative links within the documentation

## Recent Changes

1. **Physical AI & Humanoid Robotics Textbook** - Added textbook content delivery system with Docusaurus, RAG chatbot with Qdrant, user authentication with Better-Auth, personalization based on technical proficiency, and Urdu translation functionality

2. **Non-Goals Definition** - Added explicit scope boundaries to prevent feature creep including live classroom functionality, advanced robotics simulation, hardware robot control, and comprehensive LMS

3. **Specification Clarifications** - Added 5 critical clarifications: technical proficiency classification for personalization, 5-year data retention policy, "not in scope" responses for out-of-topic questions, English terms with Urdu explanations in parentheses, and public content with authenticated personalization

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->