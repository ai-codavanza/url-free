/**
 * Domain Verification Service
 * With error tracking and retry functionality
 */

export interface TLD {
    suffix: string;
    price: string;
    available: boolean | 'checking' | 'error';
    errorMessage?: string;
}

export interface SocialHandle {
    platform: string;
    handle: string;
    available: boolean | 'checking' | 'error';
    errorMessage?: string;
}

export interface ProductSuggestion {
    name: string;
    domain: string;
    status: 'idle' | 'checking' | 'available' | 'taken' | 'error';
    statusError?: string;
    trademarkStatus: 'idle' | 'checking' | 'available' | 'potential_conflict' | 'error';
    trademarkError?: string;
    slogan?: string;
    sentiment?: string;
    tlds?: TLD[];
    socials?: SocialHandle[];
    memorability?: number; // 0-10
    archetype?: string;
    rationale?: string;
    branding?: {
        colors: string[];
        font: string;
    };
}

export interface DomainCheckResult {
    available: boolean;
    error?: string;
}

/**
 * Check .com domain availability with error handling
 */
export const checkDomainAvailability = async (domain: string): Promise<DomainCheckResult> => {
    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 8000);

        const response = await fetch(
            `https://rdap.verisign.com/com/v1/domain/${domain.toLowerCase()}`,
            { signal: controller.signal }
        );

        clearTimeout(timeoutId);

        if (response.status === 404) {
            return { available: true };
        }
        return { available: false };
    } catch (error) {
        const message = error instanceof Error ? error.message : 'Unknown error';
        console.error('Error checking domain:', message);

        if (message.includes('abort')) {
            return { available: false, error: 'Timeout: verificación tardó demasiado' };
        }
        return { available: false, error: `Error de red: ${message}` };
    }
};

/**
 * Check secondary TLD with error handling
 */
export const checkSecondaryDomain = async (
    _name: string,
    suffix: string
): Promise<DomainCheckResult> => {
    try {
        // Simulate with realistic delay
        await new Promise((resolve) => setTimeout(resolve, 800 + Math.random() * 1000));

        // Simulated: 60% availability for demo
        // In production, integrate with actual registrar APIs
        const available = Math.random() > 0.4;
        return { available };
    } catch (error) {
        const message = error instanceof Error ? error.message : 'Unknown error';
        return { available: false, error: `Error verificando ${suffix}: ${message}` };
    }
};

/**
 * Retry a single domain check
 */
export const retryDomainCheck = async (domain: string): Promise<DomainCheckResult> => {
    return checkDomainAvailability(domain);
};

/**
 * Retry a secondary TLD check
 */
export const retryTLDCheck = async (
    name: string,
    suffix: string
): Promise<DomainCheckResult> => {
    return checkSecondaryDomain(name, suffix);
};
