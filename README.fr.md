# MultiChat 🌐💬

**Application de messagerie multilingue avec traduction en temps réel et adaptation du ton selon le contexte.**

![Status](https://img.shields.io/badge/status-en%20développement-yellow)
![React](https://img.shields.io/badge/React-18.2-blue)
![Python](https://img.shields.io/badge/Python-3.13+-green)
![TypeScript](https://img.shields.io/badge/TypeScript-5.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

[🇬🇧 English](./README.md)

## 📋 Table des matières

- [🎯 Fonctionnalités](#-fonctionnalités)
- [🏗️ Architecture](#-architecture)
- [🚀 Démarrage rapide](#-démarrage-rapide)
- [📁 Structure du projet](#-structure-du-projet)
- [🔧 Configuration](#-configuration)
- [📦 Dépendances](#-dépendances)
- [🌐 Déploiement](#-déploiement)
- [👥 Contribution](#-contribution)

## 🎯 Fonctionnalités

- **✨ Traduction en temps réel** - Traduction instantanée dans 9+ langues
- **🎭 Adaptation du ton** - Casual, Standard, ou Formel selon le contexte
- **📱 Design moderne** - Interface néo-brutaliste avec couleurs vives
- **🌍 Multilingue** - Support complet de FR, EN, ES, DE, IT, PT, ZH, JA, AR
- **🔐 Authentification sécurisée** - JWT + Refresh tokens
- **💾 Base de données** - Supabase PostgreSQL avec ORM SQLAlchemy
- **🔌 WebSocket** - Communication en temps réel
- **☁️ Cloud-ready** - Déploiement sur Vercel

## 🏗️ Architecture

Le projet est divisé en deux parties :

```
multichat/
├── backend/           # API FastAPI + Services de traduction
│   ├── app/
│   │   ├── api/       # Endpoints (auth, conversations, messages)
│   │   ├── core/      # Configuration, base de données, sécurité
│   │   ├── models/    # Modèles SQLAlchemy
│   │   └── schemas/   # Schémas Pydantic
│   ├── main.py        # Point d'entrée
│   └── requirements.txt
│
└── frontend/          # Application React + TypeScript
    ├── src/
    │   ├── components/ # Atomic Design (atoms, molecules, organisms)
    │   ├── pages/      # Pages principales
    │   ├── services/   # Appels API
    │   ├── types/      # Types TypeScript
    │   └── styles/     # Thème global
    └── package.json
```

## 🚀 Démarrage rapide

### Prérequis

- Node.js >= 18.0.0
- Python >= 3.13
- npm ou yarn
- Compte Supabase (pour la base de données)

### Installation

```bash
# Cloner le repository
git clone https://github.com/david15tonon/multichat_app.git
cd multichat

# Installation Backend
cd backend
python -m venv env
source env/Scripts/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt

# Installation Frontend
cd ../frontend
npm install
```

### Lancer l'application

```bash
# Backend (terminal 1)
cd backend
source env/Scripts/activate
python main.py

# Frontend (terminal 2)
cd frontend
npm run dev
```

L'application sera accessible sur `http://localhost:5173`

## 📁 Structure du projet

### Backend
- **Framework** : FastAPI
- **Base de données** : Supabase (PostgreSQL)
- **ORM** : SQLAlchemy
- **Authentification** : JWT + Refresh tokens
- **Traduction** : Service de traduction IA

Voir [backend/README.fr.md](./backend/README.fr.md) pour plus de détails.

### Frontend
- **Framework** : React 18.2
- **Typage** : TypeScript 5.2
- **Styling** : Styled Components 6.1
- **Build** : Vite 5
- **Architecture** : Atomic Design

Voir [frontend/README.fr.md](./frontend/README.fr.md) pour plus de détails.

## 🔧 Configuration

### Variables d'environnement

Créez un fichier `.env` dans le dossier `backend/` :

```env
# Database
SUPABASE_URL=votre_url_supabase
SUPABASE_KEY=votre_clé_supabase

# JWT
SECRET_KEY=votre_clé_secrète
ALGORITHM=HS256

# CORS
FRONTEND_URL=http://localhost:5173
```

## 📦 Dépendances principales

### Backend
- fastapi
- sqlalchemy
- supabase-py
- python-jose[cryptography]
- pydantic

### Frontend
- react
- typescript
- styled-components
- axios
- react-router-dom

## 🌐 Déploiement

### Frontend (Vercel)

```bash
cd frontend
vercel deploy
```

### Backend (Vercel)

```bash
cd backend
vercel deploy
```

Voir [vercel.json](./vercel.json) pour la configuration.

## 🧪 Tests

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm run test
```

## 📝 License

MIT - Voir [LICENSE](./LICENSE) pour les détails.

## 👥 Contribution

Les contributions sont bienvenues ! Veuillez :

1. Fork le repository
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📧 Support

Pour toute question ou problème, ouvrez une issue sur GitHub.

---

**Développé avec ❤️ par [david15tonon](https://github.com/david15tonon)**
