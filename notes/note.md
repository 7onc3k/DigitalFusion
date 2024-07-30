
Potřebuji udělat tuto animaci s textem v Astru:1. Máme tabulku 2x7 kde bude probíhat aniamce2. Zobrazí se písmena D a F uprostřed tabulky, zarovnané horizontálně i vertikálně, ale vedle sebe, ne přes sebe.3. D se posune nahoru na 1. řádek a F se posune dolů na 2. řádek., všechno cestuje v rovné ose4. D se posune na pozici 1,1 a F na pozici 2,2.5. V ostatních buňkách budou připravena ostatní písmena: * i, g, i, t, a, l v prvním řádku, * u, s, i, o, n na druhém řádku (začínáme od 2,3).Zbylá písmena na prvním řádku se "napíší" postupně po sobě až bude D na pozici 1,1 a zbylá písmena na druhém řádku se napíší až budou dopsána písmena na prvním řádku. Všechny posuny jsou plynulé, tabulka se nezobrazuje, je pouze orientační.Máš nějaké nejasnosti? Pokud ne, pusť se do generování kódu v Astro.


musí to udělat iterativně krok po kroku

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\package.json
==================================================
{
  "name": "",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro check && astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/check": "^0.8.2",
    "@iconify-json/mdi": "^1.1.67",
    "astro": "^4.12.1",
    "astro-icon": "^1.1.0",
    "typescript": "^5.5.3"
  },
  "devDependencies": {
    "@astrojs/tailwind": "^5.1.0",
    "tailwindcss": "^3.4.6"
  }
}


==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\tsconfig.json
==================================================
{
  "extends": "astro/tsconfigs/strict"
}

==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\env.d.ts
==================================================
/// <reference types="astro/client" />


==================================================

Prázdná složka: C:\Users\thanh\Downloads\Programy\rotagym\src\components
Prázdná složka: C:\Users\thanh\Downloads\Programy\rotagym\src\layouts
Prázdná složka: C:\Users\thanh\Downloads\Programy\rotagym\src\pages
Prázdná složka: C:\Users\thanh\Downloads\Programy\rotagym\src\styles
Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\components\Card.astro
==================================================
---
interface Props {
	title: string;
	body: string;
	href: string;
}

const { href, title, body } = Astro.props;
---

<li class="link-card">
	<a href={href}>
		<h2>
			{title}
			<span>&rarr;</span>
		</h2>
		<p>
			{body}
		</p>
	</a>
</li>
<style>
	.link-card {
		list-style: none;
		display: flex;
		padding: 1px;
		background-color: #23262d;
		background-image: none;
		background-size: 400%;
		border-radius: 7px;
		background-position: 100%;
		transition: background-position 0.6s cubic-bezier(0.22, 1, 0.36, 1);
		box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.1);
	}
	.link-card > a {
		width: 100%;
		text-decoration: none;
		line-height: 1.4;
		padding: calc(1.5rem - 1px);
		border-radius: 8px;
		color: white;
		background-color: #23262d;
		opacity: 0.8;
	}
	h2 {
		margin: 0;
		font-size: 1.25rem;
		transition: color 0.6s cubic-bezier(0.22, 1, 0.36, 1);
	}
	p {
		margin-top: 0.5rem;
		margin-bottom: 0;
	}
	.link-card:is(:hover, :focus-within) {
		background-position: 0;
		background-image: var(--accent-gradient);
	}
	.link-card:is(:hover, :focus-within) h2 {
		color: rgb(var(--accent-light));
	}
</style>


==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\layouts\Layout.astro
==================================================
---
import '../styles/global.css';

interface Props {
    title: string;
}

const { title } = Astro.props;
---

<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="description" content="Astro description" />
        <meta name="viewport" content="width=device-width" />
        <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
        <meta name="generator" content={Astro.generator} />
        <title>{title}</title>
    </head>
    <body>
        <slot />
    </body>
</html>


==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\pages\example1.astro
==================================================
---
import Layout from "../layouts/Layout.astro";
import { Icon } from 'astro-icon/components';
---

