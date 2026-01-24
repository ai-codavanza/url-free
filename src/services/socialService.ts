import { urlExists } from './corsProxy';
import { config } from '../config';

/**
 * Social Media Handle Verification Service
 * With error tracking and retry functionality
 */

export interface SocialCheckResult {
    platform: 'instagram' | 'twitter' | 'tiktok' | 'youtube';
    handle: string;
    available: boolean | 'error';
    errorMessage?: string;
}

// Platform URL patterns for profile checking
const PLATFORM_URLS: Record<string, (handle: string) => string> = {
    instagram: (handle) => `https://www.instagram.com/${handle}/`,
    twitter: (handle) => `https://x.com/${handle.replace('@', '')}`,
    tiktok: (handle) => `https://www.tiktok.com/@${handle}`,
    youtube: (handle) => `https://www.youtube.com/@${handle}`,
};

// Platform display names for error messages
const PLATFORM_NAMES: Record<string, string> = {
    instagram: 'Instagram',
    twitter: 'Twitter/X',
    tiktok: 'TikTok',
    youtube: 'YouTube',
};

/**
 * Heuristic fallback: estimate availability based on handle characteristics
 */
const heuristicAvailability = (handle: string): boolean => {
    const isLong = handle.length > 10;
    const hasNumbers = /\d/.test(handle);
    const isUnique = !['brand', 'shop', 'official', 'real', 'the'].some(
        (word) => handle.includes(word)
    );

    const availabilityScore =
        (isLong ? 0.4 : 0) + (hasNumbers ? 0.2 : 0) + (isUnique ? 0.3 : 0);

    return Math.random() < availabilityScore + 0.2;
};

/**
 * Check if a social handle is available on a specific platform
 */
const checkPlatformHandle = async (
    platform: string,
    handle: string
): Promise<SocialCheckResult> => {
    const cleanHandle = handle.replace('@', '').toLowerCase();
    const urlBuilder = PLATFORM_URLS[platform];
    const platformName = PLATFORM_NAMES[platform] || platform;

    if (!urlBuilder) {
        return {
            platform: platform as SocialCheckResult['platform'],
            handle: platform === 'twitter' ? `@${cleanHandle}` : cleanHandle,
            available: 'error',
            errorMessage: `Plataforma desconocida: ${platform}`,
        };
    }

    const profileUrl = urlBuilder(cleanHandle);

    try {
        const exists = await urlExists(profileUrl);
        return {
            platform: platform as SocialCheckResult['platform'],
            handle: platform === 'twitter' ? `@${cleanHandle}` : cleanHandle,
            available: !exists,
        };
    } catch (error) {
        const message = error instanceof Error ? error.message : 'Error desconocido';
        return {
            platform: platform as SocialCheckResult['platform'],
            handle: platform === 'twitter' ? `@${cleanHandle}` : cleanHandle,
            available: 'error',
            errorMessage: `Error verificando ${platformName}: ${message}`,
        };
    }
};

/**
 * Simulated check (used when real checks are disabled)
 */
const simulateCheck = async (
    platform: string,
    handle: string
): Promise<SocialCheckResult> => {
    await new Promise((resolve) => setTimeout(resolve, 500 + Math.random() * 1000));
    const cleanHandle = handle.replace('@', '').toLowerCase();
    return {
        platform: platform as SocialCheckResult['platform'],
        handle: platform === 'twitter' ? `@${cleanHandle}` : cleanHandle,
        available: heuristicAvailability(cleanHandle),
    };
};

/**
 * Main export: Check availability across all platforms
 */
export const checkSocialAvailability = async (
    name: string
): Promise<SocialCheckResult[]> => {
    const handle = name.toLowerCase().replace(/[^a-z0-9]/g, '');
    const platforms: SocialCheckResult['platform'][] = [
        'instagram',
        'twitter',
        'tiktok',
        'youtube',
    ];

    if (!config.features.realSocialCheck) {
        await new Promise((resolve) => setTimeout(resolve, 1000));
        return platforms.map((platform) => ({
            platform,
            handle: platform === 'twitter' ? `@${handle}` : handle,
            available: heuristicAvailability(handle),
        }));
    }

    const results = await Promise.all(
        platforms.map(async (platform, index) => {
            await new Promise((resolve) => setTimeout(resolve, index * 300));
            return checkPlatformHandle(platform, handle);
        })
    );

    return results;
};

/**
 * Retry a single social platform check
 */
export const retrySocialCheck = async (
    platform: SocialCheckResult['platform'],
    handle: string
): Promise<SocialCheckResult> => {
    if (!config.features.realSocialCheck) {
        return simulateCheck(platform, handle);
    }
    return checkPlatformHandle(platform, handle);
};
