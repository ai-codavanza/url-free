import type { ProductSuggestion } from './domainService';
import { generateBrandIdentity } from './brandVisualsService';
import { config, hasValidApiKey } from '../config';

/**
 * AI-Powered Brand Name Generation Service
 * Supports multiple providers: Gemini, OpenAI, Claude
 */

interface AIBrandSuggestion {
    name: string;
    slogan: string;
    personality: string;
    memorability: number; // 0-10
    archetype: string;
    rationale: string;
}

// ============ GEMINI API ============
const generateWithGemini = async (description: string, style: string): Promise<AIBrandSuggestion[]> => {
    const apiKey = config.ai.geminiKey;

    const prompt = `Eres un experto mundial en branding y psicología del naming. Tu misión es generar exactamente 6 nombres de marca de ALTO NIVEL comercial para el siguiente negocio:

"${description}"

El estilo solicitado es: ${style}

INSTRUCCIONES CRÍTICAS PARA EVITAR NOMBRES GENÉRICOS:
1. NO uses sufijos repetitivos como "ly", "ify", "hub", "flow", "io".
2. Busca originalidad mediante:
   - Acuñación (nombres inventados que suenan premium como 'Lexicon').
   - Metáforas (objetos o conceptos que transmitan la esencia).
   - Nombres compuestos elegantes (sin usar guiones).
   - Simbolismo fonético (que el sonido de la palabra evoque la industria).
3. Cada nombre debe ser fácil de escribir y funcional para un dominio .com.
4. Asegúrate de que los 6 nombres sean RADICALMENTE diferentes entre sí en estructura y raíz.

Para cada nombre, proporciona:
1. El nombre de marca (único, memorable).
2. Un slogan estratégico y minimalista (2-4 palabras).
3. Una palabra que define la personalidad de la marca.
4. Un puntaje de memorabilidad de 0 a 10.
5. El arquetipo de marca (ej: El Mago, El Rebelde, El Sabio).
6. Una breve razón (máximo 12 palabras) de por qué este nombre es una jugada maestra de branding.

IMPORTANTE: Responde SOLO con un JSON array válido:
[
  {"name": "Nombre", "slogan": "...", "personality": "...", "memorability": 9, "archetype": "...", "rationale": "..."},
  ...
]`;

    const response = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: prompt }] }],
                generationConfig: {
                    temperature: 0.9,
                    maxOutputTokens: 1024,
                },
            }),
        }
    );

    if (!response.ok) {
        throw new Error(`Gemini API error: ${response.status}`);
    }

    const data = await response.json();
    const text = data.candidates?.[0]?.content?.parts?.[0]?.text || '';

    // Extract JSON from response
    const jsonMatch = text.match(/\[[\s\S]*\]/);
    if (!jsonMatch) throw new Error('Invalid AI response format');

    return JSON.parse(jsonMatch[0]);
};

