/**
 * CORS Proxy Utility
 * Handles CORS-restricted requests for social media verification
 */

const CORS_PROXIES = [
    'https://corsproxy.io/?',
    'https://api.allorigins.win/raw?url=',
    'https://proxy.cors.sh/',
];

let currentProxyIndex = 0;

/**
 * Fetch a URL through a CORS proxy
 */
export const fetchWithCORS = async (
    url: string,
    options: { timeout?: number; method?: string } = {}
): Promise<Response> => {
    const { timeout = 5000, method = 'HEAD' } = options;

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);

    let lastError: Error | null = null;

    // Try each proxy until one works
    for (let attempt = 0; attempt < CORS_PROXIES.length; attempt++) {
        const proxyIndex = (currentProxyIndex + attempt) % CORS_PROXIES.length;
        const proxy = CORS_PROXIES[proxyIndex];
        const proxyUrl = `${proxy}${encodeURIComponent(url)}`;

        try {
            const response = await fetch(proxyUrl, {
                method,
                signal: controller.signal,
                headers: {
                    'Accept': 'text/html,application/xhtml+xml',
                },
            });

            clearTimeout(timeoutId);

            // Update preferred proxy on success
            currentProxyIndex = proxyIndex;

            return response;
        } catch (error) {
            lastError = error as Error;
            continue;
        }
    }

    clearTimeout(timeoutId);
    throw lastError || new Error('All CORS proxies failed');
};

/**
 * Check if a URL exists (returns 200-range status)
 */
export const urlExists = async (url: string): Promise<boolean> => {
    try {
        const response = await fetchWithCORS(url, { timeout: 4000 });
        return response.ok;
    } catch {
        // On error, assume taken (conservative approach)
        return true;
    }
};
