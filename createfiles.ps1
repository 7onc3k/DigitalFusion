# Cesta k adresáři src
$srcDir = "src"

# Cesta k adresáři layouts
$layoutsDir = Join-Path $srcDir "layouts"

# Cesta k adresáři pages
$pagesDir = Join-Path $srcDir "pages"

# Vytvoření adresářů, pokud neexistují
if (-not (Test-Path $srcDir)) {
    New-Item -ItemType Directory -Path $srcDir | Out-Null
}

if (-not (Test-Path $layoutsDir)) {
    New-Item -ItemType Directory -Path $layoutsDir | Out-Null
}

if (-not (Test-Path $pagesDir)) {
    New-Item -ItemType Directory -Path $pagesDir | Out-Null
}

# Vytvoření souboru Layout.astro, pokud neexistuje
$layoutFilePath = Join-Path $layoutsDir "Layout.astro"
if (-not (Test-Path $layoutFilePath)) {
    $layoutContent = @"
---
interface Props {
    title: string;
}

const { title } = Astro.props;
---

<!doctype html>
<html lang="cs">
    <head>
        <meta charset="UTF-8" />
        <meta name="description" content="DigitalFusion - Vaše digitální řešení" />
        <meta name="viewport" content="width=device-width" />
        <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
        <meta name="generator" content={Astro.generator} />
        <title>{title}</title>
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="/">Domů</a></li>
                    <li><a href="/o-nas">O nás</a></li>
                    <li><a href="/sluzby">Služby</a></li>
                    <li><a href="/portfolio">Portfolio</a></li>
                    <li><a href="/reference">Reference</a></li>
                    <li><a href="/blog">Blog</a></li>
                    <li><a href="/kontakt">Kontakt</a></li>
                </ul>
            </nav>
        </header>

        <main>
            <slot />
        </main>

        <footer>
            <div>
                <h3>Rychlé odkazy</h3>
                <ul>
                    <li><a href="/">Domů</a></li>
                    <li><a href="/o-nas">O nás</a></li>
                    <li><a href="/sluzby">Služby</a></li>
                    <li><a href="/kontakt">Kontakt</a></li>
                </ul>
            </div>
            <div>
                <h3>Sledujte nás</h3>
                <!-- Zde přidejte ikony sociálních médií -->
            </div>
            <div>
                <h3>Newsletter</h3>
                <!-- Zde přidejte formulář pro přihlášení k odběru novinek -->
            </div>
        </footer>
    </body>
</html>
"@
    Set-Content -Path $layoutFilePath -Value $layoutContent
}

# Vytvoření souboru index.astro, pokud neexistuje
$indexFilePath = Join-Path $pagesDir "index.astro"
if (-not (Test-Path $indexFilePath)) {
    $indexContent = @"
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="DigitalFusion - Vaše digitální řešení">
    <section id="hero">
        <h1>DigitalFusion: Vaše digitální transformace začíná zde</h1>
        <p>Inovativní řešení pro moderní podniky</p>
        <a href="/kontakt" class="cta-button">Kontaktujte nás</a>
    </section>

    <section id="about-preview">
        <h2>O nás</h2>
        <p>Jsme tým expertů na digitální technologie, připraveni posunout vaše podnikání do budoucnosti.</p>
        <a href="/o-nas">Zjistěte více</a>
    </section>

    <section id="services-preview">
        <h2>Naše služby</h2>
        <ul>
            <li>Webový design</li>
            <li>Vývoj aplikací</li>
            <li>Digitální marketing</li>
        </ul>
        <a href="/sluzby">Všechny služby</a>
    </section>

    <section id="portfolio-preview">
        <h2>Naše práce</h2>
        <!-- Zde přidejte náhledy projektů -->
        <a href="/portfolio">Prohlédnout portfolio</a>
    </section>

    <section id="testimonials">
        <h2>Co o nás říkají klienti</h2>
        <!-- Zde přidejte citace klientů -->
    </section>

    <section id="blog-preview">
        <h2>Nejnovější články</h2>
        <!-- Zde přidejte náhledy nejnovějších článků -->
        <a href="/blog">Číst více</a>
    </section>

    <section id="contact-cta">
        <h2>Připraveni začít?</h2>
        <p>Kontaktujte nás a společně vytvoříme vaše digitální řešení.</p>
        <a href="/kontakt" class="cta-button">Začněte projekt</a>
    </section>
</Layout>
"@
    Set-Content -Path $indexFilePath -Value $indexContent
}

