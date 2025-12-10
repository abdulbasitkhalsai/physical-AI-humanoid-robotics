# API Contracts: Physical AI & Humanoid Robotics Textbook

## Authentication Endpoints

### POST /api/auth/register
Register a new user with technical proficiency information.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "technical_proficiency": {
    "mathematical_concepts": "intermediate",
    "programming_experience": "advanced",
    "prior_robotics_knowledge": "beginner"
  }
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "created_at": "2025-12-09T10:00:00Z",
  "access_token": "jwt-token"
}
```

### POST /api/auth/login
Authenticate user and return access token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response:**
```json
{
  "access_token": "jwt-token",
  "user": {
    "id": "uuid-string",
    "email": "user@example.com"
  }
}
```

## Textbook Content Endpoints

### GET /api/chapters
Retrieve list of available textbook chapters.

**Response:**
```json
{
  "chapters": [
    {
      "id": "uuid-string",
      "title": "Introduction to Physical AI",
      "slug": "introduction-to-physical-ai",
      "difficulty_level": "beginner",
      "prerequisite_chapters": [],
      "tags": ["introduction", "ai", "robotics"],
      "created_at": "2025-12-09T10:00:00Z"
    }
  ]
}
```

### GET /api/chapters/{slug}
Retrieve specific textbook chapter content.

**Response:**
```json
{
  "id": "uuid-string",
  "title": "Introduction to Physical AI",
  "slug": "introduction-to-physical-ai",
  "content": "# Introduction to Physical AI\n\nPhysical AI combines...",
  "content_urdu": "# جسمانی ای ۔آئی کا تعارف\n\nجسمانی ای ۔آئی میں...",
  "difficulty_level": "beginner",
  "prerequisite_chapters": [],
  "tags": ["introduction", "ai", "robotics"],
  "version": 1
}
```

## Chatbot Endpoints

### POST /api/chat
Submit a query to the RAG chatbot.

**Request Body:**
```json
{
  "message": "Explain the concept of embodied cognition in robotics",
  "session_id": "optional-session-id"
}
```

**Response:**
```json
{
  "response": "Embodied cognition in robotics refers to...",
  "sources": [
    {
      "chapter_id": "uuid-string",
      "chapter_title": "Cognitive Robotics",
      "relevance_score": 0.85
    }
  ],
  "session_id": "new-or-existing-session-id",
  "is_fallback_response": false
}
```

## Translation Endpoints

### POST /api/translate
Translate textbook content to Urdu.

**Request Body:**
```json
{
  "content": "Physical AI combines machine learning with physical systems",
  "target_language": "ur",
  "source_language": "en"
}
```

**Response:**
```json
{
  "translated_content": "جسمانی ای ۔آئی مشین لرننگ کو جسمانی نظام کے ساتھ جوڑتا ہے",
  "detected_language": "en",
  "target_language": "ur",
  "cache_hit": false
}
```

## User Progress Endpoints

### GET /api/user/progress
Get user's progress across textbook chapters.

**Response:**
```json
{
  "progress": [
    {
      "chapter_id": "uuid-string",
      "chapter_title": "Introduction to Physical AI",
      "status": "completed",
      "completion_percentage": 100,
      "time_spent_seconds": 1800,
      "last_accessed_at": "2025-12-09T10:00:00Z"
    }
  ]
}
```

### PUT /api/user/progress/{chapter_id}
Update user's progress for a specific chapter.

**Request Body:**
```json
{
  "status": "in_progress",
  "completion_percentage": 65
}
```

**Response:**
```json
{
  "chapter_id": "uuid-string",
  "status": "in_progress",
  "completion_percentage": 65,
  "updated_at": "2025-12-09T10:00:00Z"
}
```