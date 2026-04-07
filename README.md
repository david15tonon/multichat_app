# MultiChat 🌐💬

**Application de messagerie multilingue avec traduction en temps réel et adaptation du ton selon le contexte.**

![Status](https://img.shields.io/badge/status-en%20développement-yellow)
![React](https://img.shields.io/badge/React-18.2-blue)
![Python](https://img.shields.io/badge/Python-3.13+-green)
![TypeScript](https://img.shields.io/badge/TypeScript-5.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

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

Voir [backend/README.md](./backend/README.md) pour plus de détails.

### Frontend
- **Framework** : React 18.2
- **Typage** : TypeScript 5.2
- **Styling** : Styled Components 6.1
- **Build** : Vite 5
- **Architecture** : Atomic Design

Voir [frontend/README.md](./frontend/README.md) pour plus de détails.
