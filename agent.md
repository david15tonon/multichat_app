# Agent Project Instructions: MultiChat

## 1. Context & Role
Tu es un expert Fullstack specialise en **FastAPI (Python)** et **React/Next.js (TypeScript)**. Ton objectif est de construire **MultiChat**, une application de messagerie multilingue avec traduction en temps reel et adaptation du ton.

---

## 2. Tech Stack & Constraints
- **Frontend :** React/TypeScript (Vite), Design Neo-Brutaliste, Tailwind CSS.
- **Backend :** FastAPI (Python) deploye en Serverless sur Vercel via `mangum`.
- **Base de donnees & Auth :** Supabase (PostgreSQL via SQLAlchemy). **Priorite : Email/Password**. OAuth (Google/Apple) en option secondaire.
- **Moteur IA :** **Groq Cloud (Llama-3.3-70b-versatile)** pour la traduction et le changement de ton.
- **Hebergement :** Vercel (Monorepo avec `/frontend` et `/backend`). **Zero carte de credit requise.**

---

## 3. Database Schema (SQLAlchemy Models)
Applique strictement les modeles suivants :

### User Model (`users`)
- Champs : `id` (UUID), `email`, `full_name`, `hashed_password`, `preferred_language` (Enum), `preferred_tone` (Enum), `is_active`, `is_online`.
- Enums Langues : `FR, EN, ES, DE, IT, PT, ZH, JA, AR`.
- Enums Ton : `CASUAL, STANDARD, FORMAL`.

### Message & Conversation Models
- **Message :** `content` (original), `original_language`, `translated_content`, `target_language`, `tone`, `status` (sending, sent, read), `translation_status`.
- **Conversation :** `is_group`, `name`. Relation Many-to-Many avec les utilisateurs via `ConversationParticipant`.

---

## 4. Backend Rules (FastAPI)
- **Localisation :** Tout le code backend doit etre dans le dossier `/backend`.
- **Vercel Integration :** Le fichier `main.py` doit exporter `handler = Mangum(app)`.
- **CORS :** Autoriser les requetes venant du frontend.
- **Translation Logic :**
    - Utiliser le client `Groq`.
    - Prompt systeme : `"Tu es un traducteur expert. Traduis en {target_language} avec un ton {tone}. Reponds uniquement par la traduction."`
- **Authentification :** Utiliser JWT. La connexion par email est le flux principal.

---

## 6. Project Structure (Vercel Ready)
```text
multichat/
|-- vercel.json           # Config routing (API -> /backend, Reste -> /frontend)
|-- backend/
|   |-- main.py           # Entry point FastAPI + Mangum
|   |-- requirements.txt  # fastapi, mangum, groq, supabase, sqlalchemy
|   |-- app/
|   |   |-- models/       # SQLAlchemy models
|   |   |-- api/          # Routes (auth, messages, translate)
|   |   `-- core/         # Config (Groq API, Supabase)
`-- frontend/
    `-- src/
        |-- components/   # Atomic design structure
        |-- pages/        # LoginPage, ChatPage, SettingsPage
        `-- styles/       # Neo-Brutalist theme
```

le frontend est deja bon il ne reste qu'a le connecter au backend

---

## 7. Instructions specifiques pour l'IA
- **Ne jamais** demander de carte de credit.
- **Utiliser Groq** pour la rapidite extreme en traduction.
- **Respecter le typage TS** sur le frontend.
- **Mode Hors Ligne :** Implementer une gestion d'etat (Redux/Zustand ou simple state) qui affiche un badge "Offline" et met les messages en file d'attente (Status: `SENDING`).
- **Adaptation du Ton :** S'assurer que le backend passe bien le parametre `tone` a la fonction de traduction.

---

### Variables d'environnement requises :
- `GROQ_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `DATABASE_URL` (Postgres Supabase)
- `JWT_SECRET`
