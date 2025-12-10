# Physical AI & Humanoid Robotics Textbook

An interactive textbook platform for learning about Physical AI and Humanoid Robotics with AI-powered features.

## Overview

This project implements a web-based educational platform that provides:
- Interactive textbook content on Physical AI and Humanoid Robotics
- AI-powered chatbot for learning support (RAG-based)
- Personalized content based on technical proficiency
- Multi-language support (English/Urdu)
- User progress tracking

## Architecture

The application follows a modern web architecture with:
- **Backend**: FastAPI-based API server
- **Frontend**: Docusaurus-based documentation site with React components
- **Database**: Neon Serverless Postgres
- **Vector Database**: Qdrant Cloud for RAG functionality
- **Authentication**: Better-Auth

## Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- Access to Neon Serverless Postgres
- Access to Qdrant Cloud
- OpenAI API key

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your configuration:
   ```env
   DATABASE_URL=your_neon_database_url
   QDRANT_URL=your_qdrant_cloud_url
   QDRANT_API_KEY=your_qdrant_api_key
   OPENAI_API_KEY=your_openai_api_key
   BETTER_AUTH_SECRET=your_auth_secret
   ```

5. Start the backend server:
   ```bash
   uvicorn src.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Project Structure

```
backend/
├── src/
│   ├── models/          # Database models
│   ├── services/        # Business logic
│   ├── api/             # API routes
│   ├── database/        # Database configuration
│   └── main.py          # Application entry point
└── tests/               # Test files

frontend/
├── docs/                # Textbook content
├── src/                 # React components
├── static/              # Static assets
├── docusaurus.config.js # Docusaurus configuration
└── sidebars.js          # Navigation configuration
```

## API Endpoints

The backend provides the following API endpoints:
- `/api/chapters` - Access textbook content
- `/api/chatbot/query` - Chatbot functionality
- `/api/auth/` - Authentication
- `/api/translate` - Translation services
- `/api/users/progress` - User progress tracking

## Contributing

Please follow the conventional commit format for all commits.