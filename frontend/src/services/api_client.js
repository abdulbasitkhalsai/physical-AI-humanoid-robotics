// api_client.js - API Client for Physical AI & Humanoid Robotics Textbook
// Provides a centralized interface for all frontend-backend communication

class ApiClient {
  constructor(baseURL = process.env.REACT_APP_API_BASE_URL || '/api') {
    this.baseURL = baseURL;
    this.defaultHeaders = {
      'Content-Type': 'application/json',
    };
  }

  // Helper method to get auth token from localStorage
  getAuthToken() {
    const token = localStorage.getItem('auth_token');
    return token ? `Bearer ${token}` : null;
  }

  // Helper method to include auth token in headers
  getAuthHeaders() {
    const headers = { ...this.defaultHeaders };
    const token = this.getAuthToken();
    if (token) {
      headers['Authorization'] = token;
    }
    return headers;
  }

  // Generic request method
  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      headers: { ...this.defaultHeaders, ...options.headers },
      ...options,
    };

    // Include auth token if not already provided
    if (!config.headers['Authorization']) {
      const token = this.getAuthToken();
      if (token) {
        config.headers['Authorization'] = token;
      }
    }

    try {
      const response = await fetch(url, config);

      // Handle different response status codes
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }

      // For 204 No Content responses, return null
      if (response.status === 204) {
        return null;
      }

      return await response.json();
    } catch (error) {
      console.error(`API request error for ${url}:`, error);
      throw error;
    }
  }

  // Authentication methods
  async login(email, password) {
    return this.request('/auth/login', {
      method: 'POST',
      headers: this.defaultHeaders,
      body: JSON.stringify({ email, password }),
    });
  }

  async register(name, email, password) {
    return this.request('/auth/register', {
      method: 'POST',
      headers: this.defaultHeaders,
      body: JSON.stringify({ name, email, password }),
    });
  }

  async logout() {
    // Remove auth token from localStorage
    localStorage.removeItem('auth_token');
  }

  async getProfile() {
    return this.request('/auth/profile', {
      method: 'GET',
      headers: this.getAuthHeaders(),
    });
  }

  // Textbook content methods
  async getChapters() {
    return this.request('/chapters', {
      method: 'GET',
      headers: this.defaultHeaders,
    });
  }

  async getChapter(slug) {
    return this.request(`/chapters/${slug}`, {
      method: 'GET',
      headers: this.defaultHeaders,
    });
  }

  // User progress methods
  async getUserProgress() {
    return this.request('/users/progress', {
      method: 'GET',
      headers: this.getAuthHeaders(),
    });
  }

  async updateChapterProgress(chapterId, progressData) {
    return this.request(`/users/progress/${chapterId}`, {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(progressData),
    });
  }

  // Personalization methods
  async getUserProficiency() {
    return this.request('/users/proficiency', {
      method: 'GET',
      headers: this.getAuthHeaders(),
    });
  }

  async updateUserProficiency(proficiencyData) {
    return this.request('/users/proficiency', {
      method: 'PUT',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(proficiencyData),
    });
  }

  // Chatbot methods
  async sendMessage(message, sessionId = null) {
    const body = { message };
    if (sessionId) {
      body.session_id = sessionId;
    }

    return this.request('/chatbot/chat', {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(body),
    });
  }

  async getChatHistory(sessionId) {
    return this.request(`/chatbot/history/${sessionId}`, {
      method: 'GET',
      headers: this.getAuthHeaders(),
    });
  }

  // Translation methods
  async translateContent(content, targetLanguage = 'ur') {
    return this.request('/translate', {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify({
        content,
        target_language: targetLanguage,
      }),
    });
  }

  // Health check
  async healthCheck() {
    return this.request('/health', {
      method: 'GET',
      headers: this.defaultHeaders,
    });
  }
}

// Create a singleton instance
const apiClient = new ApiClient();

export default apiClient;