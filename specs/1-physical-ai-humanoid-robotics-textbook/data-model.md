# Data Model: Physical AI & Humanoid Robotics Textbook

## User
- id: UUID (Primary Key)
- email: String (Unique, Required)
- password_hash: String (Required, encrypted)
- technical_proficiency: JSON object containing:
  - mathematical_concepts: Enum (beginner, intermediate, advanced)
  - programming_experience: Enum (beginner, intermediate, advanced)
  - prior_robotics_knowledge: Enum (beginner, intermediate, advanced)
- created_at: DateTime (Auto-generated)
- updated_at: DateTime (Auto-generated)
- last_activity_at: DateTime
- data_retention_until: DateTime (Set to 5 years after last activity)

## TextbookChapter
- id: UUID (Primary Key)
- title: String (Required)
- slug: String (Unique, URL-friendly, Required)
- content: Text (Markdown format, Required)
- content_urdu: Text (Translated content in Urdu)
- difficulty_level: Enum (beginner, intermediate, advanced)
- prerequisite_chapters: Array of UUIDs
- tags: Array of Strings
- created_at: DateTime (Auto-generated)
- updated_at: DateTime (Auto-generated)
- version: Integer (For content updates)

## UserProgress
- id: UUID (Primary Key)
- user_id: UUID (Foreign Key to User, Required)
- chapter_id: UUID (Foreign Key to TextbookChapter, Required)
- status: Enum (not_started, in_progress, completed)
- completion_percentage: Float (0-100)
- time_spent_seconds: Integer
- last_accessed_at: DateTime
- notes: Text (Optional user notes)
- quiz_scores: JSON array of objects (if quizzes are added later)
- created_at: DateTime (Auto-generated)
- updated_at: DateTime (Auto-generated)

## ChatbotSession
- id: UUID (Primary Key)
- user_id: UUID (Foreign Key to User, Optional for anonymous sessions)
- session_token: String (For anonymous sessions)
- created_at: DateTime (Auto-generated)
- updated_at: DateTime (Auto-generated)
- expires_at: DateTime (Session expiration)

## ChatbotMessage
- id: UUID (Primary Key)
- session_id: UUID (Foreign Key to ChatbotSession, Required)
- role: Enum (user, assistant)
- content: Text (Required)
- timestamp: DateTime (Auto-generated)
- source_chunks: JSON array of objects (containing references to textbook content used)
- is_fallback_response: Boolean (True if response was generated due to out-of-scope query)

## TranslationCache
- id: UUID (Primary Key)
- content_id: String (Reference to chapter or content section)
- source_language: String (Default: 'en')
- target_language: String (Default: 'ur')
- source_content_hash: String (To detect content changes)
- translated_content: Text (Cached translation)
- created_at: DateTime (Auto-generated)
- updated_at: DateTime (Auto-generated)
- expires_at: DateTime (Cache expiration)

## Relationships
- User (1) → (Many) UserProgress
- TextbookChapter (1) → (Many) UserProgress
- User (1) → (Many) ChatbotSession
- ChatbotSession (1) → (Many) ChatbotMessage
- User (1) → (Many) ChatbotMessage (via session)

## Validation Rules
- User email must be valid email format
- User technical_proficiency values must be one of the defined enums
- TextbookChapter slug must be unique
- UserProgress completion_percentage must be between 0 and 100
- UserProgress status must be one of the defined enums
- ChatbotMessage role must be either 'user' or 'assistant'

## Indexes
- User: email (unique)
- TextbookChapter: slug (unique)
- UserProgress: (user_id, chapter_id) composite (unique)
- ChatbotSession: user_id, session_token
- TranslationCache: content_id, source_language, target_language (composite, unique)