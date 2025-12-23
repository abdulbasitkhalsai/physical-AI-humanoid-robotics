# Physical AI & Humanoid Robotics Textbook

A static textbook platform for learning about Physical AI and Humanoid Robotics, deployed as a Docusaurus-based website. This MVP focuses on delivering comprehensive textbook content as a static site, with advanced interactive features to be implemented in future iterations.

## Overview

This project implements a static web-based educational platform that provides:
- Comprehensive textbook content on Physical AI and Humanoid Robotics
- Multi-language support (English/Urdu) for static content
- Proper navigation and search capabilities
- GitHub Pages deployment

Advanced features such as AI-powered chatbot, personalization, and user authentication will be implemented in future iterations.

## Architecture

The application follows a static web architecture with:
- **Frontend**: Docusaurus-based static site generation with React components
- **Deployment**: GitHub Pages for static content delivery
- **MVP Focus**: Content delivery without backend dependencies
- **Future Architecture**: Backend services will be added in future iterations

## Setup

### Prerequisites

- Node.js 18+ (for Docusaurus static site generation)

### Frontend Setup (MVP)

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

4. Build the static site for production:
   ```bash
   npm run build
   ```

### Backend (Future Iterations)

Backend components are not required for the MVP deployment. They will be implemented in future iterations after the static site is deployed.

## Project Structure

### MVP Structure
```
frontend/
├── docs/                # Textbook content (chapters in MDX format)
├── src/                 # React components for Docusaurus
├── static/              # Static assets
├── docusaurus.config.js # Docusaurus configuration
└── sidebars.js          # Navigation configuration
```

### Backend (Future Iterations)
```
backend/                 # Will be implemented after MVP deployment
├── src/
│   ├── models/
│   ├── services/
│   ├── api/
│   └── main.py
└── tests/
```

## Static Site Features

The static site provides the following functionality:
- Textbook content navigation and search
- Multi-language support (English/Urdu)
- Responsive design
- GitHub Pages deployment

## Contributing

For MVP development:
- Focus on content creation and Docusaurus configuration
- Follow standard Markdown/MDX formatting for textbook chapters
- Test static site builds before committing

For future iterations:
- Backend development will follow the conventional commit format
- API endpoints will be documented separately