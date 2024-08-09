import logging
import os
import stat
from core.app import App
from utils.config import Config
from utils.logger import setup_logger
from utils.repository import update_repository_map

def create_pre_push_hook(config):
    hooks_dir = os.path.join(config.project_dir, '.git', 'hooks')
    pre_push_path = os.path.join(hooks_dir, 'pre-push')
    
    if not os.path.exists(pre_push_path):
        logging.info("Vytvářím pre-push hook")
        
        if not os.path.exists(hooks_dir):
            os.makedirs(hooks_dir)
        
        # Použijeme cestu z konfigurace a přidáme k ní cestu k map.py
        map_path = os.path.join(config.project_dir, "automated_softdev", "src", "utils", "repository", "map.py")
        
        # Použijeme dvojité zpětné lomítko pro Windows cesty v shell skriptu
        map_path = map_path.replace("\\", "\\\\")
        
        hook_content = f"""#!/bin/sh

python "{map_path}"

# Pokud skript selže (návratový kód není 0), zabráníme pushu
exit_code=$?
if [ $exit_code -ne 0 ]; then
    echo "Pre-push hook selhal. Push byl zrušen."
    exit 1
fi

exit 0
"""
        
        with open(pre_push_path, 'w') as f:
            f.write(hook_content)
        
        # Nastavení práv pro spuštění
        os.chmod(pre_push_path, os.stat(pre_push_path).st_mode | stat.S_IEXEC)
        
        logging.info(f"Pre-push hook vytvořen: {pre_push_path}")
    else:
        logging.info("Pre-push hook již existuje")

async def main():
    # Nastavení konfigurace
    config = Config()
    
    # Nastavení loggeru
    setup_logger(config.log_level)
    
    # Vytvoření pre-push hooku
    create_pre_push_hook(config)
    
    # Aktualizace repository mapy
    await update_repository_map(config)
    
    # Vytvoření a spuštění aplikace
    app = App(config)
    app.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())