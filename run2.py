import sys
import pandas as pd 
from pathlib import Path

base = Path("/opt/archive")

arg = sys.argv[1] if len(sys.argv) > 1 else "2008"

if arg.isdigit():
    filename = f"{arg}_data.csv"
else:
    filename = arg

csv = base / filename
print("verificando arquivo:", csv)
if not csv.exists():
    raise FileNotFoundError(f"Nao encontrei {csv}. Arquivos disponiveis em {base}:\n"
    + "\n".join(f" - {p.name}" for p in sorted(base.glob("*.csv"))))

df= pd.read_csv(csv)
print("Shape: ", df.shape)
print(df.head())