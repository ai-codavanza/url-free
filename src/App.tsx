import React, { useState, useEffect } from 'react';
import {
  Sparkles, Loader2, Heart, Download, Sun, Moon,
  RefreshCw, Trash2, Search, Instagram, Youtube, Video, Twitter,
  Brain, Star, Copy, Check, Zap
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import { generateProductNames } from './services/aiService';
import { checkDomainAvailability, checkSecondaryDomain, retryDomainCheck } from './services/domainService';
import { checkTrademarkAvailability } from './services/trademarkService';
import { checkSocialAvailability } from './services/socialService';
import type { ProductSuggestion } from './services/domainService';

function App() {
  const { t, i18n } = useTranslation();
  const [description, setDescription] = useState('');
  const [namingStyle, setNamingStyle] = useState('Moderno');
  const [isGenerating, setIsGenerating] = useState(false);
  const [suggestions, setSuggestions] = useState<ProductSuggestion[]>([]);
  const [favorites, setFavorites] = useState<ProductSuggestion[]>(() => {
    const saved = localStorage.getItem('url-free-favorites');
    return saved ? JSON.parse(saved) : [];
  });
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [scanProgress, setScanProgress] = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(() => {
    return localStorage.getItem('theme') === 'dark';
  });

  // Theme Sync
  useEffect(() => {
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }, [isDarkMode]);

  // Favorites Sync
  useEffect(() => {
    localStorage.setItem('url-free-favorites', JSON.stringify(favorites));
  }, [favorites]);

  // Overall progress logic
  useEffect(() => {
    if (suggestions.length === 0) {
      setScanProgress(0);
      return;
    }

    const totalChecks = suggestions.length * 4;
    const completedChecks = suggestions.reduce((acc: number, s: ProductSuggestion) => {
      const domainDone = s.status !== 'idle' && s.status !== 'checking';
      const tmDone = s.trademarkStatus !== 'idle' && s.trademarkStatus !== 'checking';
      const tldsDone = s.tlds?.every(t => t.available !== 'checking') ? 1 : 0;
      const socialsDone = s.socials?.every(so => (so.available as any) !== 'checking') ? 1 : 0;
      return acc + (domainDone ? 1 : 0) + (tmDone ? 1 : 0) + tldsDone + socialsDone;
    }, 0);

    setScanProgress((completedChecks / totalChecks) * 100);
  }, [suggestions]);

  const handleGenerate = async (e?: React.FormEvent, isMore = false) => {
    e?.preventDefault();
    if (!description.trim() || isGenerating) return;

    setIsGenerating(true);
    setError(null);
    const startIndex = isMore ? suggestions.length : 0;

    if (!isMore) {
      setSuggestions([]);
      setScanProgress(0);
    }

    try {
      const names = await generateProductNames(description, namingStyle);

      if (isMore) {
        setSuggestions(prev => [...prev, ...names]);
      } else {
        setSuggestions(names);
      }

      await Promise.all(names.map(async (item: ProductSuggestion, i: number) => {
        const globalIndex = startIndex + i;

        setSuggestions(prev => prev.map((s: ProductSuggestion, idx: number) =>
          idx === globalIndex ? { ...s, status: 'checking', trademarkStatus: 'checking' } : s
        ));

        const domainP = checkDomainAvailability(item.domain).then(result => {
          setSuggestions(prev => prev.map((s: ProductSuggestion, idx: number) =>
            idx === globalIndex ? {
              ...s,
              status: result.error ? 'error' : (result.available ? 'available' : 'taken'),
              statusError: result.error
            } : s
          ));
        });

        const tldsP = Promise.all((item.tlds || []).map(async t => {
          const result = await checkSecondaryDomain(item.name, t.suffix);
          setSuggestions(prev => prev.map((s: ProductSuggestion, idx: number) =>
            idx === globalIndex ? {
              ...s,
              tlds: s.tlds?.map(st => st.suffix === t.suffix ? {
                ...st,
                available: result.error ? 'error' : result.available,
                errorMessage: result.error
              } : st)
            } : s
          ));
        }));

        const socialsP = checkSocialAvailability(item.name).then(results => {
          setSuggestions(prev => prev.map((s: ProductSuggestion, idx: number) =>
            idx === globalIndex ? {
              ...s,
              socials: results.map(r => ({
                platform: r.platform,
                handle: r.handle,
                available: r.available,
                errorMessage: r.errorMessage
              }))
            } : s
          ));
        });

        const tmP = checkTrademarkAvailability(item.name).then(result => {
          setSuggestions(prev => prev.map((s: ProductSuggestion, idx: number) =>
            idx === globalIndex ? { ...s, trademarkStatus: result } : s
          ));
        });

        return Promise.all([domainP, tldsP, socialsP, tmP]);
      }));
    } catch (err) {
      setError(t('main.errorGeneration'));
    } finally {
      setIsGenerating(false);
    }
  };

  const handleCopy = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(text);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const toggleFavorite = (item: ProductSuggestion) => {
    if (favorites.some((f: ProductSuggestion) => f.name === item.name)) {
      setFavorites(favorites.filter((f: ProductSuggestion) => f.name !== item.name));
    } else {
      setFavorites([...favorites, item]);
    }
  };

  const handleRetryDomain = async (suggestionName: string, domain: string) => {
    setSuggestions(prev => prev.map(s =>
      s.name === suggestionName ? { ...s, status: 'checking', statusError: undefined } : s
    ));
    const result = await retryDomainCheck(domain);
    setSuggestions(prev => prev.map(s =>
      s.name === suggestionName ? {
        ...s,
        status: result.error ? 'error' : (result.available ? 'available' : 'taken'),
        statusError: result.error
      } : s
    ));
  };

  const exportToCSV = () => {
    const headers = ['Nombre,Slogan,Dominio,Trademark,Socials'];
    const data = suggestions.length > 0 ? suggestions : favorites;
    const rows = data.map((s: ProductSuggestion) => {
      const socialStr = s.socials?.map(so => `${so.platform}: ${so.available ? 'OK' : 'X'}`).join('|');
      return `${s.name},${s.slogan},${s.domain},${s.trademarkStatus},${socialStr}`;
    });
    const content = [headers, ...rows].join('\n');
    const blob = new Blob([content], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'nombres_ai.csv';
    a.click();
  };

  const filteredSuggestions = suggestions.filter((s: ProductSuggestion) => {
    return s.status === 'available' || s.status === 'checking' || s.status === 'error';
  });

  const getArchetypeClass = (arch: string) => {
    if (arch.includes('Héroe')) return 'arch-hero';
    if (arch.includes('Mago')) return 'arch-magician';
    if (arch.includes('Sabio')) return 'arch-sage';
    if (arch.includes('Creador')) return 'arch-creator';
    if (arch.includes('Explorador')) return 'arch-explorer';
    if (arch.includes('Gobernante')) return 'arch-ruler';
    return 'bg-slate-100 dark:bg-slate-800 text-slate-500';
  };

  return (
    <div className="flex min-h-screen">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="logo-container">
          <img
            src={isDarkMode ? "/logo-dark.png" : "/logo-light.png"}
            alt="URL FREE AI Logo"
            className="logo-img"
          />
        </div>

        <div className="flex flex-col">
          <div className="mb-6 text-center">
            <h3 className="text-xl font-bold dark:text-white">{t('sidebar.title')}</h3>
            <p className="text-sm text-slate-400 leading-relaxed">{t('sidebar.subtitle')}</p>
          </div>

          <form onSubmit={handleGenerate} className="flex flex-col gap-6">
            <div className="flex flex-col gap-3">
              <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">{t('sidebar.languageLabel')}</span>
              <div className="grid grid-cols-3 gap-2">
                {[
                  { code: 'es', label: 'ESP' },
                  { code: 'en', label: 'ENG' },
                  { code: 'nl', label: 'NED' }
                ].map(lang => (
                  <button
                    key={lang.code}
                    type="button"
                    onClick={() => i18n.changeLanguage(lang.code)}
                    className={`px-2 py-2 rounded-xl text-[10px] font-bold border transition-all ${i18n.language.startsWith(lang.code) ? 'bg-blue-600 border-blue-600 text-white' : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-500 hover:border-blue-400'}`}
                  >
                    {lang.label}
                  </button>
                ))}
              </div>
            </div>

            <div className="flex flex-col gap-3">
              <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">{t('sidebar.descriptionLabel')}</span>
              <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder={t('sidebar.descriptionPlaceholder')}
                className="premium-input"
                style={{ minHeight: '140px', resize: 'none' }}
              />
            </div>

            <div className="flex flex-col gap-3">
              <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">{t('sidebar.styleLabel')}</span>
              <div className="grid grid-cols-2 gap-2">
                {['Moderno', 'Clásico', 'Abstracto', 'Minimalista'].map(style => (
                  <button
                    key={style}
                    type="button"
                    onClick={() => setNamingStyle(style)}
                    className={`px-3 py-2 rounded-xl text-[11px] font-bold border transition-all ${namingStyle === style ? 'bg-blue-600 border-blue-600 text-white' : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-500 hover:border-blue-400'}`}
                  >
                    {t(`sidebar.styles.${style}`)}
                  </button>
                ))}
              </div>
            </div>

            <div className="flex flex-col mt-2">
              <button
                type="submit"
                disabled={isGenerating || (suggestions.length > 0 && scanProgress < 100)}
                className="button-primary w-full"
              >
                {isGenerating ? <Loader2 className="animate-spin" size={20} /> : <Sparkles size={20} />}
                <span>{isGenerating ? t('sidebar.generating') : t('sidebar.generateBtn')}</span>
              </button>

              <div className="mt-4">
                <button
                  type="button"
                  onClick={() => { setSuggestions([]); setDescription(''); setScanProgress(0); }}
                  className="button-secondary w-full"
                >
                  <Trash2 size={16} />
                  <span>{t('sidebar.clearBtn')}</span>
                </button>
              </div>
            </div>
          </form>
        </div>

        {/* User Footer */}
        <div className="mt-auto pt-8 border-t border-slate-100 dark:border-slate-800 flex items-center justify-center">
          <button onClick={() => setIsDarkMode(!isDarkMode)} className="flex items-center gap-2 p-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-500 transition-colors w-full justify-center">
            {isDarkMode ? <Sun size={20} /> : <Moon size={20} />}
            <span className="text-sm font-bold uppercase tracking-widest">{isDarkMode ? t('sidebar.lightMode') : t('sidebar.darkMode')}</span>
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="main-content">
        <div className="flex items-center justify-between mb-8">
          <div className="flex items-center gap-6">
            <h2 className="text-4xl font-bold font-sora dark:text-white">{t('main.title')}</h2>
            {suggestions.length > 0 && (
              <span className="px-4 py-1.5 rounded-full bg-blue-50 dark:bg-blue-900/40 text-blue-600 dark:text-blue-400 text-xs font-bold">
                {suggestions.length} {t('main.resultsSuffix')}
              </span>
            )}
          </div>

          <div className="flex items-center gap-6">
            <button onClick={exportToCSV} className="button-secondary !py-3 !px-8">
              <Download size={18} /> <span className="font-bold">{t('main.exportCsv')}</span>
            </button>
          </div>
        </div>

        {scanProgress > 0 && scanProgress < 100 && (
          <div className="mb-8 p-4 bg-blue-50/50 dark:bg-blue-950/20 rounded-2xl border border-blue-100 dark:border-blue-900 flex items-center gap-4">
            <Loader2 className="animate-spin text-blue-600" size={20} />
            <div className="flex-1">
              <div className="flex justify-between mb-1">
                <span className="text-xs font-bold text-blue-600 uppercase tracking-widest">{t('main.scanning')}</span>
                <span className="text-xs font-bold text-blue-600">{Math.round(scanProgress)}%</span>
              </div>
              <div className="h-1.5 w-full bg-blue-100 dark:bg-blue-900/50 rounded-full overflow-hidden">
                <motion.div className="h-full bg-blue-600" animate={{ width: `${scanProgress}%` }} />
              </div>
            </div>
          </div>
        )}

        {error && <div className="p-4 bg-red-50 dark:bg-red-950/20 text-red-500 rounded-xl mb-8 border border-red-100 dark:border-red-900 text-sm">{error}</div>}

        {suggestions.length === 0 && !isGenerating && (
          <div className="flex flex-col items-center justify-center h-[50vh] opacity-20 text-slate-400">
            <Search size={80} strokeWidth={1} />
            <p className="mt-4 font-bold uppercase tracking-[.2em] text-[10px] text-center">{t('main.emptyState')}</p>
          </div>
        )}

        <div className="results-grid">
          <AnimatePresence mode="popLayout">
            {filteredSuggestions.map((item, index) => (
              <motion.div
                key={item.name}
                layout
                initial={{ opacity: 0, scale: 0.95, y: 10 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                exit={{ opacity: 0, scale: 0.95 }}
                transition={{ delay: index * 0.08, duration: 0.4 }}
                className="glass-card p-5 flex flex-col gap-2 group relative overflow-visible"
              >
                <div className="flex justify-between items-start mb-0">
                  <div className={`badge ${item.status === 'available' ? 'badge-available' :
                    item.status === 'error' ? 'badge-taken' : 'badge-taken'
                    }`}>
                    {item.status === 'checking' ? <Loader2 size={10} className="animate-spin" /> :
                      item.status === 'available' ? t('card.available') : t('card.taken')}
                  </div>
                  <div className="flex gap-2">
                    <button onClick={() => handleCopy(item.name)} className="p-2 rounded-lg text-slate-300 hover:text-blue-500 hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-all">
                      {copiedId === item.name ? <Check size={16} /> : <Copy size={16} />}
                    </button>
                    <button onClick={() => toggleFavorite(item)} className={`p-2 rounded-lg transition-colors ${favorites.some(f => f.name === item.name) ? 'bg-red-50 text-red-500' : 'text-slate-300 hover:text-slate-400'}`}>
                      <Heart size={16} fill={favorites.some(f => f.name === item.name) ? "currentColor" : "none"} />
                    </button>
                  </div>
                </div>

                <div className="mb-2 relative group/title">
                  <h3 className="brand-name font-bold dark:text-white mb-0 flex items-center gap-2">
                    {item.name}
                    {item.rationale && (
                      <div className="opacity-0 group-hover/title:opacity-100 rationale-tooltip animate-slide-up pointer-events-none">
                        <p className="font-normal text-slate-500 italic">"{item.rationale}"</p>
                      </div>
                    )}
                  </h3>
                  <p className="brand-handle text-xs font-mono text-slate-400">{item.domain}</p>
                </div>

                <div className="mt-auto">
                  <div className="flex items-center justify-end pt-2 border-t border-slate-50 dark:border-slate-800">
                    {item.status === 'available' && (
                      <a href={`https://www.vimexx.nl/`} target="_blank" className="button-primary !py-2 !px-4 !text-[11px]">
                        {t('card.buyBtn')}
                      </a>
                    )}
                    {item.status === 'error' && (
                      <button onClick={() => handleRetryDomain(item.name, item.domain)} className="button-secondary !py-2 !px-4 !text-[11px] flex gap-2">
                        <RefreshCw size={12} /> {t('card.retryBtn')}
                      </button>
                    )}
                  </div>
                </div>

                {/* Enriched Details */}
                <div className="flex flex-col gap-2 mt-2 bg-slate-50/50 dark:bg-slate-900/40 p-2 rounded-xl border border-slate-100 dark:border-slate-800">
                  <div className="flex justify-between items-center">
                    <div className="flex items-center gap-1.5 text-[9px] font-bold text-slate-500 uppercase tracking-tight">
                      <Brain size={10} className="text-blue-500" /> {t('card.memorability')}
                    </div>
                    <div className="flex gap-0.5">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} size={8} fill={i < Math.round((item.memorability || 0) / 2) ? "currentColor" : "none"} className={i < Math.round((item.memorability || 0) / 2) ? "text-amber-400" : "text-slate-200"} />
                      ))}
                    </div>
                  </div>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-1.5 text-[9px] font-bold text-slate-500 uppercase tracking-tight">
                      <Zap size={10} className="text-blue-500" /> {t('card.archetype')}
                    </div>
                    <span className={`px-2 py-0.5 rounded-full text-[8px] font-black uppercase ${getArchetypeClass(item.archetype || '')}`}>
                      {item.archetype ? (t(`archetypes.${item.archetype.replace('El ', '')}`) || item.archetype) : 'N/A'}
                    </span>
                  </div>
                </div>

                <div className="flex gap-4 mt-1 border-t border-slate-50 dark:border-slate-800 pt-2 pb-1 overflow-x-auto no-scrollbar">
                  {item.socials?.map((social) => (
                    <div key={social.platform} className="flex items-center gap-1 group/social shrink-0">
                      <div className={`p-2 rounded-xl transition-all duration-300 ${social.available === true
                        ? 'text-white bg-blue-600 shadow-[0_0_20px_rgba(37,99,235,0.6)] scale-110'
                        : 'text-slate-300 opacity-20 grayscale scale-75'}`}>
                        {social.platform === 'instagram' && <Instagram size={20} />}
                        {social.platform === 'youtube' && <Youtube size={20} />}
                        {social.platform === 'tiktok' && <Video size={20} />}
                        {social.platform === 'twitter' && <Twitter size={20} />}
                      </div>
                    </div>
                  ))}
                  <div className="ml-auto flex -space-x-1">
                    {item.branding?.colors.map(c => <div key={c} className="w-3.5 h-3.5 rounded-full border border-white dark:border-slate-800" style={{ background: c }} />)}
                  </div>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>

        {suggestions.length > 0 && (
          <div className="mt-12 flex justify-center pb-20">
            <button
              onClick={(e) => handleGenerate(e, true)}
              disabled={isGenerating}
              className="button-secondary flex items-center gap-3 !px-12 !py-4"
            >
              {isGenerating ? (
                <>
                  <Loader2 className="animate-spin" size={20} />
                  <span>{t('main.loadingMore')}</span>
                </>
              ) : (
                <>
                  <Sparkles size={20} />
                  <span>{t('main.loadMore')}</span>
                </>
              )}
            </button>
          </div>
        )}

        {/* Favorites Section */}
        {favorites.length > 0 && suggestions.length === 0 && (
          <div className="mt-20 px-4">
            <div className="flex items-center gap-4 mb-8">
              <Heart className="text-red-500" fill="currentColor" size={24} />
              <h3 className="text-2xl font-bold font-sora dark:text-white">{t('main.favorites')}</h3>
            </div>
            <div className="results-grid">
              {favorites.map((item) => (
                <div key={item.name} className="glass-card p-5 flex flex-col gap-2">
                  <div className="flex justify-between items-start">
                    <h4 className="brand-name font-bold dark:text-white mb-0">{item.name}</h4>
                    <button onClick={() => toggleFavorite(item)} className="text-red-500 p-2"><Heart size={20} fill="currentColor" /></button>
                  </div>
                  <p className="text-xs text-slate-400 font-mono mb-2">{item.domain}</p>
                  <div className="mt-auto pt-4 border-t border-slate-100 dark:border-slate-800 flex justify-between items-center">
                    <a href={`https://www.vimexx.nl/`} target="_blank" className="button-primary !py-2 !px-4">Vimexx</a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
