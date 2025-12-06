# Constitution: Physical AI & Humanoid Robotics Textbook

## Project Overview
Project: Hackathon I: Create a Textbook for Teaching Physical AI & Humanoid Robotics Course

This constitution governs the development of an AI-native textbook deployed as a dynamic web application. It ensures high-quality content, robust technical implementation, and integration of interactive AI features to support Panaversity's mission of teaching cutting-edge AI skills. Participants must adhere to this framework to maximize scoring (base 100 points + up to 200 bonus points) and demonstrate readiness for potential roles in the Panaversity ecosystem.

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
   - For RAG chatbot, ensure 95%+ accuracy on content-based queries
   - For bonuses, validate subagents/skills reuse, personalization logic, and translation fidelity (e.g., via automated checks or manual sampling)

### Bonus Feature Standards:
- **Signup/Signin**: Collect user background (software/hardware) ethically; no PII storage without consent.
- **Personalization**: Button-triggered adaptations based on user profile; maintain core content integrity.
- **Urdu Translation**: Accurate, culturally sensitive translations; support toggle back to English.

## Constraints

1. **Core Content Word Count**: 5,000-7,000 words (excluding code, docs, or auto-generated elements).
2. **Minimum Sources**: 15 total (at least 10 academic + 5 technical).
3. **Format**: Docusaurus-based website with Markdown chapters; deploy to GitHub Pages; optional PDF export for static version.
4. **Tech Stack**: Must use Spec-Kit Plus, Claude Code for book creation; OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres, Qdrant Cloud Free Tier for RAG chatbot.
5. **Bonus Constraints**: If pursuing extras, integrate seamlessly (e.g., subagents for reusable intelligence, Better-Auth for auth, per-chapter buttons for personalization/translation).
6. **Deployment**: Live site required; no downtime during evaluation; version-controlled repo (GitHub) with clear setup instructions.
7. **Timeline**: Align with hackathon deadlines; all features functional by submission.

## Success Criteria

1. All claims (content and technical) verified against sources.
2. Zero plagiarism detected in content or code.
3. Passes fact-checking and code review (e.g., no critical bugs, successful end-to-end tests for chatbot and bonuses).
4. Technical Success: Site deployed and functional.
5. Content Quality: Meets word count and source requirements.
6. User Experience: Interactive features work as intended.
7. Bonus Features: If implemented, meet the specified standards.

## Development Guidelines

1. **Spec-Driven Development**: Follow the Spec-Kit Plus methodology for all development.
2. **Testing**: Implement unit and integration tests for all components.
3. **Documentation**: Maintain clear documentation for setup, deployment, and usage.
4. **Version Control**: Use Git with clear commit messages following conventional commits.
5. **Code Reviews**: All code changes must be reviewed before merging.

## Governance

This constitution supersedes all other practices for this project. All development activities must comply with these principles and standards. Any amendments to this constitution require proper documentation, approval, and migration planning. All pull requests and code reviews must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06
