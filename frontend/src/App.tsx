import React, { useState, useEffect } from 'react';
import { ThemeProvider } from 'styled-components';
import { GlobalStyles } from './styles/GlobalStyles';
import { theme } from './styles/theme';
import { LoginPage } from './pages/LoginPage';
import { SignupPage } from './pages/SignupPage';
import { ChatPage } from './pages/ChatPage';
import { SettingsPage } from './pages/SettingsPage';
import { Message, MessageTone, Language } from './types';
import { translationAPI, healthAPI, authAPI } from './services/api';

type AppScreen = 'login' | 'signup' | 'chat' | 'settings';

interface AuthState {
  isAuthenticated: boolean;
  token: string | null;
  user: {
    id: string;
    email: string;
    fullName: string;
    preferredLanguage: Language;
  } | null;
  loading: boolean;
  error: string | null;
}

function App() {
  const [currentScreen, setCurrentScreen] = useState<AppScreen>('login');
  const [language, setLanguage] = useState<Language>('fr');
  const [tone, setTone] = useState<MessageTone>('standard');
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      senderId: 'contact-1',
      receiverId: 'user-1',
      content: 'Bonjour ! Je voulais juste vérifier comment se passe le développement de l\'application.',
      originalLanguage: 'en',
      translatedContent: 'Hi! I just wanted to check in and see how the development of the app is going.',
      targetLanguage: 'fr',
      tone: 'standard',
      timestamp: new Date(Date.now() - 3600000),
      status: 'read',
      translationStatus: 'translated',
    },
    {
      id: '2',
      senderId: 'user-1',
      receiverId: 'contact-1',
      content: "C'est super! La traduction en temps réel fonctionne-t-elle sans problème ?",
      originalLanguage: 'fr',
      translatedContent: "That sounds amazing! Is the real-time translation working smoothly?",
      targetLanguage: 'en',
      tone: 'standard',
      timestamp: new Date(Date.now() - 3000000),
      status: 'read',
      translationStatus: 'translated',
    },
  ]);

  const [auth, setAuth] = useState<AuthState>({
    isAuthenticated: false,
    token: null,
    user: null,
    loading: true,
    error: null,
  });

  const [backendConnected, setBackendConnected] = useState(false);
  const [isTranslating, setIsTranslating] = useState(false);

  // Initialize auth state from localStorage and verify token
  useEffect(() => {
    const initializeAuth = async () => {
      const token = localStorage.getItem('access_token');
      if (token) {
        try {
          const user = await authAPI.getCurrentUser(token);
          setAuth({
            isAuthenticated: true,
            token,
            user: {
              id: user.id,
              email: user.email,
              fullName: user.full_name,
              preferredLanguage: user.preferred_language as Language,
            },
            loading: false,
            error: null,
          });
          setLanguage(user.preferred_language as Language);
          setCurrentScreen('chat');
        } catch (error) {
          localStorage.removeItem('access_token');
          setAuth({
            isAuthenticated: false,
            token: null,
            user: null,
            loading: false,
            error: null,
          });
          setCurrentScreen('login');
        }
      } else {
        setAuth((prev) => ({ ...prev, loading: false }));
      }
    };

    initializeAuth();

    healthAPI
      .check()
      .then(() => {
        setBackendConnected(true);
        console.log('✅ Backend connection established');
      })
      .catch((error) => {
        setBackendConnected(false);
        console.error('❌ Backend connection failed:', error.message);
      });
  }, []);

  const handleLogin = async (email: string, password: string) => {
    setAuth((prev) => ({ ...prev, loading: true, error: null }));
    try {
      const response = await authAPI.login(email, password);
      localStorage.setItem('access_token', response.access_token);
      
      // Fetch user info
      const user = await authAPI.getCurrentUser(response.access_token);
      
      setAuth({
        isAuthenticated: true,
        token: response.access_token,
        user: {
          id: user.id,
          email: user.email,
          fullName: user.full_name,
          preferredLanguage: user.preferred_language as Language,
        },
        loading: false,
        error: null,
      });
      setLanguage(user.preferred_language as Language);
      setCurrentScreen('chat');
    } catch (error: any) {
      setAuth((prev) => ({
        ...prev,
        loading: false,
        error: error.message || 'Erreur de connexion',
      }));
    }
  };

  const handleSignup = async (email: string, password: string, fullName: string) => {
    setAuth((prev) => ({ ...prev, loading: true, error: null }));
    try {
      const response = await authAPI.signup(email, password, fullName, 'fr');
      localStorage.setItem('access_token', response.access_token);
      
      // Fetch user info
      const user = await authAPI.getCurrentUser(response.access_token);
      
      setAuth({
        isAuthenticated: true,
        token: response.access_token,
        user: {
          id: user.id,
          email: user.email,
          fullName: user.full_name,
          preferredLanguage: user.preferred_language as Language,
        },
        loading: false,
        error: null,
      });
      setLanguage(user.preferred_language as Language);
      setCurrentScreen('chat');
    } catch (error: any) {
      setAuth((prev) => ({
        ...prev,
        loading: false,
        error: error.message || 'Erreur d\'inscription',
      }));
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    setAuth({
      isAuthenticated: false,
      token: null,
      user: null,
      loading: false,
      error: null,
    });
    setCurrentScreen('login');
  };

  const handleSettingsClick = () => {
    setCurrentScreen('settings');
  }

  const handleSendMessage = async (content: string, messageTone: MessageTone) => {
    // Determine target language for translation
    const targetLanguage: Language = language === 'fr' ? 'en' : 'fr';

    const newMessage: Message = {
      id: Date.now().toString(),
      senderId: 'user-1',
      receiverId: 'contact-1',
      content,
      originalLanguage: language,
      targetLanguage,
      tone: messageTone,
      timestamp: new Date(),
      status: 'sending',
      translationStatus: 'translating',
    };

    setMessages([...messages, newMessage]);
    setIsTranslating(true);

    try {
      const result = await translationAPI.translate(content, targetLanguage, messageTone);
      
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === newMessage.id
            ? {
                ...msg,
                status: 'sent',
                translationStatus: 'translated',
                translatedContent: result.translated_text,
              }
            : msg
        )
      );
      setIsTranslating(false);
    } catch (error) {
      console.error('Translation error:', error);
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === newMessage.id
            ? {
                ...msg,
                status: 'sent',
                translationStatus: 'failed',
              }
            : msg
        )
      );
      setIsTranslating(false);
    }
  };

  // Show loading state while checking auth
  if (auth.loading) {
    return (
      <ThemeProvider theme={theme}>
        <GlobalStyles />
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
          <p>Chargement...</p>
        </div>
      </ThemeProvider>
    );
  }

  return (
    <ThemeProvider theme={theme}>
      <GlobalStyles />
      
      {!auth.isAuthenticated && currentScreen === 'login' && (
        <LoginPage
          onLogin={handleLogin}
          onSocialLogin={() => console.log('Social login not implemented')}
          onForgotPassword={() => console.log('Forget password not implemented')}
          onSignup={() => setCurrentScreen('signup')}
          isLoading={auth.loading}
          error={auth.error || undefined}
        />
      )}

      {!auth.isAuthenticated && currentScreen === 'signup' && (
        <SignupPage
          onSignup={(fullName, email, password) => handleSignup(email, password, fullName)}
          onSocialSignup={() => console.log('Social signup not implemented')}
          onLoginClick={() => setCurrentScreen('login')}
          onTermsClick={() => console.log('Terms not implemented')}
          onPrivacyClick={() => console.log('Privacy not implemented')}
          isLoading={auth.loading}
          error={auth.error || undefined}
        />
      )}

      {auth.isAuthenticated && currentScreen === 'chat' && (
        <ChatPage
          currentUserId={auth.user?.id || 'user-1'}
          contactName="Elena"
          contactAvatar=""
          isOnline={true}
          messages={messages}
          onSendMessage={handleSendMessage}
          onBackClick={handleLogout}
          onSettingsClick={handleSettingsClick}
          isConnected={backendConnected}
          showSettingsButton={true}
        />
      )}

      {auth.isAuthenticated && currentScreen === 'settings' && (
        <SettingsPage
          language={language}
          tone={tone}
          onLanguageChange={setLanguage}
          onToneChange={setTone}
          onBackClick={() => setCurrentScreen('chat')}
        />
      )}
    </ThemeProvider>
  );
}

export default App;
