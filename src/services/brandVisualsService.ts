export interface BrandIdentity {
    colors: string[];
    font: string;
}

const COLOR_PALETTES = [
    ['#1e293b', '#6366f1', '#a5b4fc'], // Indigo Tech
    ['#064e3b', '#10b981', '#6ee7b7'], // Green Eco
    ['#450a0a', '#ef4444', '#f87171'], // Red Bold
    ['#312e81', '#818cf8', '#c7d2fe'], // Blue Modern
    ['#3f2c06', '#f59e0b', '#fbbf24'], // Gold Premium
    ['#1e1b4b', '#4f46e5', '#818cf8'], // Violet Deep
    ['#0f172a', '#334155', '#94a3b8'], // Slate Mono
];

const FONTS = ['Inter', 'Outfit', 'Plus Jakarta Sans', 'Sora', 'Playfair Display'];

export const generateBrandIdentity = (name: string, description: string): BrandIdentity => {
    // Deterministic "random" based on name to keep it consistent for the same result
    const seed = name.length + description.length;

    return {
        colors: COLOR_PALETTES[seed % COLOR_PALETTES.length],
        font: FONTS[seed % FONTS.length],
    };
};
