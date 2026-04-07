# Backend - MultiChat API 🚀

**FastAPI for MultiChat with JWT authentication, conversation management with Supabase and AI translation.**

![Python](https://img.shields.io/badge/Python-3.13+-green)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-blue)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

[🇫🇷 Français](./README.fr.md)

## 📋 Table of Contents

- [🎯 Features](#-features)
- [🏗️ Structure](#-structure)
- [🚀 Installation](#-installation)
- [📖 API Endpoints](#-api-endpoints)
- [🔐 Authentication](#-authentication)
- [🗄️ Database](#️-database)
- [🔄 WebSocket](#-websocket)
- [📝 Environment Variables](#-environment-variables)
- [🧪 Tests](#-tests)

## 🎯 Features

- **🔐 JWT Authentication** - Access and refresh tokens
- **👤 User Management** - Account creation, profile, updates
- **💬 Conversations** - Create, retrieve, delete
- **💭 Messages** - Send, translate, history
- **🌐 Translation** - Integrated AI translation service
- **📡 WebSocket** - Real-time communication (optional)
- **🔑 Security** - CORS, rate limiting, Pydantic validation

## 🏗️ Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py              # Main router
│   │   ├── auth.py              # Auth endpoints
│   │   ├── conversations.py      # Conversation endpoints
│   │   ├── messages.py          # Message endpoints
│   │   ├── translate.py         # Translation endpoints
│   │   └── deps.py              # FastAPI dependencies
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py            # Config and env vars
│   │   ├── security.py          # JWT security, password hashing
│   │   ├── database.py          # SQLAlchemy session
│   │   └── supabase.py          # Supabase client
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py              # Base model
│   │   ├── user.py              # User model
│   │   ├── conversation.py      # Conversation model
│   │   ├── message.py           # Message model
│   │   └── enums.py             # Enums (Tone, Language)
│   └── schemas/
│       ├── __init__.py
│       ├── auth.py              # Auth schemas (request/response)
│       ├── conversation.py      # Conversation schemas
│       ├── message.py           # Message schemas
│       └── translate.py         # Translation schemas
├── main.py                       # Entry point
├── requirements.txt              # Python dependencies
└── vercel.json                   # Vercel config
```

## 🚀 Installation

### Prerequisites

- Python >= 3.13
- pip or conda
- Supabase account with PostgreSQL

### Setup

```bash
# 1. Navigate to backend folder
cd backend

# 2. Create virtual environment
python -m venv env

# 3. Activate environment
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file (see Environment Variables section)
touch .env

# 6. Run server
python main.py
```

Server starts on `http://localhost:8000`

### API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📖 API Endpoints

### Authentication

```
POST   /api/auth/register          # Create account
POST   /api/auth/login             # Sign in
POST   /api/auth/refresh           # Refresh token
POST   /api/auth/logout            # Sign out
GET    /api/auth/me                # Get user profile
PUT    /api/auth/me                # Update profile
```

### Conversations

```
GET    /api/conversations          # List conversations
POST   /api/conversations          # Create conversation
GET    /api/conversations/{id}     # Get details
PUT    /api/conversations/{id}     # Update
DELETE /api/conversations/{id}     # Delete
```

### Messages

```
GET    /api/conversations/{id}/messages      # List messages
POST   /api/conversations/{id}/messages      # Send message
DELETE /api/messages/{id}                    # Delete message
```

### Translation

```
POST   /api/translate              # Translate message
POST   /api/translate/batch        # Batch translation
```

## 🔐 Authentication

### JWT Token

Authentication uses **JWT tokens**:

```bash
# Access token (short-lived)
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

# Refresh token (long-lived)
{
  "token_type": "bearer",
  "access_token": "...",
  "refresh_token": "..."
}
```

### Flow

1. **Register**: Create account
2. **Login**: Receive access_token + refresh_token
3. **Use**: Add token to headers
4. **Refresh**: Use refresh_token for new access_token

```python
# Example with requests
import requests

headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get("http://localhost:8000/api/auth/me", headers=headers)
```

## 🗄️ Database

### Supabase PostgreSQL

Database uses **Supabase** (managed PostgreSQL):

### Schema

```sql
-- Users
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(100),
  hashed_password VARCHAR(255),
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Conversations
CREATE TABLE conversations (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  title VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Messages
CREATE TABLE messages (
  id UUID PRIMARY KEY,
  conversation_id UUID REFERENCES conversations(id),
  sender_id UUID REFERENCES users(id),
  content TEXT NOT NULL,
  tone VARCHAR(50),
  language VARCHAR(10),
  translated_content TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### SQLAlchemy Models

Models are defined in `app/models/`:

```python
from sqlalchemy import Column, String, DateTime
from app.models.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String)
    hashed_password = Column(String)
```

## 🔄 WebSocket

Real-time communication (optional):

```python
# app/api/websocket.py
from fastapi import WebSocket

@app.websocket("/ws/{conversation_id}")
async def websocket_endpoint(websocket: WebSocket, conversation_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Process message
```

## 📝 Environment Variables

Create `.env` file at root of `backend/` folder:

```env
# Database
DATABASE_URL=postgresql://user:password@host:5432/database
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-key

# Security
SECRET_KEY=your-super-secret-key-min-32-characters
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
FRONTEND_URL=http://localhost:5173

# Translation API
TRANSLATION_API_KEY=your-api-key
TRANSLATION_SERVICE=huggingface  # or other

# Debug
DEBUG=True
```

### Generate Keys

```python
import secrets
print(secrets.token_urlsafe(32))
```

## 🧪 Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest

# With coverage
pytest --cov=app tests/

# Verbose mode
pytest -v
```

### Test Structure

```
tests/
├── test_auth.py         # Auth tests
├── test_conversations.py # Conversation tests
├── test_messages.py      # Message tests
└── conftest.py          # Pytest config
```

## 🚀 Deployment

### Vercel

```bash
# Deploy to Vercel
vercel deploy

# Production
vercel deploy --prod
```

### Environment Variables on Vercel

1. Go to `Settings` > `Environment Variables`
2. Add all variables from `.env`
3. Redeploy

### Docker (optional)

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

```bash
docker build -t multichat-backend .
docker run -p 8000:8000 multichat-backend
```

## 📦 Main Dependencies

See [requirements.txt](./requirements.txt) for complete list.

- **fastapi** - Web framework
- **sqlalchemy** - ORM
- **supabase-py** - Supabase client
- **python-jose** - JWT
- **passlib** - Password hashing
- **pydantic** - Data validation
- **uvicorn** - ASGI server
- **python-multipart** - Form data

## 🔗 Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Supabase Docs](https://supabase.com/docs)
- [JWT.io](https://jwt.io)

## 💡 Tips

- Use Python types for automatic validation
- Structure responses with Pydantic schemas
- Use FastAPI dependencies for reusability
- Document endpoints with docstrings
- Test regularly with Pytest

## 👥 Support

For questions or issues:
1. Check server logs
2. See FastAPI documentation
3. Open an issue on GitHub

---

**Developed with ❤️ for MultiChat**
