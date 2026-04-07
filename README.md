# MultiChat 🌐💬

**Multilingual messaging application with real-time translation and tone adaptation based on context.**

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![React](https://img.shields.io/badge/React-18.2-blue)
![Python](https://img.shields.io/badge/Python-3.13+-green)
![TypeScript](https://img.shields.io/badge/TypeScript-5.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

[🇫🇷 Français](./README.fr.md)

## 📋 Table of Contents

- [🎯 Features](#-features)
- [🏗️ Architecture](#-architecture)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🔧 Configuration](#-configuration)
- [📦 Dependencies](#-dependencies)
- [🌐 Deployment](#-deployment)
- [👥 Contributing](#-contributing)

## 🎯 Features

- **✨ Real-time Translation** - Instant translation to 9+ languages
- **🎭 Tone Adaptation** - Casual, Standard, or Formal based on context
- **📱 Modern Design** - Neo-brutalist interface with vibrant colors
- **🌍 Multilingual** - Full support for FR, EN, ES, DE, IT, PT, ZH, JA, AR
- **🔐 Secure Authentication** - JWT + Refresh tokens
- **💾 Database** - Supabase PostgreSQL with SQLAlchemy ORM
- **🔌 WebSocket** - Real-time communication
- **☁️ Cloud-ready** - Vercel deployment

## 🏗️ Architecture

The project is divided into two parts:

```
multichat/
├── backend/           # FastAPI + Translation Services
│   ├── app/
│   │   ├── api/       # Endpoints (auth, conversations, messages)
│   │   ├── core/      # Config, database, security
│   │   ├── models/    # SQLAlchemy models
│   │   └── schemas/   # Pydantic schemas
│   ├── main.py        # Entry point
│   └── requirements.txt
│
└── frontend/          # React + TypeScript App
    ├── src/
    │   ├── components/ # Atomic Design (atoms, molecules, organisms)
    │   ├── pages/      # Main pages
    │   ├── services/   # API calls
    │   ├── types/      # TypeScript types
    │   └── styles/     # Global theme
    └── package.json
```

## 🚀 Quick Start

### Prerequisites

- Node.js >= 18.0.0
- Python >= 3.13
- npm or yarn
- Supabase account (for database)

### Installation

```bash
# Clone the repository
git clone https://github.com/david15tonon/multichat_app.git
cd multichat

# Backend Installation
cd backend
python -m venv env
source env/Scripts/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt

# Frontend Installation
cd ../frontend
npm install
```

### Running the Application

```bash
# Backend (terminal 1)
cd backend
source env/Scripts/activate
python main.py

# Frontend (terminal 2)
cd frontend
npm run dev
```

The application will be accessible at `http://localhost:5173`

## 📁 Project Structure

### Backend
- **Framework**: FastAPI
- **Database**: Supabase (PostgreSQL)
- **ORM**: SQLAlchemy
- **Authentication**: JWT + Refresh tokens
- **Translation**: AI translation service

See [backend/README.md](./backend/README.md) for more details.

### Frontend
- **Framework**: React 18.2
- **Typing**: TypeScript 5.2
- **Styling**: Styled Components 6.1
- **Build**: Vite 5
- **Architecture**: Atomic Design

See [frontend/README.md](./frontend/README.md) for more details.

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `backend/` folder:

```env
# Database
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

# JWT
SECRET_KEY=your_secret_key
ALGORITHM=HS256

# CORS
FRONTEND_URL=http://localhost:5173
```

## 📦 Main Dependencies

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

## 🌐 Deployment

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

See [vercel.json](./vercel.json) for configuration.

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

MIT - See [LICENSE](./LICENSE) for details.

## 👥 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For any questions or issues, open an issue on GitHub.

---

**Developed with ❤️ by [david15tonon](https://github.com/david15tonon)**