<Layout title="Phòng tập Rota - Hiện đại và tối giản">
    <main
        class="bg-gradient-to-b from-gray-900 to-black text-white min-h-screen font-sans"
    >
        <header
            class="bg-black bg-opacity-50 backdrop-filter backdrop-blur-lg p-4 fixed w-full z-10"
        >
            <div class="container mx-auto flex justify-between items-center">
                <h1
                    class="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600"
                >
                    Phòng tập Rota
                </h1>
                <nav class="hidden md:flex">
                    <a
                        href="#about"
                        class="mx-2 hover:text-purple-400 transition-colors duration-300"
                        >Về chúng tôi</a
                    >
                    <a
                        href="#services"
                        class="mx-2 hover:text-purple-400 transition-colors duration-300"
                        >Dịch vụ</a
                    >
                    <a
                        href="#pricing"
                        class="mx-2 hover:text-purple-400 transition-colors duration-300"
                        >Bảng giá</a
                    >
                    <a
                        href="#gallery"
                        class="mx-2 hover:text-purple-400 transition-colors duration-300"
                        >Thư viện ảnh</a
                    >
                    <a
                        href="#contact"
                        class="mx-2 hover:text-purple-400 transition-colors duration-300"
                        >Liên hệ</a
                    >
                </nav>
                <button id="menu-toggle" class="md:hidden text-white">
                    <Icon name="mdi:menu" class="w-6 h-6" />
                </button>
            </div>
            <nav id="mobile-menu" class="hidden mt-4 md:hidden">
                <a
                    href="#about"
                    class="block py-2 hover:text-purple-400 transition-colors duration-300"
                    >Về chúng tôi</a
                >
                <a
                    href="#services"
                    class="block py-2 hover:text-purple-400 transition-colors duration-300"
                    >Dịch vụ</a
                >
                <a
                    href="#pricing"
                    class="block py-2 hover:text-purple-400 transition-colors duration-300"
                    >Bảng giá</a
                >
                <a
                    href="#gallery"
                    class="block py-2 hover:text-purple-400 transition-colors duration-300"
                    >Thư viện ảnh</a
                >
                <a
                    href="#contact"
                    class="block py-2 hover:text-purple-400 transition-colors duration-300"
                    >Liên hệ</a
                >
            </nav>
        </header>

        <section
            id="hero"
            class="relative h-screen flex items-center justify-center"
        >
            <div class="absolute inset-0">
                <img
                    src="../../public/hero.jpg"
                    alt="Nội thất hiện đại của phòng tập"
                    class="w-full h-full object-cover"
                />
                <div class="absolute inset-0 bg-black bg-opacity-50"></div>
            </div>
            <div class="relative z-10 text-center">
                <h2
                    class="text-4xl md:text-6xl font-bold mb-4 animate-fade-in-up"
                >
                    Bước vào thế giới thể hình hiện đại
                </h2>
                <a
                    href="#services"
                    class="inline-block bg-purple-600 text-white px-6 py-3 rounded-full hover:bg-purple-700 transition-colors duration-300"
                >
                    Khám phá dịch vụ
                    <Icon
                        name="mdi:arrow-right"
                        class="inline-block w-5 h-5 ml-2"
                    />
                </a>
            </div>
        </section>

        <section id="about" class="py-20 bg-gray-900">
            <div class="container mx-auto px-4">
                <h2
                    class="text-3xl md:text-4xl font-bold mb-8 text-center text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600"
                >
                    Về chúng tôi
                </h2>
                <p class="text-xl max-w-3xl mx-auto text-center">
                    Phòng tập Rota là trung tâm thể hình hiện đại tập trung vào
                    việc đạt được mục tiêu của bạn trong môi trường dễ chịu và
                    khích lệ. Chúng tôi kết hợp công nghệ tiên tiến với phương
                    pháp huấn luyện chuyên nghiệp để mang lại trải nghiệm tập
                    luyện tối ưu.
                </p>
            </div>
        </section>

        <section id="services" class="py-20">
            <div class="container mx-auto px-4">
                <h2
                    class="text-3xl md:text-4xl font-bold mb-8 text-center text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600"
                >
                    Dịch vụ
                </h2>
                <div
                    class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8"
                >
                    <div
                        class="bg-gray-800 bg-opacity-50 p-6 rounded-lg backdrop-filter backdrop-blur-lg hover:shadow-lg transition-shadow duration-300"
                    >
                        <Icon
                            name="mdi:account-cowboy-hat"
                            class="w-12 h-12 mb-4 text-purple-400"
                        />
                        <h3 class="text-xl font-bold mb-2">
                            Huấn luyện cá nhân
                        </h3>
                        <p>
                            Chương trình tập luyện được cá nhân hóa để đáp ứng
                            mục tiêu cụ thể của bạn.
                        </p>
                    </div>
                    <div
                        class="bg-gray-800 bg-opacity-50 p-6 rounded-lg backdrop-filter backdrop-blur-lg hover:shadow-lg transition-shadow duration-300"
                    >
                        <Icon
                            name="mdi:account-group"
                            class="w-12 h-12 mb-4 text-purple-400"
                        />
                        <h3 class="text-xl font-bold mb-2">Lớp học nhóm</h3>
                        <p>
                            Tham gia các lớp học nhóm năng động để tăng cường
                            động lực và kết nối xã hội.
                        </p>
                    </div>
                    <div
                        class="bg-gray-800 bg-opacity-50 p-6 rounded-lg backdrop-filter backdrop-blur-lg hover:shadow-lg transition-shadow duration-300"
                    >
                        <Icon
                            name="mdi:run"
                            class="w-12 h-12 mb-4 text-purple-400"
                        />
                        <h3 class="text-xl font-bold mb-2">Khu vực cardio</h3>
                        <p>
                            Trang thiết bị cardio hiện đại để cải thiện sức bền
                            và đốt cháy calo.
                        </p>
                    </div>
                    <div
                        class="bg-gray-800 bg-opacity-50 p-6 rounded-lg backdrop-filter backdrop-blur-lg hover:shadow-lg transition-shadow duration-300"
                    >
                        <Icon
                            name="mdi:weight-lifter"
                            class="w-12 h-12 mb-4 text-purple-400"
                        />
                        <h3 class="text-xl font-bold mb-2">
                            Huấn luyện sức mạnh
                        </h3>
                        <p>
                            Khu vực tập luyện sức mạnh với đầy đủ thiết bị để
                            xây dựng cơ bắp và sức mạnh.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section id="pricing" class="py-20 bg-gray-900">
            <div class="container mx-auto px-4">
                <h2
                    class="text-3xl md:text-4xl font-bold mb-8 text-center text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600"
                >
                    Bảng giá
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div
                        class="bg-gray-800 bg-opacity-50 p-6 rounded-lg backdrop-filter backdrop-blur-lg hover:shadow-lg transition-shadow duration-300"
                    >
                        <h3 class="text-xl font-bold mb-4">Đi một lần</h3>
                        <p class="text-3xl font-bold text-purple-400 mb-4">
                            150.000 VND
                        </p>
                        <ul class="mb-6">
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Truy cập toàn bộ thiết bị
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Sử dụng phòng tắm và tủ khóa
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="block text-center bg-purple-600 text-white px-4 py-2 rounded-full hover:bg-purple-700 transition-colors duration-300"
                            >Đăng ký ngay</a
                        >
                    </div>
                    <div
                        class="bg-gray-800 bg-opacity-50 p-6 rounded-lg backdrop-filter backdrop-blur-lg hover:shadow-lg transition-shadow duration-300 transform scale-105"
                    >
                        <h3 class="text-xl font-bold mb-4">
                            Thành viên hàng tháng
                        </h3>
                        <p class="text-3xl font-bold text-purple-400 mb-4">
                            1.200.000 VND
                        </p>
                        <ul class="mb-6">
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Truy cập không giới hạn
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Tham gia lớp học nhóm miễn phí
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Tư vấn dinh dưỡng cơ bản
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="block text-center bg-purple-600 text-white px-4 py-2 rounded-full hover:bg-purple-700 transition-colors duration-300"
                            >Đăng ký ngay</a
                        >
                    </div>
                    <div
                        class="bg-gray-800 bg-opacity-50 p-6 rounded-lg backdrop-filter backdrop-blur-lg hover:shadow-lg transition-shadow duration-300"
                    >
                        <h3 class="text-xl font-bold mb-4">
                            Thành viên hàng năm
                        </h3>
                        <p class="text-3xl font-bold text-purple-400 mb-4">
                            12.000.000 VND
                        </p>
                        <ul class="mb-6">
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Tất cả quyền lợi của gói tháng
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                2 buổi huấn luyện cá nhân miễn phí
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Giảm giá 10% cho các dịch vụ bổ sung
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="block text-center bg-purple-600 text-white px-4 py-2 rounded-full hover:bg-purple-700 transition-colors duration-300"
                            >Đăng ký ngay</a
                        >
                    </div>
                </div>
            </div>
        </section>

        <section id="gallery" class="py-20">
            <div class="container mx-auto px-4">
                <h2
                    class="text-3xl md:text-4xl font-bold mb-8 text-center text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600"
                >
                    Thư viện ảnh
                </h2>
                <div
                    class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4"
                >
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 1"
                        class="w-full h-64 object-cover rounded-lg hover:opacity-75 transition-opacity duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 2"
                        class="w-full h-64 object-cover rounded-lg hover:opacity-75 transition-opacity duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 3"
                        class="w-full h-64 object-cover rounded-lg hover:opacity-75 transition-opacity duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 4"
                        class="w-full h-64 object-cover rounded-lg hover:opacity-75 transition-opacity duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 5"
                        class="w-full h-64 object-cover rounded-lg hover:opacity-75 transition-opacity duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 6"
                        class="w-full h-64 object-cover rounded-lg hover:opacity-75 transition-opacity duration-300"
                    />
                </div>
            </div>
        </section>

        <section id="contact" class="py-20 bg-gray-900">
            <div class="container mx-auto px-4">
                <h2
                    class="text-3xl md:text-4xl font-bold mb-8 text-center text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600"
                >
                    Liên hệ
                </h2>
                <form class="max-w-md mx-auto">
                    <div class="mb-4">
                        <label for="name" class="block mb-2">Họ tên</label>
                        <input
                            type="text"
                            id="name"
                            name="name"
                            class="w-full p-2 bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-purple-400"
                            required
                        />
                    </div>
                    <div class="mb-4">
                        <label for="email" class="block mb-2">Email</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            class="w-full p-2 bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-purple-400"
                            required
                        />
                    </div>
                    <div class="mb-4">
                        <label for="message" class="block mb-2">Tin nhắn</label>
                        <textarea
                            id="message"
                            name="message"
                            rows="4"
                            class="w-full p-2 bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-purple-400"
                            required></textarea>
                    </div>
                    <button
                        type="submit"
                        class="w-full bg-purple-600 text-white px-4 py-2 rounded-full hover:bg-purple-700 transition-colors duration-300"
                        >Gửi</button
                    >
                </form>
            </div>
        </section>

        <footer class="bg-black py-8">
            <div class="container mx-auto px-4">
                <div class="flex flex-wrap justify-between items-center">
                    <div class="w-full md:w-1/3 mb-6 md:mb-0">
                        <h3 class="text-xl font-bold mb-2">Phòng tập Rota</h3>
                        <p>Nâng cao sức khỏe và thể hình của bạn</p>
                    </div>
                    <div class="w-full md:w-1/3 mb-6 md:mb-0">
                        <h4 class="text-lg font-bold mb-2">Liên kết nhanh</h4>
                        <ul>
                            <li>
                                <a
                                    href="#about"
                                    class="hover:text-purple-400 transition-colors duration-300"
                                    >Về chúng tôi</a>
                            </li>
                            <li>
                                <a
                                    href="#services"
                                    class="hover:text-purple-400 transition-colors duration-300"
                                    >Dịch vụ</a>
                            </li>
                            <li>
                                <a
                                    href="#pricing"
                                    class="hover:text-purple-400 transition-colors duration-300"
                                    >Bảng giá</a>
                            </li>
                            <li>
                                <a
                                    href="#contact"
                                    class="hover:text-purple-400 transition-colors duration-300"
                                    >Liên hệ</a>
                            </li>
                        </ul>
                    </div>
                    <div class="w-full md:w-1/3">
                        <h4 class="text-lg font-bold mb-2">
                            Theo dõi chúng tôi
                        </h4>
                        <div class="flex space-x-4">
                            <a
                                href="#"
                                class="text-white hover:text-purple-400 transition-colors duration-300"
                            >
                                <Icon name="mdi:facebook" class="w-6 h-6" />
                            </a>
                            <a
                                href="#"
                                class="text-white hover:text-purple-400 transition-colors duration-300"
                            >
                                <Icon name="mdi:instagram" class="w-6 h-6" />
                            </a>
                            <a
                                href="#"
                                class="text-white hover:text-purple-400 transition-colors duration-300"
                            >
                                <Icon name="mdi:twitter" class="w-6 h-6" />
                            </a>
                        </div>
                    </div>
                </div>
                <div class="border-t border-gray-800 mt-8 pt-8 text-center">
                    <p>
                        &copy; 2024 Phòng tập Rota. T��t cả các quyền được bảo
                        lưu.
                    </p>
                </div>
            </div>
        </footer>
    </main>
