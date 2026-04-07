# Backend - API MultiChat 🚀

**FastAPI pour MultiChat avec authentification JWT, gestion de conversations avec Supabase et traduction IA.**

![Python](https://img.shields.io/badge/Python-3.13+-green)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-blue)
![Status](https://img.shields.io/badge/status-en%20développement-yellow)

[🇬🇧 English](./README.md)

## 📋 Table des matières

- [🎯 Fonctionnalités](#-fonctionnalités)
- [🏗️ Structure](#-structure)
- [🚀 Installation](#-installation)
- [📖 Endpoints API](#-endpoints-api)
- [🔐 Authentification](#-authentification)
- [🗄️ Base de données](#️-base-de-données)
- [🔄 WebSocket](#-websocket)
- [📝 Variables d'environnement](#-variables-denvironnement)
- [🧪 Tests](#-tests)

## 🎯 Fonctionnalités

- **🔐 Authentification JWT** - Tokens d'accès et refresh
- **👤 Gestion d'utilisateurs** - Création, profil, mise à jour
- **💬 Conversations** - Création, récupération, suppression
- **💭 Messages** - Envoi, traduction, historique
- **🌐 Traduction** - Service de traduction IA intégré
- **📡 WebSocket** - Communication temps réel (optionnel)
- **🔑 Sécurité** - CORS, rate limiting, validation Pydantic

## 🏗️ Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py              # Router principal
│   │   ├── auth.py              # Endpoints d'authentification
│   │   ├── conversations.py      # Endpoints de conversations
│   │   ├── messages.py          # Endpoints de messages
│   │   ├── translate.py         # Endpoints de traduction
│   │   └── deps.py              # Dépendances FastAPI
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py            # Configuration et variables d'env
│   │   ├── security.py          # Sécurité JWT, hash passwords
│   │   ├── database.py          # Session SQLAlchemy
│   │   └── supabase.py          # Client Supabase
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py              # Base model
│   │   ├── user.py              # User model
│   │   ├── conversation.py      # Conversation model
│   │   ├── message.py           # Message model
│   │   └── enums.py             # Enums (Tone, Language)
│   └── schemas/
│       ├── __init__.py
│       ├── auth.py              # Schemas pour auth
│       ├── conversation.py      # Schemas de conversations
│       ├── message.py           # Schemas de messages
│       └── translate.py         # Schemas de traduction
├── main.py                       # Point d'entrée
├── requirements.txt              # Dépendances Python
└── vercel.json                   # Configuration Vercel
```

## 🚀 Installation

### Prérequis

- Python >= 3.13
- pip ou conda
- Compte Supabase avec PostgreSQL

### Setup

```bash
# 1. Naviguer au dossier backend
cd backend

# 2. Créer un environnement virtuel
python -m venv env

# 3. Activer l'environnement
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Créer le fichier .env
touch .env

# 6. Lancer le serveur
python main.py
```

Le serveur démarre sur `http://localhost:8000`

### Documentation API

- **Swagger UI** : `http://localhost:8000/docs`
- **ReDoc** : `http://localhost:8000/redoc`

## 📖 Endpoints API

### Authentication

```
POST   /api/auth/register          # Créer un compte
POST   /api/auth/login             # Se connecter
POST   /api/auth/refresh           # Rafraîchir le token
POST   /api/auth/logout            # Se déconnecter
GET    /api/auth/me                # Profil utilisateur
PUT    /api/auth/me                # Mettre à jour le profil
```

### Conversations

```
GET    /api/conversations          # Lister les conversations
POST   /api/conversations          # Créer une conversation
GET    /api/conversations/{id}     # Détail d'une conversation
PUT    /api/conversations/{id}     # Mettre à jour
DELETE /api/conversations/{id}     # Supprimer
```

### Messages

```
GET    /api/conversations/{id}/messages      # Lister les messages
POST   /api/conversations/{id}/messages      # Envoyer un message
DELETE /api/messages/{id}                    # Supprimer un message
```

### Traduction

```
POST   /api/translate              # Traduire un message
POST   /api/translate/batch        # Traduction en masse
```

## 🔐 Authentification

### JWT Token

La authentification utilise des **JWT tokens** :

```bash
# Token d'accès (court terme)
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

# Refresh token (long terme)
{
  "token_type": "bearer",
  "access_token": "...",
  "refresh_token": "..."
}
```

### Flux

1. **Register** : Créer un compte
2. **Login** : Recevoir access_token + refresh_token
3. **Utiliser** : Ajouter token aux headers
4. **Rafraîchir** : Utiliser refresh_token pour nouveau access_token

```python
# Exemple avec requests
import requests

headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get("http://localhost:8000/api/auth/me", headers=headers)
```

## 🗄️ Base de données

### Supabase PostgreSQL

La base de données utilise **Supabase** (PostgreSQL managed) :

### Schéma

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

### Modèles SQLAlchemy

Les modèles sont définis dans `app/models/` :

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

Communication temps réel (optionnel) :

```python
# app/api/websocket.py
from fastapi import WebSocket

@app.websocket("/ws/{conversation_id}")
async def websocket_endpoint(websocket: WebSocket, conversation_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Traiter le message
```

## 📝 Variables d'environnement

Créez un fichier `.env` à la racine du dossier `backend/` :

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
TRANSLATION_SERVICE=huggingface  # ou autre

# Debug
DEBUG=True
```

### Génération des clés

```python
import secrets
print(secrets.token_urlsafe(32))
```

## 🧪 Tests

```bash
# Installation des dépendances de test
pip install pytest pytest-asyncio httpx

# Lancer les tests
pytest

# Avec couverture
pytest --cov=app tests/

# Mode verbose
pytest -v
```

### Structure des tests

```
tests/
├── test_auth.py         # Tests authentification
├── test_conversations.py # Tests conversations
├── test_messages.py      # Tests messages
└── conftest.py          # Configuration pytest
```

## 🚀 Déploiement

### Vercel

```bash
# Déployer sur Vercel
vercel deploy

# Production
vercel deploy --prod
```

### Variables d'environnement sur Vercel

1. Aller sur `Settings` > `Environment Variables`
2. Ajouter toutes les variables du `.env`
3. Redéployer

### Docker (optionnel)

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

## 📦 Dépendances principales

Voir [requirements.txt](./requirements.txt) pour la liste complète.

- **fastapi** - Framework web
- **sqlalchemy** - ORM
- **supabase-py** - Client Supabase
- **python-jose** - JWT
- **passlib** - Hash passwords
- **pydantic** - Validation données
- **uvicorn** - ASGI server
- **python-multipart** - Form data

## 🔗 Ressources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Supabase Docs](https://supabase.com/docs)
- [JWT.io](https://jwt.io)

## 💡 Conseils

- Utilisez les types Python pour une validation automatique
- Structurez les réponses avec Pydantic schemas
- Utilisez des dépendances FastAPI pour la réutilisation
- Documentez vos endpoints avec des docstrings
- Testez régulièrement avec Pytest

## 👥 Support

Pour des questions ou problèmes :
1. Vérifiez les logs du serveur
2. Consultez la documentation FastAPI
3. Ouvrez une issue sur GitHub

---

**Développé avec ❤️ pour MultiChat**
