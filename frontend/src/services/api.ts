/**
 * API Service - Centralized communication with MultiChat backend
 */

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';

interface ApiResponse<T = unknown> {
  data?: T;
  status: number;
  error?: string;
}

/**
 * Translation API
 */
export const translationAPI = {
  async translate(
    text: string,
    targetLanguage: string,
    tone: string
  ): Promise<{ translated_text: string }> {
    const response = await fetch(`${API_URL}/translate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text,
        target_language: targetLanguage.toUpperCase(),
        tone: tone.toUpperCase(),
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Translation failed');
    }

    return response.json();
  },
};

/**
 * Authentication API
 */
export const authAPI = {
  async login(email: string, password: string): Promise<{ access_token: string; token_type: string }> {
    const response = await fetch(`${API_URL}/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Login failed');
    }

    return response.json();
  },

  async signup(
    email: string,
    password: string,
    fullName: string,
    preferredLanguage: string
  ): Promise<{ access_token: string; token_type: string; user: { id: string; email: string } }> {
    const response = await fetch(`${API_URL}/auth/signup`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email,
        password,
        full_name: fullName,
        preferred_language: preferredLanguage.toUpperCase(),
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Signup failed');
    }

    return response.json();
  },

  async refreshToken(token: string): Promise<{ access_token: string }> {
    const response = await fetch(`${API_URL}/auth/refresh`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error('Token refresh failed');
    }

    return response.json();
  },

  async getCurrentUser(token: string): Promise<{
    id: string;
    email: string;
    full_name: string;
    preferred_language: string;
    preferred_tone: string;
  }> {
    const response = await fetch(`${API_URL}/auth/me`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch current user');
    }

    return response.json();
  },
};

/**
 * Conversations API
 */
export const conversationsAPI = {
  async list(token: string): Promise<Array<{ id: string; name: string; is_group: boolean }>> {
    const response = await fetch(`${API_URL}/conversations`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch conversations');
    }

    return response.json();
  },

  async create(
    token: string,
    name: string,
    isGroup: boolean,
    participantIds?: string[]
  ): Promise<{ id: string; name: string }> {
    const response = await fetch(`${API_URL}/conversations`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        name,
        is_group: isGroup,
        participant_ids: participantIds,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to create conversation');
    }

    return response.json();
  },
};

/**
 * Messages API
 */
export const messagesAPI = {
  async listByConversation(
    token: string,
    conversationId: string
  ): Promise<
    Array<{
      id: string;
      content: string;
      original_language: string;
      translated_content?: string;
      target_language?: string;
      tone: string;
    }>
  > {
    const response = await fetch(
      `${API_URL}/conversations/${conversationId}/messages`,
      {
        method: 'GET',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    if (!response.ok) {
      throw new Error('Failed to fetch messages');
    }

    return response.json();
  },

  async send(
    token: string,
    conversationId: string,
    content: string,
    originalLanguage: string,
    tone: string,
    targetLanguage?: string
  ): Promise<{ id: string; status: string }> {
    const response = await fetch(
      `${API_URL}/conversations/${conversationId}/messages`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          content,
          original_language: originalLanguage.toUpperCase(),
          tone: tone.toUpperCase(),
          target_language: targetLanguage?.toUpperCase(),
        }),
      }
    );

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to send message');
    }

    return response.json();
  },
};

/**
 * Health Check
 */
export const healthAPI = {
  async check(): Promise<{ status: string; message: string }> {
    const response = await fetch(`${API_URL}/health`, {
      method: 'GET',
    });

    if (!response.ok) {
      throw new Error('Backend is not available');
    }

    return response.json();
  },
};