</Layout>

<style>
    .animate-fade-in-up {
        animation: fadeInUp 1s ease-out;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>

<script>
    document.addEventListener("DOMContentLoaded", (event) => {
        const menuToggle = document.getElementById("menu-toggle");
        const mobileMenu = document.getElementById("mobile-menu");
        if (menuToggle && mobileMenu) {
            menuToggle.addEventListener("click", () => {
                mobileMenu.classList.toggle("hidden");
            });
        }

        // Přidáme plynulé scrollování pro navigační odkazy
        document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
            anchor.addEventListener("click", (e: Event) => {
                e.preventDefault();
                const href = (
                    e.currentTarget as HTMLAnchorElement
                ).getAttribute("href");
                if (href) {
                    document.querySelector(href)?.scrollIntoView({
                        behavior: "smooth",
                    });
                }
            });
        });
    });
</script>


==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\pages\example2.astro
==================================================
---
import Layout from "../layouts/Layout.astro";
import { Icon } from 'astro-icon/components';
---

<Layout title="Phòng tập Rota - Năng động và sôi nổi">
    <main
        class="bg-gradient-to-br from-blue-900 via-purple-900 to-pink-900 text-white min-h-screen font-sans"
    >
        <header
            class="bg-gradient-to-r from-blue-800 to-purple-800 p-4 sticky top-0 z-50"
        >
            <div class="container mx-auto flex justify-between items-center">
                <h1
                    class="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-500"
                >
                    Phòng tập Rota
                </h1>
                <nav class="hidden md:flex space-x-6">
                    <a
                        href="#about"
                        class="hover:text-yellow-400 transition-colors duration-300"
                        >Về chúng tôi</a
                    >
                    <a
                        href="#services"
                        class="hover:text-yellow-400 transition-colors duration-300"
                        >Dịch vụ</a
                    >
                    <a
                        href="#pricing"
                        class="hover:text-yellow-400 transition-colors duration-300"
                        >Bảng giá</a
                    >
                    <a
                        href="#gallery"
                        class="hover:text-yellow-400 transition-colors duration-300"
                        >Thư viện ảnh</a
                    >
                    <a
                        href="#contact"
                        class="hover:text-yellow-400 transition-colors duration-300"
                        >Liên hệ</a
                    >
                </nav>
                <button id="menu-toggle" class="md:hidden text-white">
                    <Icon name="mdi:menu" class="w-6 h-6" />
                </button>
            </div>
            <nav id="mobile-menu" class="hidden mt-4 md:hidden">
                <a
                    href="#about"
                    class="block py-2 hover:text-yellow-400 transition-colors duration-300"
                    >Về chúng tôi</a
                >
                <a
                    href="#services"
                    class="block py-2 hover:text-yellow-400 transition-colors duration-300"
                    >Dịch vụ</a
                >
                <a
                    href="#pricing"
                    class="block py-2 hover:text-yellow-400 transition-colors duration-300"
                    >Bảng giá</a
                >
                <a
                    href="#gallery"
                    class="block py-2 hover:text-yellow-400 transition-colors duration-300"
                    >Thư viện ảnh</a
                >
                <a
                    href="#contact"
                    class="block py-2 hover:text-yellow-400 transition-colors duration-300"
                    >Liên hệ</a
                >
            </nav>
        </header>

        <section id="hero" class="py-20 relative overflow-hidden">
            <div class="container mx-auto text-center px-4 relative z-10">
                <h2
                    class="text-5xl md:text-7xl font-bold mb-8 animate-pulse-scale"
                >
                    Vượt qua giới hạn của bạn!
                </h2>
                <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto">
                    Hãy tham gia cùng chúng tôi và khám phá tiềm năng thực sự
                    của bản thân trong một môi trường năng động và đầy cảm hứng.
                </p>
                <a
                    href="#services"
                    class="bg-gradient-to-r from-yellow-400 to-orange-500 text-blue-900 font-bold py-3 px-8 rounded-full hover:from-yellow-300 hover:to-orange-400 transition-all duration-300 transform hover:scale-105"
                >
                    Bắt đầu ngay
                    <Icon
                        name="mdi:arrow-right"
                        class="inline-block w-5 h-5 ml-2"
                    />
                </a>
            </div>
            <div class="absolute inset-0 z-0">
                <img
                    src="https://via.placeholder.com/1920x1080"
                    alt="Người tập thể dục"
                    class="w-full h-full object-cover opacity-30"
                />
            </div>
            <div
                class="absolute inset-0 bg-gradient-to-b from-transparent to-blue-900 z-0"
            >
            </div>
        </section>

        <section id="about" class="py-20 bg-blue-800 transform -skew-y-3">
            <div class="container mx-auto skew-y-3 px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-8 text-center text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-500"
                >
                    Về chúng tôi
                </h2>
                <p class="text-lg md:text-xl max-w-4xl mx-auto text-center">
                    Phòng tập Rota là nơi hội tụ năng lượng, động lực và kết
                    quả. Chúng tôi không chỉ là một phòng tập gym thông thường,
                    mà là một cộng đồng những người đam mê fitness, luôn sẵn
                    sàng hỗ trợ và truyền cảm hứng cho nhau. Với đội ngũ huấn
                    luyện viên chuyên nghiệp và trang thiết bị hiện đại, chúng
                    tôi cam kết mang đến cho bạn trải nghiệm tập luyện tốt nhất.
                </p>
            </div>
        </section>

        <section id="services" class="py-20">
            <div class="container mx-auto px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-12 text-center text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-500"
                >
                    Dịch vụ của chúng tôi
                </h2>
                <div
                    class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8"
                >
                    <div
                        class="bg-blue-800 p-6 rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    >
                        <Icon
                            name="mdi:dumbbell"
                            class="w-16 h-16 mb-4 text-yellow-400 mx-auto"
                        />
                        <h3 class="text-2xl font-bold mb-4 text-center">
                            Huấn luyện cá nhân
                        </h3>
                        <p class="text-center">
                            Chương trình tập luyện được cá nhân hóa để đáp ứng
                            mục tiêu cụ thể của bạn.
                        </p>
                    </div>
                    <div
                        class="bg-blue-800 p-6 rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    >
                        <Icon
                            name="mdi:account-group"
                            class="w-16 h-16 mb-4 text-yellow-400 mx-auto"
                        />
                        <h3 class="text-2xl font-bold mb-4 text-center">
                            Lớp học nhóm
                        </h3>
                        <p class="text-center">
                            Tham gia các lớp học nhóm năng động để tăng cường
                            động lực và kết nối xã hội.
                        </p>
                    </div>
                    <div
                        class="bg-blue-800 p-6 rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    >
                        <Icon
                            name="mdi:heart-pulse"
                            class="w-16 h-16 mb-4 text-yellow-400 mx-auto"
                        />
                        <h3 class="text-2xl font-bold mb-4 text-center">
                            Khu vực cardio
                        </h3>
                        <p class="text-center">
                            Trang thiết bị cardio hiện đại để cải thiện sức bền
                            và đốt cháy calo.
                        </p>
                    </div>
                    <div
                        class="bg-blue-800 p-6 rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    >
                        <Icon
                            name="mdi:weight-lifter"
                            class="w-16 h-16 mb-4 text-yellow-400 mx-auto"
                        />
                        <h3 class="text-2xl font-bold mb-4 text-center">
                            Tập luyện sức mạnh
                        </h3>
                        <p class="text-center">
                            Khu vực tập luyện sức mạnh với đầy đủ thiết bị để
                            xây dựng cơ bắp và sức mạnh.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section id="pricing" class="py-20 bg-blue-800 transform skew-y-3">
            <div class="container mx-auto -skew-y-3 px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-12 text-center text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-500"
                >
                    Bảng giá
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div
                        class="bg-blue-700 p-8 rounded-lg shadow-lg text-center"
                    >
                        <h3 class="text-2xl font-bold mb-4">Vé vào một lần</h3>
                        <p class="text-4xl font-bold text-yellow-400 mb-6">
                            150.000 VND
                        </p>
                        <ul class="mb-8 text-left">
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check-circle"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Truy cập toàn bộ thiết bị
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check-circle"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Sử dụng phòng tắm và tủ khóa
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="inline-block bg-gradient-to-r from-yellow-400 to-orange-500 text-blue-900 font-bold py-2 px-6 rounded-full hover:from-yellow-300 hover:to-orange-400 transition-all duration-300"
                            >Đăng ký ngay</a
                        >
                    </div>
                    <div
                        class="bg-blue-700 p-8 rounded-lg shadow-lg text-center transform scale-105"
                    >
                        <h3 class="text-2xl font-bold mb-4">
                            Thành viên hàng tháng
                        </h3>
                        <p class="text-4xl font-bold text-yellow-400 mb-6">
                            1.200.000 VND
                        </p>
                        <ul class="mb-8 text-left">
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check-circle"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Truy cập không giới hạn
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check-circle"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Tham gia lớp học nhóm miễn phí
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check-circle"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Tư vấn dinh dưỡng cơ bản
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="inline-block bg-gradient-to-r from-yellow-400 to-orange-500 text-blue-900 font-bold py-2 px-6 rounded-full hover:from-yellow-300 hover:to-orange-400 transition-all duration-300"
                            >Đăng ký ngay</a
                        >
                    </div>
                    <div
                        class="bg-blue-700 p-8 rounded-lg shadow-lg text-center"
                    >
                        <h3 class="text-2xl font-bold mb-4">
                            Thành viên hàng năm
                        </h3>
                        <p class="text-4xl font-bold text-yellow-400 mb-6">
                            12.000.000 VND
                        </p>
                        <ul class="mb-8 text-left">
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check-circle"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Tất cả quyền lợi của gói tháng
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check-circle"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                2 buổi huấn luyện cá nhân miễn phí
                            </li>
                            <li class="flex items-center mb-2">
                                <Icon
                                    name="mdi:check-circle"
                                    class="w-5 h-5 mr-2 text-green-400"
                                />
                                Giảm giá 10% cho các dịch vụ bổ sung
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="inline-block bg-gradient-to-r from-yellow-400 to-orange-500 text-blue-900 font-bold py-2 px-6 rounded-full hover:from-yellow-300 hover:to-orange-400 transition-all duration-300"
                            >Đăng ký ngay</a
                        >
                    </div>
                </div>
            </div>
        </section>

        <section id="gallery" class="py-20">
            <div class="container mx-auto px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-12 text-center text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-500"
                >
                    Thư viện ảnh
                </h2>
                <div
                    class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"
                >
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Ảnh phòng tập 1"
                        class="w-full h-64 object-cover rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Ảnh phòng tập 2"
                        class="w-full h-64 object-cover rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Ảnh phòng tập 3"
                        class="w-full h-64 object-cover rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Ảnh phòng tập 4"
                        class="w-full h-64 object-cover rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Ảnh phòng tập 5"
                        class="w-full h-64 object-cover rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Ảnh phòng tập 6"
                        class="w-full h-64 object-cover rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Ảnh phòng tập 7"
                        class="w-full h-64 object-cover rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Ảnh phòng tập 8"
                        class="w-full h-64 object-cover rounded-lg shadow-lg transform hover:scale-105 transition-all duration-300"
                    />
                </div>
            </div>
        </section>

        <section id="contact" class="py-20 bg-blue-800">
            <div class="container mx-auto text-center px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-12 text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-500"
                >
                    Liên hệ
                </h2>
                <div
                    class="max-w-3xl mx-auto bg-blue-700 p-8 rounded-lg shadow-lg"
                >
                    <form class="space-y-6">
                        <div>
                            <input
                                type="text"
                                placeholder="Họ và tên"
                                class="w-full p-3 rounded bg-blue-600 text-white placeholder-blue-300 focus:outline-none focus:ring-2 focus:ring-yellow-400"
                                required
                            />
                        </div>
                        <div>
                            <input
                                type="email"
                                placeholder="Email"
                                class="w-full p-3 rounded bg-blue-600 text-white placeholder-blue-300 focus:outline-none focus:ring-2 focus:ring-yellow-400"
                                required
                            />
                        </div>
                        <div>
                            <textarea
                                placeholder="Tin nhắn"
                                rows="4"
                                class="w-full p-3 rounded bg-blue-600 text-white placeholder-blue-300 focus:outline-none focus:ring-2 focus:ring-yellow-400"
                                required></textarea>
                        </div>
                        <button
                            type="submit"
                            class="bg-gradient-to-r from-yellow-400 to-orange-500 text-blue-900 font-bold py-3 px-8 rounded-full hover:from-yellow-300 hover:to-orange-400 transition-all duration-300 transform hover:scale-105"
                            >Gửi</button
                        >
                    </form>
                </div>
                <div class="mt-12 flex justify-center space-x-6">
                    <a
                        href="#"
                        class="text-white hover:text-yellow-400 transition-colors duration-300"
                    >
                        <Icon name="mdi:facebook" class="w-8 h-8" />
                    </a>
                    <a
                        href="#"
                        class="text-white hover:text-yellow-400 transition-colors duration-300"
                    >
                        <Icon name="mdi:instagram" class="w-8 h-8" />
                    </a>
                    <a
                        href="#"
                        class="text-white hover:text-yellow-400 transition-colors duration-300"
                    >
                        <Icon name="mdi:twitter" class="w-8 h-8" />
                    </a>
                </div>
            </div>
        </section>

        <footer class="bg-blue-900 py-8">
            <div class="container mx-auto px-4">
                <div class="flex flex-wrap justify-between items-center">
                    <div class="w-full md:w-1/3 mb-6 md:mb-0">
                        <h3 class="text-2xl font-bold text-yellow-400 mb-2">
                            Phòng tập Rota
                        </h3>
                        <p>Nâng cao sức khỏe và thể hình của bạn</p>
                    </div>
                    <div class="w-full md:w-1/3 mb-6 md:mb-0">
                        <h4 class="text-xl font-bold text-yellow-400 mb-4">
                            Liên kết nhanh
                        </h4>
                        <ul class="space-y-2">
                            <li>
                                <a
                                    href="#about"
                                    class="hover:text-yellow-400 transition-colors duration-300"
                                    >Về chúng tôi</a>
                            </li>
                            <li>
                                <a
                                    href="#services"
                                    class="hover:text-yellow-400 transition-colors duration-300"
                                    >Dịch vụ</a>
                            </li>
                            <li>
                                <a
                                    href="#pricing"
                                    class="hover:text-yellow-400 transition-colors duration-300"
                                    >Bảng giá</a>
                            </li>
                            <li>
                                <a
                                    href="#contact"
                                    class="hover:text-yellow-400 transition-colors duration-300"
                                    >Liên hệ</a>
                            </li>
                        </ul>
                    </div>
                    <div class="w-full md:w-1/3">
                        <h4 class="text-xl font-bold text-yellow-400 mb-4">
                            Thông tin liên hệ
                        </h4>
                        <p class="flex items-center mb-2">
                            <Icon
                                name="mdi:map-marker"
                                class="w-5 h-5 mr-2 text-yellow-400"
                            />
                            123 Đường Fitness, Thành phố 123 45
                        </p>
                        <p class="flex items-center mb-2">
                            <Icon
                                name="mdi:phone"
                                class="w-5 h-5 mr-2 text-yellow-400"
                            />
                            +84 123 456 789
                        </p>
                        <p class="flex items-center">
                            <Icon
                                name="mdi:email"
                                class="w-5 h-5 mr-2 text-yellow-400"
                            />
                            info@rotagym.vn
                        </p>
                    </div>
                </div>
                <div class="border-t border-blue-800 mt-8 pt-8 text-center">
                    <p>&copy; 2024 Phòng tập Rota. Đã đăng ký bản quyền.</p>
                </div>
            </div>
        </footer>
    </main>
