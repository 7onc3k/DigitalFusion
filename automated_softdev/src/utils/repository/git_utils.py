import asyncio
from typing import List
from utils.logger import get_logger

logger = get_logger(__name__)

async def get_changed_files(project_dir: str) -> List[str]:
    try:
        process = await asyncio.create_subprocess_exec(
            'git', 'diff', '--name-only', 'HEAD^', 'HEAD',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=project_dir
        )
        stdout, stderr = await process.communicate()
        if stderr:
            print(f"Git diff chyba: {stderr.decode()}")
            logger.error(f"Git diff chyba: {stderr.decode()}")
        changed_files = stdout.decode().splitlines()
        print(f"Git diff výstup: {stdout.decode()}")
        logger.info(f"Zjištěno {len(changed_files)} změněných souborů")
        return changed_files
    except Exception as e:
        print(f"Chyba při získávání změněných souborů: {str(e)}")
        logger.error(f"Chyba při získávání změněných souborů: {str(e)}")
        return []
