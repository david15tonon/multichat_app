# Frontend - Application MultiChat 🎨

**Application React moderne avec TypeScript, Styled Components et Atomic Design.**

![React](https://img.shields.io/badge/React-18.2-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.2-blue)
![Vite](https://img.shields.io/badge/Vite-5-violet)
![Styled Components](https://img.shields.io/badge/Styled%20Components-6.1-pink)

[🇬🇧 English](./README.md)

## 📋 Table des matières

- [🎯 Fonctionnalités](#-fonctionnalités)
- [🏗️ Architecture](#-architecture)
- [🚀 Installation](#-installation)
- [📁 Structure](#-structure)
- [🎨 Design System](#-design-system)
- [🧩 Composants](#-composants)
- [📱 Pages](#-pages)
- [🔧 Configuration](#-configuration)
- [📦 Scripts npm](#-scripts-npm)
- [🌐 Déploiement](#-déploiement)

## 🎯 Fonctionnalités

- **✨ Interface moderne** - Design néo-brutaliste avec couleurs vives
- **🏗️ Atomic Design** - Architecture scalable et réutilisable
- **📝 TypeScript strict** - Typage complet pour éviter les erreurs
- **🎨 Styled Components** - CSS-in-JS modulaire
- **⚡ Vite** - Build ultra-rapide et HMR
- **🌍 Multilingue** - Support pour 9+ langues
- **📱 Responsive** - Optimisé mobile, tablet, desktop
- **🔐 Authentification** - JWT avec tokens

## 🏗️ Architecture

L'application suit le pattern **Atomic Design** pour une meilleure organisation :

```
Atom (plus petit)
  ↓
Molecule (combinaison d'atoms)
  ↓
Organism (sections complètes)
  ↓
Page (compositions d'organisms)
```

## 🚀 Installation

### Prérequis

- Node.js >= 18.0.0
- npm >= 9.0.0 ou yarn >= 3.0.0

### Setup

```bash
# 1. Naviguer au dossier frontend
cd frontend

# 2. Installer les dépendances
npm install

# 3. Lancer en mode développement
npm run dev

# 4. Ouvrir http://localhost:5173
```

## 📁 Structure

```
frontend/
├── public/                    # Assets statiques
├── src/
│   ├── index.tsx             # Point d'entrée React
│   ├── App.tsx               # Composant principal
│   ├── components/
│   │   ├── atoms/            # Composants de base
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   ├── Icon.tsx
│   │   │   ├── Avatar.tsx
│   │   │   ├── Badge.tsx
│   │   │   └── index.ts       # Barrel export
│   │   ├── molecules/         # Composants composés
│   │   │   ├── MessageBubble.tsx
│   │   │   ├── ToneSelector.tsx
│   │   │   ├── LanguagePicker.tsx
│   │   │   └── index.ts
│   │   └── organisms/         # Sections complètes
│   │       ├── Header.tsx
│   │       ├── MessageComposer.tsx
│   │       └── index.ts
│   ├── pages/                 # Pages complètes
│   │   ├── LoginPage.tsx
│   │   ├── ChatPage.tsx
│   │   ├── SettingsPage.tsx
│   │   ├── ForgotPassword.tsx
│   │   ├── SignupPage.tsx
│   │   └── index.ts
│   ├── services/              # Services API
│   │   └── api.ts             # Appels HTTP
│   ├── types/                 # Types TypeScript
│   │   └── index.ts           # Types partagés
│   └── styles/                # Styles globaux
│       ├── GlobalStyles.ts
│       ├── theme.ts           # Configuration thème
│       └── styled.d.ts        # Types styled-components
├── index.html                 # HTML racine
├── package.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts            # Configuration Vite
└── vercel.json               # Configuration Vercel
```

## 🎨 Design System

### Palette de couleurs

```typescript
// src/styles/theme.ts

const colors = {
  primary: {
    yellow: "#FDB924",    // Énergie et optimisme
    orange: "#FF6B35",    // Chaleur et dynamisme
    purple: "#6C5CE7",    // Innovation et créativité
  },
  neutral: {
    black: "#000000",     // Texte et bordures
    white: "#F5F5F0",     // Arrière-plan
    gray: "#8B8B8B",
  },
  semantic: {
    success: "#27AE60",
    error: "#E74C3C",
    warning: "#F39C12",
    info: "#3498DB",
  },
};
```

### Typographie

```typescript
const typography = {
  fonts: {
    primary: "'Inter', sans-serif",
    display: "'Playfair Display', serif",
  },
  sizes: {
    xs: "0.75rem",      // 12px
    sm: "0.875rem",     // 14px
    base: "1rem",       // 16px
    lg: "1.125rem",     // 18px
    xl: "1.25rem",      // 20px
    "2xl": "1.5rem",    // 24px
    "3xl": "2rem",      // 32px
  },
};
```

### Espacements

```typescript
const spacing = {
  xs: "0.25rem",     // 4px
  sm: "0.5rem",      // 8px
  md: "1rem",        // 16px
  lg: "1.5rem",      // 24px
  xl: "2rem",        // 32px
  "2xl": "3rem",     // 48px
};
```

## 🧩 Composants

### Atoms

#### Button

```tsx
import { Button } from "@/components/atoms";

// Default
<Button>Cliquez-moi</Button>

// Variants
<Button variant="primary">Primary</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="outline">Outline</Button>

// Sizes
<Button size="small">Small</Button>
<Button size="medium">Medium</Button>
<Button size="large">Large</Button>

// States
<Button disabled>Disabled</Button>
<Button loading>Loading</Button>
<Button fullWidth>Full Width</Button>
```

#### Input

```tsx
import { Input } from "@/components/atoms";

<Input 
  type="email"
  placeholder="Email"
  value={email}
  onChange={(e) => setEmail(e.target.value)}
/>

<Input 
  type="password"
  placeholder="Mot de passe"
  error="Mot de passe invalide"
/>
```

#### Avatar

```tsx
import { Avatar } from "@/components/atoms";

<Avatar 
  src="https://..."
  alt="Utilisateur"
  size="lg"
  online={true}
/>
```

### Molecules

#### MessageBubble

```tsx
import { MessageBubble } from "@/components/molecules";

<MessageBubble
  message={{
    id: "1",
    content: "Bonjour !",
    sender: "Alice",
    timestamp: new Date(),
    tone: "casual",
  }}
  isOwn={false}
  showTranslation={true}
/>
```

#### ToneSelector

```tsx
import { ToneSelector } from "@/components/molecules";

<ToneSelector
  selected="standard"
  onChange={(tone) => setTone(tone)}
/>
```

#### LanguagePicker

```tsx
import { LanguagePicker } from "@/components/molecules";

<LanguagePicker
  selected="fr"
  onChange={(lang) => setLanguage(lang)}
/>
```

### Organisms

#### Header

```tsx
import { Header } from "@/components/organisms";

<Header 
  user={currentUser}
  onLogout={handleLogout}
/>
```

#### MessageComposer

```tsx
import { MessageComposer } from "@/components/organisms";

<MessageComposer
  onSend={(message) => handleSend(message)}
  tone={tone}
/>
```

## 📱 Pages

### LoginPage

- Formulaire email/mot de passe
- Connexion sociale (Google, Apple, Twitter)
- Lien vers inscription et réinitialisation

**Route** : `/login`

### SignupPage

- Formulaire d'inscription
- Validation email
- Confirmation mot de passe

**Route** : `/signup`

### ChatPage

- Liste des conversations
- Zone de messages
- Sélecteur de ton
- Traduction en temps réel

**Route** : `/chat` (protégée)

### SettingsPage

- Sélection de langue
- Configuration du ton
- Profil utilisateur

**Route** : `/settings` (protégée)

### ForgotPassword

- Réinitialisation par email
- Confirmation par token

**Route** : `/forgot-password`

## 🔧 Configuration

### Variables d'environnement

Créez un fichier `.env.local` :

```env
VITE_API_URL=http://localhost:8000
VITE_DEBUG=true
```

### Thème

Modifiez `src/styles/theme.ts` pour personnaliser :

```typescript
export const colors = {
  // Vos couleurs
};

export const theme = {
  colors,
  // Autres configurations
};
```

### Axios/API

`src/services/api.ts` :

```typescript
import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// Intercepteur pour le token JWT
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```

## 📦 Scripts npm

```bash
# Développement
npm run dev              # Démarrer Vite

# Build
npm run build            # Build production
npm run build:lib        # Build library

# Preview
npm run preview          # Prévisualiser le build

# Qualité du code
npm run lint             # ESLint
npm run format           # Prettier
npm run typecheck        # TypeScript check

# Tests
npm run test             # Lancer tests
npm run test:ui          # Vitest UI
npm run coverage         # Couverture tests

# Déploiement
npm run deploy           # Déployer sur Vercel
```

## 🌐 Déploiement

### Vercel (recommandé)

```bash
# Installation CLI Vercel
npm install -g vercel

# Déployer
vercel

# Production
vercel --prod
```

### GitHub Pages

```bash
# Build
npm run build

# Déployer avec gh-pages
npm run deploy
```

### Docker

```dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
RUN npm install -g serve
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]
```

```bash
docker build -t multichat-frontend .
docker run -p 3000:3000 multichat-frontend
```

## 🧪 Tests

### Vitest + React Testing Library

```bash
# Lancer les tests
npm run test

# Mode watch
npm run test:watch

# Avec couverture
npm run coverage
```

### Structure des tests

```
src/__tests__/
├── components/
│   ├── atoms/
│   │   └── Button.test.tsx
│   └── molecules/
└── pages/
```

## 📖 Conventions de code

### Nommage des fichiers

- **Composants** : `PascalCase` (Button.tsx)
- **Hooks** : `camelCase` (useAuth.ts)
- **Services** : `camelCase` (authService.ts)
- **Types** : `PascalCase` (User.ts)

### Structure des composants

```typescript
import styled from "styled-components";
import { FC } from "react";

interface Props {
  label: string;
  onClick: () => void;
}

const StyledButton = styled.button`
  /* styles */
`;

export const Button: FC<Props> = ({ label, onClick }) => {
  return <StyledButton onClick={onClick}>{label}</StyledButton>;
};
```

### Imports

```typescript
// 1. React/libs externes
import { FC } from "react";
import styled from "styled-components";

// 2. Composants locaux
import { Header } from "@/components/organisms";

// 3. Hooks/utils
import { useAuth } from "@/hooks";

// 4. Types
import { User } from "@/types";
```

## 🔗 Ressources

- [React Docs](https://react.dev)
- [TypeScript Docs](https://www.typescriptlang.org/docs/)
- [Styled Components](https://styled-components.com/)
- [Vite Docs](https://vitejs.dev/)
- [Atomic Design](https://atomicdesign.bradfrost.com/)

## 💡 Conseils

- Utilisez les barrel exports (`index.ts`) pour simplifier les imports
- Documentez vos composants avec des commentaires JSDoc
- Testez régulièrement vos composants
- Respectez l'Atomic Design pour la scalabilité
- Utilisez des variables CSS pour les thèmes

## 👥 Support

Pour des questions ou problèmes :
1. Consultez la documentation Vite/React
2. Vérifiez la console du navigateur
3. Ouvrez une issue sur GitHub

---

**Développé avec ❤️ pour MultiChat**
