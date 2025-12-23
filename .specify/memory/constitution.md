# Constitution: Physical AI & Humanoid Robotics Textbook

## Project Overview
Project: Create a Textbook for Teaching Physical AI & Humanoid Robotics Course

This constitution governs the development of a textbook deployed as a static web application using Docusaurus. It ensures high-quality content, robust technical implementation, and proper deployment to GitHub Pages to support Panaversity's mission of teaching cutting-edge AI skills. The MVP approach focuses on delivering core textbook content as a static site first, with advanced interactive features to be implemented in future iterations. All development must adhere to this framework to ensure quality and consistency.

## Core Principles

1. **Accuracy through primary source verification** for all content and technical claims.
2. **Clarity for academic audience** (computer science background), with intuitive user interfaces for interactive elements.
3. **Reproducibility** (all claims, code, and configurations cited and traceable).
4. **Rigor** (peer-reviewed sources preferred for content; best practices for code and AI integrations).
5. **Technical Reliability**: Ensure deployments are stable, code is maintainable, and integrations are secure.
6. **User-Centric Interactivity**: Prioritize features that enhance learning, such as personalized content and responsive chatbots.
7. **Innovation through AI**: Leverage AI tools ethically to create reusable intelligence and dynamic experiences.

## Key Standards

1. **Source Verification**: All factual and technical claims must be traceable to sources.
   - Citation format: APA style for content; inline comments or README for code/technical refs.
   - Source types: Minimum 50% peer-reviewed articles for textbook content; at least 30% technical documentation (e.g., API refs for FastAPI, Qdrant) for implementations.

2. **Plagiarism Policy**: 0% tolerance for content and code before submission (use tools like Copyleaks or GitHub Copilot checks).

3. **Writing Standards**: Writing clarity: Flesch-Kincaid grade 10-12 for textbook chapters.

4. **Code Quality**:
   - Adhere to PEP 8 for Python
   - Include unit tests for key components (e.g., chatbot queries)
   - Ensure cross-browser compatibility for the Docusaurus site

5. **Security**:
   - Implement secure authentication (e.g., via Better-Auth for bonus features)
   - Protect user data in compliance with basic privacy standards

6. **AI Integration**:
   - MVP phase focuses on static content delivery; AI features (RAG chatbot, personalization, translation) will be implemented in future iterations
   - For future RAG chatbot, ensure 95%+ accuracy on content-based queries

### Bonus Feature Standards:
- **Signup/Signin**: Collect user background (software/hardware) ethically; no PII storage without consent.
- **Personalization**: Button-triggered adaptations based on user profile; maintain core content integrity.
- **Urdu Translation**: Accurate, culturally sensitive translations; support toggle back to English.

## Constraints

1. **Core Content Word Count**: 5,000-7,000 words (excluding code, docs, or auto-generated elements).
2. **Minimum Sources**: 15 total (at least 10 academic + 5 technical).
3. **Format**: Docusaurus-based static website with Markdown chapters; deploy to GitHub Pages; optional PDF export for static version.
4. **Tech Stack**: Must use Spec-Kit Plus, Claude Code for book creation; Docusaurus for static site generation; backend services will be implemented in future iterations.
5. **Bonus Constraints**: Advanced features (RAG chatbot, authentication, personalization, translation) will be implemented in future iterations after MVP deployment.
6. **Deployment**: Static site deployed to GitHub Pages; no backend services required for MVP.
7. **Timeline**: MVP must be functional by project deadline with proper version control and documentation.

## Success Criteria

1. All claims (content and technical) verified against sources.
2. Zero plagiarism detected in content or code.
3. Passes fact-checking and content review (e.g., no critical bugs, successful static site deployment).
4. Technical Success: Static site deployed and functional on GitHub Pages.
5. Content Quality: Meets word count and source requirements.
6. User Experience: Textbook content is accessible and well-organized.
7. MVP Requirements: Static Docusaurus site successfully deployed without backend dependencies.

## Development Guidelines

1. **Spec-Driven Development**: Follow the Spec-Kit Plus methodology for all development.
2. **Testing**: Focus on content validation and static site functionality for MVP.
3. **Documentation**: Maintain clear documentation for setup, deployment, and usage.
4. **Version Control**: Use Git with clear commit messages following conventional commits.
5. **Code Reviews**: All code changes must be reviewed before merging.
6. **MVP Focus**: Prioritize static content delivery and proper deployment over advanced interactive features.

## Governance

This constitution supersedes all other practices for this project. All development activities must comply with these principles and standards. Any amendments to this constitution require proper documentation, approval, and migration planning. All pull requests and code reviews must verify compliance with these principles.

**Version**: 1.0.1 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-09