# Vytvoření ostatních souborů stránek
$pageFiles = @(
    @{
        Name = "o-nas.astro"
        Content = @"
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="O nás - DigitalFusion">
    <h1>O nás</h1>
    
    <section id="history">
        <h2>Naše historie</h2>
        <p>Krátký příběh o vzniku a vývoji DigitalFusion...</p>
    </section>

    <section id="mission-vision">
        <h2>Mise a vize</h2>
        <p>Naše hodnoty a cíle...</p>
    </section>

    <section id="team">
        <h2>Náš tým</h2>
        <!-- Zde přidejte informace o klíčových členech týmu -->
    </section>

    <section id="careers">
        <h2>Kariéra</h2>
        <p>Informace o možnostech práce v DigitalFusion...</p>
        <a href="/kariera">Volné pozice</a>
    </section>
</Layout>
"@
    }
    @{
        Name = "sluzby.astro"
        Content = @"
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Služby - DigitalFusion">
    <h1>Naše služby</h1>
    
    <section id="web-design">
        <h2>Webový design</h2>
        <p>Profesionální a moderní webové stránky, které zaujmou vaše návštěvníky.</p>
    </section>

    <section id="app-development">
        <h2>Vývoj aplikací</h2>
        <p>Vývoj mobilních a webových aplikací na míru vašim potřebám.</p>
    </section>

    <section id="digital-marketing">
        <h2>Digitální marketing</h2>
        <p>Efektivní marketingové strategie pro zvýšení vaší online viditelnosti.</p>
    </section>
</Layout>
"@
    }
    @{
        Name = "portfolio.astro"
        Content = @"
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Portfolio - DigitalFusion">
    <h1>Naše práce</h1>
    
    <section id="project-1">
        <h2>Projekt 1</h2>
        <p>Popis projektu 1...</p>
    </section>

    <section id="project-2">
        <h2>Projekt 2</h2>
        <p>Popis projektu 2...</p>
    </section>

    <section id="project-3">
        <h2>Projekt 3</h2>
        <p>Popis projektu 3...</p>
    </section>
</Layout>
"@
    }
    @{
        Name = "reference.astro"
        Content = @"
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Reference - DigitalFusion">
    <h1>Co o nás říkají klienti</h1>
    
    <section id="testimonial-1">
        <h2>Klient 1</h2>
        <p>"Skvělá spolupráce a vynikající výsledky!"</p>
    </section>

    <section id="testimonial-2">
        <h2>Klient 2</h2>
        <p>"Profesionální přístup a kvalitní práce."</p>
    </section>

    <section id="testimonial-3">
        <h2>Klient 3</h2>
        <p>"Doporučuji všem, kdo hledají spolehlivého partnera."</p>
    </section>
</Layout>
"@
    }
    @{
        Name = "blog.astro"
        Content = @"
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Blog - DigitalFusion">
    <h1>Nejnovější články</h1>
    
    <section id="article-1">
        <h2>Článek 1</h2>
        <p>Úvod do článku 1...</p>
        <a href="/blog/clanek-1">Číst více</a>
    </section>

    <section id="article-2">
        <h2>Článek 2</h2>
        <p>Úvod do článku 2...</p>
        <a href="/blog/clanek-2">Číst více</a>
    </section>

    <section id="article-3">
        <h2>Článek 3</h2>
        <p>Úvod do článku 3...</p>
        <a href="/blog/clanek-3">Číst více</a>
    </section>
</Layout>
"@
    }
    @{
        Name = "kontakt.astro"
        Content = @"
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Kontakt - DigitalFusion">
    <h1>Kontaktujte nás</h1>
    
    <section id="contact-form">
        <h2>Kontaktní formulář</h2>
        <form action="/odeslat" method="post">
            <label for="name">Jméno:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="message">Zpráva:</label>
            <textarea id="message" name="message" required></textarea>
            
            <button type="submit">Odeslat</button>
        </form>
    </section>

    <section id="contact-info">
        <h2>Kontaktní údaje</h2>
        <p>Telefon: +420 123 456 789</p>
        <p>Email: info@digitalfusion.cz</p>
        <p>Adresa: Ulice 123, Město, PSČ</p>
    </section>

    <section id="map">
        <h2>Kde nás najdete</h2>
        <!-- Zde přidejte interaktivní mapu -->
    </section>
</Layout>
"@
    }
)

foreach ($page in $pageFiles) {
    $pageFilePath = Join-Path $pagesDir $page.Name
    if (-not (Test-Path $pageFilePath)) {
        Set-Content -Path $pageFilePath -Value $page.Content
    }
}

Write-Host "Soubory byly úspěšně vytvořeny."