// ============ OPENAI API ============
const generateWithOpenAI = async (description: string): Promise<AIBrandSuggestion[]> => {
    const apiKey = config.ai.openaiKey;

    const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`,
        },
        body: JSON.stringify({
            model: 'gpt-4o-mini',
            messages: [
                {
                    role: 'system',
                    content: 'Eres un experto en branding. Responde SOLO con JSON válido, sin markdown ni texto adicional.',
                },
                {
                    role: 'user',
                    content: `Genera 6 nombres de marca para: "${description}". 
Formato JSON: [{"name": "...", "slogan": "...", "personality": "...", "memorability": 8, "archetype": "..."}]`,
                },
            ],
            temperature: 0.9,
            response_format: { type: "json_object" },
        }),
    });

    if (!response.ok) {
        throw new Error(`OpenAI API error: ${response.status}`);
    }

    const data = await response.json();
    const content = data.choices?.[0]?.message?.content || '[]';
    const parsed = JSON.parse(content);

    return parsed.brands || parsed;
};

// ============ CLAUDE API ============
const generateWithClaude = async (description: string): Promise<AIBrandSuggestion[]> => {
    const apiKey = config.ai.claudeKey;

    const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-api-key': apiKey,
            'anthropic-version': '2023-06-01',
            'anthropic-dangerous-direct-browser-access': 'true',
        },
        body: JSON.stringify({
            model: 'claude-3-haiku-20240307',
            max_tokens: 1024,
            messages: [
                {
                    role: 'user',
                    content: `Genera 6 nombres de marca para: "${description}". 
Responde SOLO con JSON: [{"name": "...", "slogan": "...", "personality": "...", "memorability": 9, "archetype": "..."}]`,
                },
            ],
        }),
    });

    if (!response.ok) {
        throw new Error(`Claude API error: ${response.status}`);
    }

    const data = await response.json();
    const text = data.content?.[0]?.text || '';
    const jsonMatch = text.match(/\[[\s\S]*\]/);
    if (!jsonMatch) throw new Error('Invalid AI response format');

    return JSON.parse(jsonMatch[0]);
};

// ============ FALLBACK LOCAL GENERATOR ============
const DICTIONARIES = {
    modern: {
        prefixes: ['Neo', 'Meta', 'Omni', 'Hyper', 'Flux', 'Zync', 'Xo', 'Velo'],
        suffixes: ['node', 'grid', 'pulse', 'layer', 'sync', 'flow', 'bit', 'byte'],
        roots: ['strato', 'nexus', 'prism', 'apex', 'quint', 'vertex', 'zenith']
    },
    classic: {
        prefixes: ['Royal', 'Grand', 'Elite', 'Ivory', 'Prime', 'Noble', 'Vintage', 'Heritage'],
        suffixes: ['stone', 'vault', 'bridge', 'court', 'house', 'crest', 'hall', 'port'],
        roots: ['aurum', 'vitas', 'solis', 'astra', 'terra', 'lux', 'fide']
    },
    abstract: {
        prefixes: ['Aura', 'Kyo', 'Mora', 'Voda', 'Zora', 'Lumi', 'Nexa', 'Oura'],
        suffixes: ['is', 'um', 'ia', 'on', 'as', 'ex', 'os', 'en'],
        roots: ['elix', 'vorn', 'tyro', 'phos', 'koda', 'syra', 'muna']
    },
    minimalist: {
        prefixes: ['Nu', 'Re', 'Un', 'On', 'In', 'Ex', 'Bi', 'Tri'],
        suffixes: ['o', 'a', 'u', 'i', 'x', 'z', 'm', 'n'],
        roots: ['pure', 'base', 'core', 'form', 'line', 'dot', 'void']
    }
};

const BRAND_PERSONALITIES = ['Innovador', 'Elegante', 'Confiable', 'Directo', 'Audaz', 'Místico'];
const BRAND_ARCHETYPES = ['El Creador', 'El Sabio', 'El Mago', 'El Héroe', 'El Explorador', 'El Inocente'];

const generateLocalFallback = (description: string, style: string = 'Moderno'): AIBrandSuggestion[] => {
    const styleKey = style.toLowerCase() as keyof typeof DICTIONARIES;
    const dict = DICTIONARIES[styleKey] || DICTIONARIES.modern;
    const words = description.split(' ').filter(w => w.length > 3).map(w => w.toLowerCase());

    const suggestions: AIBrandSuggestion[] = [];

    for (let i = 0; i < 6; i++) {
        const seed = words[Math.floor(Math.random() * words.length)] || 'brand';
        const cleanSeed = seed.replace(/[^a-z]/g, '');

        let name = '';
        const namingType = i % 4;

        switch (namingType) {
            case 0: // Prefijo + Roots
                name = dict.prefixes[Math.floor(Math.random() * dict.prefixes.length)] + dict.roots[Math.floor(Math.random() * dict.roots.length)];
                break;
            case 1: // Seed + Suffix
                name = cleanSeed.charAt(0).toUpperCase() + cleanSeed.slice(1, 4) + dict.suffixes[Math.floor(Math.random() * dict.suffixes.length)];
                break;
            case 2: // Portmanteau (Prefix + Seed)
                name = dict.prefixes[Math.floor(Math.random() * dict.prefixes.length)] + cleanSeed.charAt(0).toUpperCase() + cleanSeed.slice(1);
                break;
            case 3: // Pure Abstract
                name = dict.roots[Math.floor(Math.random() * dict.roots.length)].charAt(0).toUpperCase() + dict.roots[Math.floor(Math.random() * dict.roots.length)].slice(1) + dict.suffixes[Math.floor(Math.random() * dict.suffixes.length)];
                break;
        }

        suggestions.push({
            name,
            slogan: [
                "Tu visión elevada.",
                "Simplemente excepcional.",
                "El nuevo estándar.",
                "Evolución constante.",
                "Inspirando el mañana.",
                "Donde nace el futuro."
            ][i],
            personality: BRAND_PERSONALITIES[Math.floor(Math.random() * BRAND_PERSONALITIES.length)],
            memorability: 7 + Math.random() * 2,
            archetype: BRAND_ARCHETYPES[Math.floor(Math.random() * BRAND_ARCHETYPES.length)],
            rationale: `Combinación basada en el estilo ${style} y conceptos de "${seed}".`
        });
    }

    return suggestions;
};

// ============ MAIN EXPORT ============
export const generateProductNames = async (description: string, style: string = 'Moderno'): Promise<ProductSuggestion[]> => {
    let aiBrands: AIBrandSuggestion[];

    if (hasValidApiKey()) {
        try {
            switch (config.ai.provider) {
                case 'gemini':
                    aiBrands = await generateWithGemini(description, style);
                    break;
                case 'openai':
                    aiBrands = await generateWithOpenAI(description);
                    break;
                case 'claude':
                    aiBrands = await generateWithClaude(description);
                    break;
                default:
                    aiBrands = generateLocalFallback(description, style);
            }
        } catch (error) {
            console.warn('AI generation failed, using fallback:', error);
            aiBrands = generateLocalFallback(description, style);
        }
    } else {
        aiBrands = generateLocalFallback(description, style);
    }

    // Transform AI suggestions to ProductSuggestion format
    return aiBrands.map((brand) => {
        const identity = generateBrandIdentity(brand.name, description);

        return {
            name: brand.name,
            domain: `${brand.name.toLowerCase().replace(/[^a-z0-9]/g, '')}.com`,
            status: 'idle',
            trademarkStatus: 'idle',
            slogan: brand.slogan,
            sentiment: brand.personality,
            memorability: brand.memorability,
            archetype: brand.archetype,
            rationale: brand.rationale,
            tlds: [
                { suffix: '.io', price: '$35/yr', available: 'checking' as const },
                { suffix: '.ai', price: '$65/yr', available: 'checking' as const },
            ],
            socials: [
                { platform: 'instagram', handle: brand.name.toLowerCase().replace(/[^a-z0-9]/g, ''), available: 'checking' as const },
                { platform: 'twitter', handle: `@${brand.name.toLowerCase().replace(/[^a-z0-9]/g, '')}`, available: 'checking' as const },
                { platform: 'tiktok', handle: brand.name.toLowerCase().replace(/[^a-z0-9]/g, ''), available: 'checking' as const },
                { platform: 'youtube', handle: brand.name.toLowerCase().replace(/[^a-z0-9]/g, ''), available: 'checking' as const },
            ],
            branding: {
                colors: identity.colors,
                font: identity.font,
            },
        };
    });
};
