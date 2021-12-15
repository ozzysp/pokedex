from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# diretório do icone do sistema
WINDOWS_ICON_DIR = str(BASE_DIR.joinpath('assets', 'teste.png'))

print(WINDOWS_ICON_DIR)
