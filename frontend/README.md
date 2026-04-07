# Frontend - MultiChat App 🎨

**Modern React application with TypeScript, Styled Components and Atomic Design.**

![React](https://img.shields.io/badge/React-18.2-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.2-blue)
![Vite](https://img.shields.io/badge/Vite-5-violet)
![Styled Components](https://img.shields.io/badge/Styled%20Components-6.1-pink)

[🇫🇷 Français](./README.fr.md)

## 📋 Table of Contents

- [🎯 Features](#-features)
- [🏗️ Architecture](#-architecture)
- [🚀 Installation](#-installation)
- [📁 Structure](#-structure)
- [🎨 Design System](#-design-system)
- [🧩 Components](#-components)
- [📱 Pages](#-pages)
- [🔧 Configuration](#-configuration)
- [📦 npm Scripts](#-npm-scripts)
- [🌐 Deployment](#-deployment)

## 🎯 Features

- **✨ Modern Interface** - Neo-brutalist design with vibrant colors
- **🏗️ Atomic Design** - Scalable and reusable architecture
- **📝 Strict TypeScript** - Full typing to avoid errors
- **🎨 Styled Components** - Modular CSS-in-JS
- **⚡ Vite** - Ultra-fast build and HMR
- **🌍 Multilingual** - Support for 9+ languages
- **📱 Responsive** - Mobile, tablet, desktop optimized
- **🔐 Authentication** - JWT with tokens

## 🏗️ Architecture

The application follows the **Atomic Design** pattern for better organization:

```
Atom (smallest)
  ↓
Molecule (combination of atoms)
  ↓
Organism (complete sections)
  ↓
Page (compositions of organisms)
```

## 🚀 Installation

### Prerequisites

- Node.js >= 18.0.0
- npm >= 9.0.0 or yarn >= 3.0.0

### Setup

```bash
# 1. Navigate to frontend folder
cd frontend

# 2. Install dependencies
npm install

# 3. Launch in development mode
npm run dev

# 4. Open http://localhost:5173
```

## 📁 Structure

```
frontend/
├── public/                    # Static assets
├── src/
│   ├── index.tsx             # React entry point
│   ├── App.tsx               # Main component
│   ├── components/
│   │   ├── atoms/            # Basic components
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   ├── Icon.tsx
│   │   │   ├── Avatar.tsx
│   │   │   ├── Badge.tsx
│   │   │   └── index.ts       # Barrel export
│   │   ├── molecules/         # Composed components
│   │   │   ├── MessageBubble.tsx
│   │   │   ├── ToneSelector.tsx
│   │   │   ├── LanguagePicker.tsx
│   │   │   └── index.ts
│   │   └── organisms/         # Complete sections
│   │       ├── Header.tsx
│   │       ├── MessageComposer.tsx
│   │       └── index.ts
│   ├── pages/                 # Complete pages
│   │   ├── LoginPage.tsx
│   │   ├── ChatPage.tsx
│   │   ├── SettingsPage.tsx
│   │   ├── ForgotPassword.tsx
│   │   ├── SignupPage.tsx
│   │   └── index.ts
│   ├── services/              # API services
│   │   └── api.ts             # HTTP calls
│   ├── types/                 # TypeScript types
│   │   └── index.ts           # Shared types
│   └── styles/                # Global styles
│       ├── GlobalStyles.ts
│       ├── theme.ts           # Theme config
│       └── styled.d.ts        # Styled types
├── index.html                 # Root HTML
├── package.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts            # Vite config
└── vercel.json               # Vercel config
```

## 🎨 Design System

### Color Palette

```typescript
// src/styles/theme.ts

const colors = {
  primary: {
    yellow: "#FDB924",    // Energy and optimism
    orange: "#FF6B35",    // Warmth and dynamism
    purple: "#6C5CE7",    // Innovation and creativity
  },
  neutral: {
    black: "#000000",     // Text and borders
    white: "#F5F5F0",     // Background
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

### Typography

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

### Spacing

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

## 🧩 Components

### Atoms

#### Button

```tsx
import { Button } from "@/components/atoms";

// Default
<Button>Click me</Button>

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
  placeholder="Password"
  error="Invalid password"
/>
```

#### Avatar

```tsx
import { Avatar } from "@/components/atoms";

<Avatar 
  src="https://..."
  alt="User"
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
    content: "Hello!",
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
  selected="en"
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

- Email/password form
- Social login (Google, Apple, Twitter)
- Link to signup and password reset

**Route**: `/login`

### SignupPage

- Signup form
- Email validation
- Password confirmation

**Route**: `/signup`

### ChatPage

- Conversation list
- Message area
- Tone selector
- Real-time translation

**Route**: `/chat` (protected)

### SettingsPage

- Language selection
- Tone configuration
- User profile

**Route**: `/settings` (protected)

### ForgotPassword

- Password reset by email
- Token confirmation

**Route**: `/forgot-password`

## 🔧 Configuration

### Environment Variables

Create a `.env.local` file:

```env
VITE_API_URL=http://localhost:8000
VITE_DEBUG=true
```

### Theme

Modify `src/styles/theme.ts` to customize:

```typescript
export const colors = {
  // Your colors
};

export const theme = {
  colors,
  // Other config
};
```

### Axios/API

`src/services/api.ts`:

```typescript
import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// Interceptor for JWT token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```

## 📦 npm Scripts

```bash
# Development
npm run dev              # Start Vite

# Build
npm run build            # Production build
npm run build:lib        # Library build

# Preview
npm run preview          # Preview build

# Code Quality
npm run lint             # ESLint
npm run format           # Prettier
npm run typecheck        # TypeScript check

# Tests
npm run test             # Run tests
npm run test:ui          # Vitest UI
npm run coverage         # Test coverage

# Deployment
npm run deploy           # Deploy to Vercel
```

## 🌐 Deployment

### Vercel (recommended)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Production
vercel --prod
```

### GitHub Pages

```bash
# Build
npm run build

# Deploy with gh-pages
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
# Run tests
npm run test

# Watch mode
npm run test:watch

# With coverage
npm run coverage
```

### Test Structure

```
src/__tests__/
├── components/
│   ├── atoms/
│   │   └── Button.test.tsx
│   └── molecules/
└── pages/
```

## 📖 Code Conventions

### File Naming

- **Components**: `PascalCase` (Button.tsx)
- **Hooks**: `camelCase` (useAuth.ts)
- **Services**: `camelCase` (authService.ts)
- **Types**: `PascalCase` (User.ts)

### Component Structure

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
// 1. React/external libs
import { FC } from "react";
import styled from "styled-components";

// 2. Local components
import { Header } from "@/components/organisms";

// 3. Hooks/utils
import { useAuth } from "@/hooks";

// 4. Types
import { User } from "@/types";
```

## 🔗 Resources

- [React Docs](https://react.dev)
- [TypeScript Docs](https://www.typescriptlang.org/docs/)
- [Styled Components](https://styled-components.com/)
- [Vite Docs](https://vitejs.dev/)
- [Atomic Design](https://atomicdesign.bradfrost.com/)

## 💡 Tips

- Use barrel exports (`index.ts`) to simplify imports
- Document components with JSDoc comments
- Test regularly
- Respect Atomic Design for scalability
- Use CSS variables for themes

## 👥 Support

For questions or issues:
1. Check Vite/React documentation
2. Verify browser console
3. Open an issue on GitHub

---

**Developed with ❤️ for MultiChat**
