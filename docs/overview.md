# Project Overview

This project implements a Mood-Based Recipe Application incorporating features from Jira issues SCRUM-163, SCRUM-164, and SCRUM-165.

## Features Implemented:

### SCRUM-163: MVP - Mood Input, Recipe Recommendation, Feedback Capture
- React frontend to select mood, browse recipes matching mood, and submit feedback.
- Backend REST API using Flask to handle mood listings, recipe retrieval filtered by mood, and feedback submission.
- Database models for Moods, Recipes, and Feedback with SQLite for ease of use.
- Basic caching for improved performance.
- HTTPS enabled with demo self-signed certificate (adhoc).
- Unit and integration tests scaffolded in backend.

### SCRUM-164: Post-MVP - User Accounts, Advanced Mood Detection, Social Features (Partial)
- User account management microservice with registration and login functionality.
- Password hashing for security.
- RESTful API for user management.

### SCRUM-165: Future Expansions - AI-driven Personalized Recipes, Multi-language Support (Partial)
- AI-inspired personalized recipe generation microservice mocking selection based on mood input.
- Modular design to enable multi-language support and further AI model integration.

## Project Structure

- `backend/` - Flask backend microservices:
  - `app.py` - core mood, recipe and feedback API.
  - `user_service.py` - user accounts and authentication.
  - `ai_recipe_service.py` - AI-driven personalized recipe generation.

- `frontend/` - React frontend:
  - `src/App.js` - mood selection, recipe browsing, and feedback submission UI.

- `docs/overview.md` - this overview document.

## Next Steps
- Extend frontend for user login and account management.
- Implement advanced mood detection input methods.
- Add social sharing features.
- Expand AI recipe generation with real machine learning models.
- Implement multi-language localization.
- Comprehensive testing and deployment pipelines.

For detailed designs and ongoing development, see: https://docs.google.com/document/d/1vEinqBWs-BvnKW09RKTdu6DUE33jvGUs-Cu6IiUm8MA/edit
