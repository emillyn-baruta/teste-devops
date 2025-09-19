import sys
from pathlib import Path

# Caminho raiz do projeto
ROOT = Path(__file__).resolve().parents[1]

# Se não estiver no sys.path, adiciona
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