</Layout>

<style>
    .animate-pulse-scale {
        animation: pulseScale 2s infinite;
    }

    @keyframes pulseScale {
        0%,
        100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
</style>

<script>
    document.addEventListener("DOMContentLoaded", (event) => {
        const menuToggle = document.getElementById("menu-toggle");
        const mobileMenu = document.getElementById("mobile-menu");
        if (menuToggle && mobileMenu) {
            menuToggle.addEventListener("click", () => {
                mobileMenu.classList.toggle("hidden");
            });
        }

        // Плавная прокрутка для навигационных ссылок
        document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
            anchor.addEventListener("click", (e: Event) => {
                e.preventDefault();
                const href = (
                    e.currentTarget as HTMLAnchorElement
                ).getAttribute("href");
                if (href) {
                    document.querySelector(href)?.scrollIntoView({
                        behavior: "smooth",
                    });
                }
            });
        });
    });
</script>


==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\pages\example3.astro
==================================================
---
import Layout from "../layouts/Layout.astro";
import { Icon } from 'astro-icon/components';
---

<Layout title="Rota Gym - Công nghiệp và thô mộc">
    <main class="bg-black text-gray-300 min-h-screen font-mono">
        <header class="bg-zinc-900 p-4 sticky top-0 z-50">
            <div class="container mx-auto flex justify-between items-center">
                <h1
                    class="text-3xl font-bold text-red-600 glitch"
                    data-text="ROTA GYM"
                >
                    ROTA GYM
                </h1>
                <nav class="hidden md:flex space-x-6">
                    <a
                        href="#about"
                        class="hover:text-red-600 transition-colors duration-300"
                        >VỀ CHÚNG TÔI</a
                    >
                    <a
                        href="#services"
                        class="hover:text-red-600 transition-colors duration-300"
                        >DỊCH VỤ</a
                    >
                    <a
                        href="#pricing"
                        class="hover:text-red-600 transition-colors duration-300"
                        >GIÁ CẢ</a
                    >
                    <a
                        href="#gallery"
                        class="hover:text-red-600 transition-colors duration-300"
                        >THƯ VIỆN ẢNH</a
                    >
                    <a
                        href="#contact"
                        class="hover:text-red-600 transition-colors duration-300"
                        >LIÊN HỆ</a
                    >
                </nav>
                <button id="menu-toggle" class="md:hidden text-red-600">
                    <Icon name="mdi:menu" class="w-6 h-6" />
                </button>
            </div>
            <nav id="mobile-menu" class="hidden mt-4 md:hidden">
                <a
                    href="#about"
                    class="block py-2 hover:text-red-600 transition-colors duration-300"
                    >VỀ CHÚNG TÔI</a
                >
                <a
                    href="#services"
                    class="block py-2 hover:text-red-600 transition-colors duration-300"
                    >DỊCH VỤ</a
                >
                <a
                    href="#pricing"
                    class="block py-2 hover:text-red-600 transition-colors duration-300"
                    >GIÁ CẢ</a
                >
                <a
                    href="#gallery"
                    class="block py-2 hover:text-red-600 transition-colors duration-300"
                    >THƯ VIỆN ẢNH</a
                >
                <a
                    href="#contact"
                    class="block py-2 hover:text-red-600 transition-colors duration-300"
                    >LIÊN HỆ</a
                >
            </nav>
        </header>

        <section id="hero" class="py-20 bg-zinc-800 relative overflow-hidden">
            <div class="container mx-auto text-center px-4 relative z-10">
                <h2
                    class="text-5xl md:text-7xl font-bold mb-8 text-red-600 typewriter"
                >
                    SỨC MẠNH LÀ LỰA CHỌN
                </h2>
                <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto">
                    Tại Rota Gym, chúng tôi không chỉ xây dựng cơ bắp. Chúng tôi
                    rèn luyện ý chí.
                </p>
                <a
                    href="#services"
                    class="bg-red-600 text-black font-bold py-3 px-8 rounded-none hover:bg-red-700 transition-colors duration-300 inline-flex items-center group"
                >
                    KHÁM PHÁ NGAY
                    <Icon
                        name="mdi:arrow-right"
                        class="w-5 h-5 ml-2 transform group-hover:translate-x-1 transition-transform duration-300"
                    />
                </a>
            </div>
            <div class="absolute inset-0 z-0 opacity-20">
                <img
                    src="../../public/hero.jpg"
                    alt="Gym Equipment"
                    class="w-full h-full object-cover"
                />
            </div>
            <div
                class="absolute inset-0 bg-gradient-to-b from-transparent to-black z-0"
            >
            </div>
        </section>

        <section id="about" class="py-20 bg-zinc-900">
            <div class="container mx-auto px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-12 text-center text-red-600"
                >
                    VỀ CHÚNG TÔI
                </h2>
                <div
                    class="flex flex-col md:flex-row items-center justify-between"
                >
                    <div class="md:w-1/2 mb-8 md:mb-0">
                        <img
                            src="https://via.placeholder.com/600x400"
                            alt="Gym Interior"
                            class="w-full h-auto rounded-none shadow-lg"
                        />
                    </div>
                    <div class="md:w-1/2 md:pl-12">
                        <p class="text-lg mb-6">
                            Rota Gym không chỉ là phòng tập gym. Đó là nơi mồ
                            hôi trộn lẫn với quyết tâm, nơi mỗi âm thanh của sắt
                            thép là âm nhạc cho tai của những chiến binh thực
                            sự. Tại đây, sức mạnh, sự kiên trì và nhân cách được
                            sinh ra.
                        </p>
                        <p class="text-lg mb-6">
                            Chúng tôi tin rằng sức mạnh thực sự đến từ bên
                            trong. Đó là lý do tại sao chúng tôi không chỉ tập
                            trung vào việc xây dựng cơ bắp, mà còn rèn luyện
                            tinh thần và ý chí của bạn.
                        </p>
                        <a
                            href="#services"
                            class="inline-block bg-red-600 text-black font-bold py-2 px-6 rounded-none hover:bg-red-700 transition-colors duration-300"
                            >TÌM HIỂU THÊM</a
                        >
                    </div>
                </div>
            </div>
        </section>

        <section id="services" class="py-20 bg-black">
            <div class="container mx-auto px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-12 text-center text-red-600"
                >
                    DỊCH VỤ
                </h2>
                <div
                    class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8"
                >
                    <div
                        class="bg-zinc-800 p-6 border border-red-600 group hover:bg-red-600 transition-colors duration-300"
                    >
                        <Icon
                            name="mdi:dumbbell"
                            class="w-16 h-16 mb-4 text-red-600 group-hover:text-black transition-colors duration-300"
                        />
                        <h3
                            class="text-2xl font-bold mb-4 group-hover:text-black transition-colors duration-300"
                        >
                            HUẤN LUYỆN CÁ NHÂN
                        </h3>
                        <p
                            class="group-hover:text-black transition-colors duration-300"
                        >
                            Vượt qua giới hạn của bạn với các huấn luyện viên
                            giàu kinh nghiệm của chúng tôi
                        </p>
                    </div>
                    <div
                        class="bg-zinc-800 p-6 border border-red-600 group hover:bg-red-600 transition-colors duration-300"
                    >
                        <Icon
                            name="mdi:weight-lifter"
                            class="w-16 h-16 mb-4 text-red-600 group-hover:text-black transition-colors duration-300"
                        />
                        <h3
                            class="text-2xl font-bold mb-4 group-hover:text-black transition-colors duration-300"
                        >
                            HUẤN LUYỆN SỨC MẠNH
                        </h3>
                        <p
                            class="group-hover:text-black transition-colors duration-300"
                        >
                            Đặt nặng, xây dựng sức mạnh và nhân cách
                        </p>
                    </div>
                    <div
                        class="bg-zinc-800 p-6 border border-red-600 group hover:bg-red-600 transition-colors duration-300"
                    >
                        <Icon
                            name="mdi:run-fast"
                            class="w-16 h-16 mb-4 text-red-600 group-hover:text-black transition-colors duration-300"
                        />
                        <h3
                            class="text-2xl font-bold mb-4 group-hover:text-black transition-colors duration-300"
                        >
                            KHU VỰC THỂ DỤC
                        </h3>
                        <p
                            class="group-hover:text-black transition-colors duration-300"
                        >
                            Đẩy giới hạn thể dục của bạn lên một cấp độ mới
                        </p>
                    </div>
                    <div
                        class="bg-zinc-800 p-6 border border-red-600 group hover:bg-red-600 transition-colors duration-300"
                    >
                        <Icon
                            name="mdi:food-apple"
                            class="w-16 h-16 mb-4 text-red-600 group-hover:text-black transition-colors duration-300"
                        />
                        <h3
                            class="text-2xl font-bold mb-4 group-hover:text-black transition-colors duration-300"
                        >
                            TƯ VẤN DINH DƯỠNG
                        </h3>
                        <p
                            class="group-hover:text-black transition-colors duration-300"
                        >
                            Tối ưu hóa kết quả của bạn với chế độ dinh dưỡng phù
                            hợp
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section id="pricing" class="py-20 bg-zinc-900">
            <div class="container mx-auto px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-12 text-center text-red-600"
                >
                    GIÁ CẢ
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-black p-8 border-t-4 border-red-600">
                        <h3 class="text-2xl font-bold mb-4">ĐẦU VÀO ĐƠN LẺ</h3>
                        <p class="text-4xl font-bold text-red-600 mb-6">
                            150 Kč
                        </p>
                        <ul class="mb-8 space-y-2">
                            <li class="flex items-center">
                                <Icon
                                    name="mdi:check-bold"
                                    class="w-5 h-5 mr-2 text-red-600"
                                />
                                Truy cập toàn bộ thiết bị
                            </li>
                            <li class="flex items-center">
                                <Icon
                                    name="mdi:check-bold"
                                    class="w-5 h-5 mr-2 text-red-600"
                                />
                                Sử dụng phòng tắm và tủ khóa
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="block text-center bg-red-600 text-black font-bold py-2 px-6 rounded-none hover:bg-red-700 transition-colors duration-300"
                            >ĐĂNG KÝ NGAY</a
                        >
                    </div>
                    <div
                        class="bg-black p-8 border-t-4 border-red-600 transform scale-105"
                    >
                        <h3 class="text-2xl font-bold mb-4">
                            THÀNH VIÊN THÁNG
                        </h3>
                        <p class="text-4xl font-bold text-red-600 mb-6">
                            1200 Kč
                        </p>
                        <ul class="mb-8 space-y-2">
                            <li class="flex items-center">
                                <Icon
                                    name="mdi:check-bold"
                                    class="w-5 h-5 mr-2 text-red-600"
                                />
                                Truy cập không giới hạn
                            </li>
                            <li class="flex items-center">
                                <Icon
                                    name="mdi:check-bold"
                                    class="w-5 h-5 mr-2 text-red-600"
                                />
                                Tham gia lớp học nhóm miễn phí
                            </li>
                            <li class="flex items-center">
                                <Icon
                                    name="mdi:check-bold"
                                    class="w-5 h-5 mr-2 text-red-600"
                                />
                                Tư vấn dinh dưỡng cơ bản
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="block text-center bg-red-600 text-black font-bold py-2 px-6 rounded-none hover:bg-red-700 transition-colors duration-300"
                            >ĐĂNG KÝ NGAY</a
                        >
                    </div>
                    <div class="bg-black p-8 border-t-4 border-red-600">
                        <h3 class="text-2xl font-bold mb-4">THÀNH VIÊN NĂM</h3>
                        <p class="text-4xl font-bold text-red-600 mb-6">
                            12000 Kč
                        </p>
                        <ul class="mb-8 space-y-2">
                            <li class="flex items-center">
                                <Icon
                                    name="mdi:check-bold"
                                    class="w-5 h-5 mr-2 text-red-600"
                                />
                                Tất cả quyền lợi của gói tháng
                            </li>
                            <li class="flex items-center">
                                <Icon
                                    name="mdi:check-bold"
                                    class="w-5 h-5 mr-2 text-red-600"
                                />
                                2 buổi huấn luyện cá nhân miễn phí
                            </li>
                            <li class="flex items-center">
                                <Icon
                                    name="mdi:check-bold"
                                    class="w-5 h-5 mr-2 text-red-600"
                                />
                                Giảm giá 10% cho các dịch vụ bổ sung
                            </li>
                        </ul>
                        <a
                            href="#contact"
                            class="block text-center bg-red-600 text-black font-bold py-2 px-6 rounded-none hover:bg-red-700 transition-colors duration-300"
                            >ĐĂNG KÝ NGAY</a
                        >
                    </div>
                </div>
            </div>
        </section>

        <section id="gallery" class="py-20 bg-black">
            <div class="container mx-auto px-4">
                <h2
                    class="text-4xl md:text-5xl font-bold mb-12 text-center text-red-600"
                >
                    THƯ VIỆN ẢNH
                </h2>
                <div
                    class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"
                >
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 1"
                        class="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 2"
                        class="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 3"
                        class="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 4"
                        class="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 5"
                        class="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 6"
                        class="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 7"
                        class="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/400x300"
                        alt="Ảnh phòng tập 8"
                        class="w-full h-64 object-cover grayscale hover:grayscale-0 transition-all duration-300"
                    />
                </div>
            </div>
        </section>

        <section id="contact" class="py-20 bg-zinc-900">
            <div class="container mx-auto text-center px-4">
                <h2 class="text-4xl md:text-5xl font-bold mb-12 text-red-600">
                    LIÊN HỆ
                </h2>
                <div
                    class="max-w-3xl mx-auto bg-black p-8 border border-red-600"
                >
                    <form class="space-y-6">
                        <div>
                            <input
                                type="text"
                                placeholder="Họ và tên"
                                class="w-full p-3 bg-zinc-800 text-white placeholder-gray-500 border-b-2 border-red-600 focus:outline-none focus:border-red-400"
                                required
                            />
                        </div>
                        <div>
                            <input
                                type="email"
                                placeholder="Email"
                                class="w-full p-3 bg-zinc-800 text-white placeholder-gray-500 border-b-2 border-red-600 focus:outline-none focus:border-red-400"
                                required
                            />
                        </div>
                        <div>
                            <textarea
                                placeholder="Tin nhắn"
                                rows="4"
                                class="w-full p-3 bg-zinc-800 text-white placeholder-gray-500 border-b-2 border-red-600 focus:outline-none focus:border-red-400"
                                required></textarea>
                        </div>
                        <button
                            type="submit"
                            class="bg-red-600 text-black font-bold py-3 px-8 rounded-none hover:bg-red-700 transition-colors duration-300"
                            >GỬI</button
                        >
                    </form>
                </div>
                <div class="mt-12 flex justify-center space-x-6">
                    <a
                        href="#"
                        class="text-gray-400 hover:text-red-600 transition-colors duration-300"
                    >
                        <Icon name="mdi:facebook" class="w-8 h-8" />
                    </a>
                    <a
                        href="#"
                        class="text-gray-400 hover:text-red-600 transition-colors duration-300"
                    >
                        <Icon name="mdi:instagram" class="w-8 h-8" />
                    </a>
                    <a
                        href="#"
                        class="text-gray-400 hover:text-red-600 transition-colors duration-300"
                    >
                        <Icon name="mdi:twitter" class="w-8 h-8" />
                    </a>
                </div>
            </div>
        </section>

        <footer class="bg-black py-8 border-t border-red-600">
            <div class="container mx-auto px-4">
                <div class="flex flex-wrap justify-between items-center">
                    <div class="w-full md:w-1/3 mb-6 md:mb-0">
                        <h3 class="text-2xl font-bold text-red-600 mb-2">
                            ROTA GYM
                        </h3>
                        <p>Nâng cao sức mạnh và nhân cách của bạn</p>
                    </div>
                    <div class="w-full md:w-1/3 mb-6 md:mb-0">
                        <h4 class="text-xl font-bold text-red-600 mb-4">
                            LIÊN KẾT NHANH
                        </h4>
                        <ul class="space-y-2">
                            <li>
                                <a
                                    href="#about"
                                    class="hover:text-red-600 transition-colors duration-300"
                                    >Về chúng tôi</a>
                            </li>
                            <li>
                                <a
                                    href="#services"
                                    class="hover:text-red-600 transition-colors duration-300"
                                    >Dịch vụ</a>
                            </li>
                            <li>
                                <a
                                    href="#pricing"
                                    class="hover:text-red-600 transition-colors duration-300"
                                    >Giá cả</a>
                            </li>
                            <li>
                                <a
                                    href="#contact"
                                    class="hover:text-red-600 transition-colors duration-300"
                                    >Liên hệ</a>
                            </li>
                        </ul>
                    </div>
                    <div class="w-full md:w-1/3">
                        <h4 class="text-xl font-bold text-red-600 mb-4">
                            THÔNG TIN LIÊN HỆ
                        </h4>
                        <p class="flex items-center mb-2">
                            <Icon
                                name="mdi:map-marker"
                                class="w-5 h-5 mr-2 text-red-600"
                            />
                            123 Đường Fitness, Thành phố 123 45
                        </p>
                        <p class="flex items-center mb-2">
                            <Icon
                                name="mdi:phone"
                                class="w-5 h-5 mr-2 text-red-600"
                            />
                            +84 123 456 789
                        </p>
                        <p class="flex items-center">
                            <Icon
                                name="mdi:email"
                                class="w-5 h-5 mr-2 text-red-600"
                            />
                            info@rotagym.vn
                        </p>
                    </div>
                </div>
                <div class="border-t border-gray-800 mt-8 pt-8 text-center">
                    <p>&copy; 2024 ROTA GYM. TẤT CẢ CÁC QUYỀN ĐƯỢC BẢO LƯU.</p>
                </div>
            </div>
        </footer>
    </main>
