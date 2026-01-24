/**
 * Application Configuration
 * Centralized config for API keys and feature toggles
 */

export type AIProvider = 'gemini' | 'openai' | 'claude';

interface Config {
  ai: {
    provider: AIProvider;
    geminiKey: string;
    openaiKey: string;
    claudeKey: string;
  };
  features: {
    realSocialCheck: boolean;
  };
}

export const config: Config = {
  ai: {
    provider: (import.meta.env.VITE_AI_PROVIDER as AIProvider) || 'gemini',
    geminiKey: import.meta.env.VITE_GEMINI_API_KEY || '',
    openaiKey: import.meta.env.VITE_OPENAI_API_KEY || '',
    claudeKey: import.meta.env.VITE_CLAUDE_API_KEY || '',
  },
  features: {
    realSocialCheck: import.meta.env.VITE_REAL_SOCIAL_CHECK === 'true',
  },
};

export const getActiveApiKey = (): string => {
  switch (config.ai.provider) {
    case 'gemini':
      return config.ai.geminiKey;
    case 'openai':
      return config.ai.openaiKey;
    case 'claude':
      return config.ai.claudeKey;
    default:
      return '';
  }
};

export const hasValidApiKey = (): boolean => {
  const key = getActiveApiKey();
  return key.length > 10 && !key.includes('your-');
};
