import logging
from core.app import App
from utils.config import Config
from utils.logger import setup_logger
from utils.repository import update_repository_map  # Upravený import

async def main():
    # Nastavení konfigurace
    config = Config()
    
    # Nastavení loggeru
    setup_logger(config.log_level)
    
    # Aktualizace repository mapy
    await update_repository_map(config)
    
    # Vytvoření a spuštění aplikace
    app = App(config)
    app.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