</Layout>

<style>
    .glitch {
        position: relative;
    }
    .glitch::before,
    .glitch::after {
        content: attr(data-text);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .glitch::before {
        left: 2px;
        text-shadow: -2px 0 #ff00c1;
        clip: rect(24px, 550px, 90px, 0);
        animation: glitch-anim-2 3s infinite linear alternate-reverse;
    }
    .glitch::after {
        left: -2px;
        text-shadow:
            -2px 0 #00fff9,
            2px 2px #ff00c1;
        animation: glitch-anim 2.5s infinite linear alternate-reverse;
    }
    @keyframes glitch-anim {
        0% {
            clip: rect(55px, 9999px, 56px, 0);
        }
        5% {
            clip: rect(92px, 9999px, 72px, 0);
        }
        10% {
            clip: rect(42px, 9999px, 35px, 0);
        }
        15% {
            clip: rect(94px, 9999px, 9px, 0);
        }
        20% {
            clip: rect(39px, 9999px, 52px, 0);
        }
        25% {
            clip: rect(82px, 9999px, 94px, 0);
        }
        30% {
            clip: rect(55px, 9999px, 57px, 0);
        }
        35% {
            clip: rect(14px, 9999px, 46px, 0);
        }
        40% {
            clip: rect(21px, 9999px, 16px, 0);
        }
        45% {
            clip: rect(20px, 9999px, 93px, 0);
        }
        50% {
            clip: rect(94px, 9999px, 84px, 0);
        }
        55% {
            clip: rect(44px, 9999px, 26px, 0);
        }
        60% {
            clip: rect(2px, 9999px, 54px, 0);
        }
        65% {
            clip: rect(23px, 9999px, 6px, 0);
        }
        70% {
            clip: rect(39px, 9999px, 30px, 0);
        }
        75% {
            clip: rect(64px, 9999px, 39px, 0);
        }
        80% {
            clip: rect(12px, 9999px, 79px, 0);
        }
        85% {
            clip: rect(68px, 9999px, 41px, 0);
        }
        90% {
            clip: rect(49px, 9999px, 81px, 0);
        }
        95% {
            clip: rect(11px, 9999px, 21px, 0);
        }
        100% {
            clip: rect(59px, 9999px, 90px, 0);
        }
    }

    .typewriter {
        overflow: hidden;
        border-right: 0.15em solid #dc2626;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: 0.15em;
        animation:
            typing 3.5s steps(40, end),
            blink-caret 0.75s step-end infinite;
    }

    @keyframes typing {
        from {
            width: 0;
        }
        to {
            width: 100%;
        }
    }

    @keyframes blink-caret {
        from,
        to {
            border-color: transparent;
        }
        50% {
            border-color: #dc2626;
        }
    }
</style>

<script>
    document.addEventListener("DOMContentLoaded", (event) => {
        const menuToggle = document.getElementById("menu-toggle");
        const mobileMenu = document.getElementById("mobile-menu");
        if (menuToggle && mobileMenu) {
            menuToggle.addEventListener("click", () => {
                mobileMenu.classList.toggle("hidden");
            });
        }

        // Plynulé scrollování pro navigační odkazy
        document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
            anchor.addEventListener("click", (e: Event) => {
                e.preventDefault();
                const href = (
                    e.currentTarget as HTMLAnchorElement
                ).getAttribute("href");
                if (href) {
                    document.querySelector(href)?.scrollIntoView({
                        behavior: "smooth",
                    });
                }
            });
        });
    });
