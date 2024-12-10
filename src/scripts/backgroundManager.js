// Function to save background settings to localStorage
function saveBackgroundSettings(options) {
    localStorage.setItem('backgroundSettings', JSON.stringify(options));
}

// Function to load background settings from localStorage
function loadBackgroundSettings() {
    const savedSettings = localStorage.getItem('backgroundSettings');
    return savedSettings ? JSON.parse(savedSettings) : null;
}

// Function to apply background settings
function applyBackgroundSettings() {
    const savedSettings = loadBackgroundSettings();
    if (savedSettings) {
        const tsParticles = window.tsParticles;
        if (tsParticles) {
            const container = tsParticles.domItem(0);
            if (container) {
                container.options = { ...container.options, ...savedSettings };
                container.refresh();
            }
        }
    }
}

// Zachování stavu částic mezi přechodem stránek
function preserveParticlesState() {
    const tsParticles = window.tsParticles;
    if (tsParticles) {
        const container = tsParticles.domItem(0);
        if (container) {
            // Uložení aktuálního stavu částic
            sessionStorage.setItem('particlesState', JSON.stringify({
                options: container.options,
                particleCount: container.particles.count
            }));
        }
    }
}

// Obnovení stavu částic
function restoreParticlesState() {
    const savedState = sessionStorage.getItem('particlesState');
    if (savedState) {
        const { options, particleCount } = JSON.parse(savedState);
        const tsParticles = window.tsParticles;
        
        if (tsParticles) {
            const container = tsParticles.domItem(0);
            if (container) {
                // Obnovení uložených možností
                container.options = { ...container.options, ...options };
                container.refresh();
            }
        }
    }
}

// Initialize background settings
document.addEventListener('DOMContentLoaded', () => {
    applyBackgroundSettings();
    
    // Save settings whenever they change
    const tsParticles = window.tsParticles;
    if (tsParticles) {
        const container = tsParticles.domItem(0);
        if (container) {
            saveBackgroundSettings(container.options);
        }
    }
});

// Přidání event listenerů pro zachování stavu
document.addEventListener('astro:before-swap', preserveParticlesState);
document.addEventListener('astro:page-load', restoreParticlesState);