</script>


==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\pages\example4.astro
==================================================
---
import Layout from "../layouts/Layout.astro";
import { Icon } from "astro-icon/components";
---

<Layout title="Rota Gym - Sạch sẽ và hiện đại">
    <main class="bg-white text-gray-800 min-h-screen font-sans">
        <header class="bg-white shadow-md p-4 sticky top-0 z-50">
            <div class="container mx-auto flex justify-between items-center">
                <h1 class="text-3xl font-bold text-teal-600">Rota Gym</h1>
                <nav class="hidden md:flex space-x-6">
                    <a href="#about" class="hover:text-teal-600 transition-colors duration-300">Về chúng tôi</a>
                    <a href="#services" class="hover:text-teal-600 transition-colors duration-300">Dịch vụ</a>
                    <a href="#pricing" class="hover:text-teal-600 transition-colors duration-300">Bảng giá</a>
                    <a href="#gallery" class="hover:text-teal-600 transition-colors duration-300">Thư viện ảnh</a>
                    <a href="#contact" class="hover:text-teal-600 transition-colors duration-300">Liên hệ</a>
                </nav>
                <button id="menu-toggle" class="md:hidden text-gray-800">
                    <Icon name="mdi:menu" class="w-6 h-6" />
                </button>
            </div>
            <nav id="mobile-menu" class="hidden mt-4 md:hidden">
                <a href="#about" class="block py-2 hover:text-teal-600 transition-colors duration-300">Về chúng tôi</a>
                <a href="#services" class="block py-2 hover:text-teal-600 transition-colors duration-300">Dịch vụ</a>
                <a href="#pricing" class="block py-2 hover:text-teal-600 transition-colors duration-300">Bảng giá</a>
                <a href="#gallery" class="block py-2 hover:text-teal-600 transition-colors duration-300">Thư viện ảnh</a>
                <a href="#contact" class="block py-2 hover:text-teal-600 transition-colors duration-300">Liên hệ</a>
            </nav>
        </header>

        <section id="hero" class="py-20 bg-teal-50">
            <div class="container mx-auto text-center px-4">
                <h2 class="text-5xl md:text-7xl font-bold mb-8 text-teal-800">
                    Khám phá sức mạnh của bạn
                </h2>
                <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto text-gray-600">
                    Chào mừng đến với Rota Gym, nơi mỗi buổi tập là một bước tiến tới
                    một bạn tốt hơn. Hãy tham gia cùng chúng tôi và biến đổi cơ thể và
                    tâm trí của bạn.
                </p>
                <a href="#services" class="bg-teal-600 text-white font-bold py-3 px-8 rounded-full hover:bg-teal-700 transition-colors duration-300 inline-flex items-center group">
                    Bắt đầu hành trình của bạn
                    <Icon
                        name="mdi:arrow-right"
                        class="w-5 h-5 ml-2 transform group-hover:translate-x-1 transition-transform duration-300"
                    />
                </a>
            </div>
        </section>

        <section id="services" class="py-20">
            <div class="container mx-auto px-4">
                <h2 class="text-4xl md:text-5xl font-bold mb-12 text-center text-teal-800">
                    Dịch vụ của chúng tôi
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                        <Icon name="mdi:dumbbell" class="w-16 h-16 mb-4 text-teal-600 mx-auto" />
                        <h3 class="text-2xl font-bold mb-4 text-center">Huấn luyện cá nhân</h3>
                        <p class="text-center text-gray-600">
                            Chương trình cá nhân hóa theo mục tiêu và nhu cầu của bạn.
                        </p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                        <Icon name="mdi:account-group" class="w-16 h-16 mb-4 text-teal-600 mx-auto" />
                        <h3 class="text-2xl font-bold mb-4 text-center">Lớp học nhóm</h3>
                        <p class="text-center text-gray-600">
                            Các lớp học năng động cho mọi cấp độ thể chất.
                        </p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                        <Icon name="mdi:yoga" class="w-16 h-16 mb-4 text-teal-600 mx-auto" />
                        <h3 class="text-2xl font-bold mb-4 text-center">Yoga và sức khỏe</h3>
                        <p class="text-center text-gray-600">
                            Bài tập thư giãn và tăng cường cho cơ thể và tâm trí.
                        </p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                        <Icon name="mdi:nutrition" class="w-16 h-16 mb-4 text-teal-600 mx-auto" />
                        <h3 class="text-2xl font-bold mb-4 text-center">Tư vấn dinh dưỡng</h3>
                        <p class="text-center text-gray-600">
                            Kế hoạch ăn uống cá nhân hóa để đạt kết quả tối ưu.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section id="pricing" class="py-20 bg-teal-50">
            <div class="container mx-auto px-4">
                <h2 class="text-4xl md:text-5xl font-bold mb-12 text-center text-teal-800">
                    Bảng giá
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-white p-8 rounded-lg shadow-lg">
                        <h3 class="text-2xl font-bold mb-4 text-center">Cơ bản</h3>
                        <p class="text-4xl font-bold text-teal-600 mb-6 text-center">
                            500.000 VNĐ / tháng
                        </p>
                        <ul class="mb-8 space-y-2">
                            <li class="flex items-center">
                                <Icon name="mdi:check-circle" class="w-5 h-5 mr-2 text-teal-600" />
                                Truy cập không giới hạn vào phòng tập
                            </li>
                            <li class="flex items-center">
                                <Icon name="mdi:check-circle" class="w-5 h-5 mr-2 text-teal-600" />
                                Thiết bị cơ bản
                            </li>
                        </ul>
                        <a href="#contact" class="block text-center bg-teal-600 text-white font-bold py-2 px-6 rounded-full hover:bg-teal-700 transition-colors duration-300">Chọn gói</a>
                    </div>
                    <div class="bg-white p-8 rounded-lg shadow-lg transform scale-105">
                        <h3 class="text-2xl font-bold mb-4 text-center">Cao cấp</h3>
                        <p class="text-4xl font-bold text-teal-600 mb-6 text-center">
                            1.000.000 VNĐ / tháng
                        </p>
                        <ul class="mb-8 space-y-2">
                            <li class="flex items-center">
                                <Icon name="mdi:check-circle" class="w-5 h-5 mr-2 text-teal-600" />
                                Tất cả các tính năng của gói Cơ bản
                            </li>
                            <li class="flex items-center">
                                <Icon name="mdi:check-circle" class="w-5 h-5 mr-2 text-teal-600" />
                                Lớp học nhóm miễn phí
                            </li>
                            <li class="flex items-center">
                                <Icon name="mdi:check-circle" class="w-5 h-5 mr-2 text-teal-600" />
                                1 buổi huấn luyện cá nhân mỗi tháng
                            </li>
                        </ul>
                        <a href="#contact" class="block text-center bg-teal-600 text-white font-bold py-2 px-6 rounded-full hover:bg-teal-700 transition-colors duration-300">Chọn gói</a>
                    </div>
                    <div class="bg-white p-8 rounded-lg shadow-lg">
                        <h3 class="text-2xl font-bold mb-4 text-center">VIP</h3>
                        <p class="text-4xl font-bold text-teal-600 mb-6 text-center">
                            2.000.000 VNĐ / tháng
                        </p>
                        <ul class="mb-8 space-y-2">
                            <li class="flex items-center">
                                <Icon name="mdi:check-circle" class="w-5 h-5 mr-2 text-teal-600" />
                                Tất cả các tính năng của gói Cao cấp
                            </li>
                            <li class="flex items-center">
                                <Icon name="mdi:check-circle" class="w-5 h-5 mr-2 text-teal-600" />
                                Huấn luyện cá nhân không giới hạn
                            </li>
                            <li class="flex items-center">
                                <Icon name="mdi:check-circle" class="w-5 h-5 mr-2 text-teal-600" />
                                Tư vấn dinh dưỡng
                            </li>
                        </ul>
                        <a href="#contact" class="block text-center bg-teal-600 text-white font-bold py-2 px-6 rounded-full hover:bg-teal-700 transition-colors duration-300">Chọn gói</a>
                    </div>
                </div>
            </div>
        </section>

        <section id="gallery" class="py-20">
            <div class="container mx-auto px-4">
                <h2 class="text-4xl md:text-5xl font-bold mb-12 text-center text-teal-800">
                    Thư viện ảnh
                </h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Thiết bị phòng gym"
                        class="w-full h-64 object-cover rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Lớp yoga"
                        class="w-full h-64 object-cover rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Huấn luyện cá nhân"
                        class="w-full h-64 object-cover rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300"
                    />
                    <img
                        src="https://via.placeholder.com/300x300"
                        alt="Tập luyện nhóm"
                        class="w-full h-64 object-cover rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300"
                    />
                </div>
            </div>
        </section>

        <section id="contact" class="py-20 bg-teal-50">
            <div class="container mx-auto text-center px-4">
                <h2 class="text-4xl md:text-5xl font-bold mb-12 text-teal-800">
                    Liên hệ với chúng tôi
                </h2>
                <div class="max-w-3xl mx-auto bg-white p-8 rounded-lg shadow-lg">
                    <form class="space-y-6">
                        <div>
                            <input
                                type="text"
                                placeholder="Tên của bạn"
                                class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-teal-400"
                                required
                            />
                        </div>
                        <div>
                            <input
                                type="email"
                                placeholder="Email của bạn"
                                class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-teal-400"
                                required
                            />
                        </div>
                        <div>
                            <textarea
                                placeholder="Tin nhắn của bạn"
                                rows="4"
                                class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-teal-400"
                                required
                            ></textarea>
                        </div>
                        <button
                            type="submit"
                            class="bg-teal-600 text-white font-bold py-3 px-8 rounded-full hover:bg-teal-700 transition-colors duration-300"
                        >Gửi</button>
                    </form>
                </div>
                <div class="mt-12 flex justify-center space-x-6"><div class="mt-12 flex justify-center space-x-6">
                    <a href="#" class="text-teal-600 hover:text-teal-800 transition-colors duration-300">
                        <Icon name="mdi:facebook" class="w-8 h-8" />
                    </a>
                    <a href="#" class="text-teal-600 hover:text-teal-800 transition-colors duration-300">
                        <Icon name="mdi:instagram" class="w-8 h-8" />
                    </a>
                    <a href="#" class="text-teal-600 hover:text-teal-800 transition-colors duration-300">
                        <Icon name="mdi:twitter" class="w-8 h-8" />
                    </a>
                </div>
            </div>
        </section>

        <footer class="bg-teal-800 text-white py-8">
            <div class="container mx-auto px-4">
                <div class="flex flex-wrap justify-between items-center">
                    <div class="w-full md:w-1/3 mb-6 md:mb-0">
                        <h3 class="text-2xl font-bold mb-2">Rota Gym</h3>
                        <p>Con đường của bạn đến sức khỏe và thể hình tốt hơn</p>
                    </div>
                    <div class="w-full md:w-1/3 mb-6 md:mb-0">
                        <h4 class="text-xl font-bold mb-4">Liên kết nhanh</h4>
                        <ul class="space-y-2">
                            <li>
                                <a href="#about" class="hover:text-teal-300 transition-colors duration-300">Về chúng tôi</a>
                            </li>
                            <li>
                                <a href="#services" class="hover:text-teal-300 transition-colors duration-300">Dịch vụ</a>
                            </li>
                            <li>
                                <a href="#pricing" class="hover:text-teal-300 transition-colors duration-300">Bảng giá</a>
                            </li>
                            <li>
                                <a href="#contact" class="hover:text-teal-300 transition-colors duration-300">Liên hệ</a>
                            </li>
                        </ul>
                    </div>
                    <div class="w-full md:w-1/3">
                        <h4 class="text-xl font-bold mb-4">Thông tin liên hệ</h4>
                        <p>123 Đường Fitness, Hà Nội</p>
                        <p>Điện thoại: +84 123 456 789</p>
                        <p>Email: info@rotagym.vn</p>
                    </div>
                </div>
                <div class="border-t border-teal-700 mt-8 pt-8 text-center">
                    <p>&copy; 2024 Rota Gym. Tất cả các quyền được bảo lưu.</p>
                </div>
            </div>
        </footer>
    </main>
</Layout>

<script>
    document.addEventListener("DOMContentLoaded", (event) => {
        const menuToggle = document.getElementById("menu-toggle");
        const mobileMenu = document.getElementById("mobile-menu");
        if (menuToggle && mobileMenu) {
            menuToggle.addEventListener("click", () => {
                mobileMenu.classList.toggle("hidden");
            });
        }

        // Plynulé scrollování pro navigační odkazy
        document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
            anchor.addEventListener("click", (e: Event) => {
                e.preventDefault();
                const href = (
                    e.currentTarget as HTMLAnchorElement
                ).getAttribute("href");
                if (href) {
                    document.querySelector(href)?.scrollIntoView({
                        behavior: "smooth",
                    });
                }
            });
        });
    });
</script>

==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\pages\index.astro
==================================================
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Rota Gym - Příklady designu">
    <main class="bg-gray-900 min-h-screen text-white p-8">
        <h1 class="text-4xl font-bold mb-8 text-center">Rota Gym - Příklady designu</h1>
        <nav>
            <ul class="space-y-4">
                <li><a href="/example1" class="text-xl hover:text-yellow-400 transition-colors">Příklad 1: Moderní a minimalistický</a></li>
                <li><a href="/example2" class="text-xl hover:text-yellow-400 transition-colors">Příklad 2: Energický a dynamický</a></li>
                <li><a href="/example3" class="text-xl hover:text-yellow-400 transition-colors">Příklad 3: Industriální a syrový</a></li>
                <li><a href="/example4" class="text-xl hover:text-yellow-400 transition-colors">Příklad 4: Čistý a moderní</a></li>
            </ul>
        </nav>
    </main>
</Layout>

==================================================

Obsah souboru: C:\Users\thanh\Downloads\Programy\rotagym\src\styles\global.css
==================================================
@tailwind base;
@tailwind components;
@tailwind utilities;


==================================================
