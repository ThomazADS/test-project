import pandas as pd
from pathlib import Path

csv = Path("/opt/archive/2010_data.csv")

print("Lendo arquivos:", csv)

df = pd.read_csv(csv)

#print("\n primeiras linhas:")
#print(df.head())

#print("\n Informacoes do DataFrame:")
#print(df.info())

#print("\n Estatisticas numericas:")
#print(df.describe())

#print("\n Coluna 'Ticker':")
#print(df["Ticker"].head())

#print("\n Apenaslinhas onde Ticker == 'BRL=X'")
#print(df[df["Ticker"] == "BRL=X"].head())

#print("\n Tickers disponiveis no dataset")
#print(df["Ticker"].unique())

#print("\n Apenas linhas onde Ticker == 'JPY=X")
#print(df[df["Ticker"] == "JPY=X"].head())
#print(df[df["Ticker"] == "JPY=X"].describe())

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# print("\n Tipose das colunas (dtypes)")
# print(df.dtypes)

# print("\n Intervalo de datas disponiveis:")
# print("min:", df["Date"].min(), "| max", df["Date"].max())

# print("\n Datas invalidas (NaT) apos conversao:", df["Date"].isna().sum())

# full_range = pd.date_range(

#     start=df["Date"].min(),
#     end=df["Date"].max(),
#     freq="D"
# )

# unique_dates = df["Date"].unique()

# missing = full_range.difference(unique_dates)

# print("Dias faltando:", len(missing))

# if len(missing) > 0:
#     print("Lista de dias faltando:")
#     print(missing)
# else:
#     print("Nenhum dia faltando!")

# print("\n Selecionando apenas 'Date' e 'Close': ")
# subset = df[["Date", "Close"]]
# print(subset.head())

# print("\n Ordenar por data (crescente):")
# print(df.sort_values("Date").head())

# print("\n Ordenando por fechamento (Close) do maior para o menor:")
# print(df.sort_values("Close").head())

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# tickers = ["JPY=X", "EUR=X"]
# df_cmp = df[df["Ticker"].isin(tickers)].copy()

# df_cmp = df_cmp.sort_values(["Ticker","Date"])

# normed = []

# for t in tickers:
#     sub = df_cmp[df_cmp["Ticker"] == t].copy()
#     sub["Close_norm"] = sub["Close"]/sub["Close"].iloc[0]
#     normed.append(sub[["Date", "Ticker", "Close_norm"]])

# df_norm = pd.concat(normed, ignore_index=True)

# out_dir = Path("/opt/figs")
# out_dir.mkdir(exist_ok=True)

# plt.figure()
# for t in tickers:
#     sub = df_norm[df_norm["Ticker"] == t]
#     plt.plot(sub["Date"], sub["Close_norm"], label = t)
# plt.title("Comparacao normalizada Close - 2010")
# plt.xlabel("Date")
# plt.ylabel("Close normalizado (t0=1.0)")
# plt.legend()
# plt.tight_layout()

# out_file = out_dir / "{Compare_EUR_JPY_normalized_2010.png"
# plt.savefig(out_file, dpi=150)
# print("\n Grafico salvo em:", out_file)

# df_ret = df.sort_values(["Ticker", "Date"]).copy()

# df_ret["Return"] = df_ret.groupby("Ticker")["Close"].pct_change()

# print("\n Amostra de retornos (linhas nao nulas):")
# print(df_ret[df_ret["Return"].notna()].head())

# print("\n Estatisticas dos retornos por Ticker:")
# print(df_ret.groupby("Ticker")["Return"].describe()[["count", "mean", "std","min", "max"]])

# out_dir = Path("/opt/outputs")
# out_dir.mkdir(exist_ok=True)
# out_csv = out_dir / "returns_2010.csv"
# df_ret.to_csv(out_csv, index=False)
# print("\n CSV de retornos salvos em:", out_csv)

# ticker = "EUR=X"
# df_mm = df[df["Ticker"] == ticker].copy()
# df_mm = df_mm.sort_values("Date")

# df_mm["SMA_7"] = df_mm["Close"].rolling(7).mean()
# df_mm["SMA_30"] = df_mm["Close"].rolling(30).mean()

# df_mm["EMA_12"] = df_mm["Close"].ewm(span=12, adjust=False).mean()
# df_mm["EMA_26"] = df_mm["Close"].ewm(span=26, adjust=False).mean()

# print("\n Amostra das medias moveis:")
# print(df_mm[["Date", "Close", "SMA_7", "SMA_30", "EMA_12", "EMA_26" ]].head(20))

# out_dir = Path("/opt/figs")
# out_dir.mkdir(exist_ok=True)

# plt.figure(figsize=(10,5))
# plt.plot(df_mm["Date"], df_mm["Close"], label = "Close", linewidth=1)
# plt.plot(df_mm["Date"], df_mm["SMA_7"], label = "SMA_7", linewidth=1)
# plt.plot(df_mm["Date"], df_mm["SMA_30"], label = "SMA_30", linewidth=1)

# plt.title(f"{ticker} - Close, SMA 7 e SMA 30")
# plt.xlabel("Date")
# plt.ylabel("Close")
# plt.legend()
# plt.tight_layout()

# out_file = out_dir / f"{ticker.replace('=','_')}_SMA_2010.png"
# plt.savefig(out_file, dpi=150)

# print("\n Grafico de medias moveis salvo em:", out_file)

# plt.figure(figsize=(10,5))
# plt.plot(df_mm["Date"], df_mm["Close"], label = "Close", linewidth=1)
# plt.plot(df_mm["Date"], df_mm["EMA_12"], label = "EMA_12", linewidth=1)
# plt.plot(df_mm["Date"], df_mm["EMA_26"], label = "EMA_26", linewidth=1)

# plt.title(f"{ticker} - Close, EMA 12 e EMA 26")
# plt.xlabel("Date")
# plt.ylabel("Close")
# plt.legend()
# plt.tight_layout()

# out_file = out_dir / f"{ticker.replace('=', '_')}_EMA_2010.png"
# plt.savefig(out_file, dpi=150)

# print("\n Grafico de medias exponenciais moveis salvo em:", out_file)

ticker = "EUR=X"
# df_t = df[df["Ticker"] == ticker].sort_values("Date").copy()

# df_t["Return"] = df_t["Close"].pct_change()
# df_t["CumReturn"] = (1.0 + df_t["Return"]).cumprod() - 1.0

# df_t["RollingMax"] = df_t["Close"].cummax()
# df_t["Drawdown"] = df_t["Close"]/df_t["RollingMax"] - 1.0

# out_dir = Path("/opt/figs"); out_dir.mkdir(exist_ok=True)

# plt.figure(figsize=(10,5))
# plt.plot(df_t["Date"], df_t["CumReturn"], label = "Cumulative Return", linewidth=1)
# plt.plot(df_t["Date"], df_t["Drawdown"], label = "Drawdown", linewidth=1)
# plt.title(f"{ticker.replace('=','_')} Cumulative Return and Drawdown")
# plt.xlabel("Date"); plt.ylabel("Acumulado desde o inicio")
# plt.legend(); plt.tight_layout()
# out_file = out_dir / f"{ticker.replace('=', '_')}_Drawdown_2010.png"
# plt.savefig(out_file, dpi=150)

# print("Grafico salvo em:", out_file)
# df_f = df[df["Ticker"] == ticker].copy()

# df_f = df_f.set_index("Date").sort_index()

# df_daily = df_f.resample("D").ffill()

# df_daily["Ticker"] = ticker

# print("\n Amostra da serie diaria preenchida:")
# print(df_daily.head(15))

# out_dir = Path("/opt/outputs"); out_dir.mkdir(exist_ok=True)
# out_csv = out_dir / f"{ticker.replace('=', '_')}_daily_filled_2010.csv"
# df_daily.to_csv(out_csv)
# print("Serie diaria com preenchimento salva em:", out_csv)

# df_pivot = df.pivot(index = "Date", columns = "Ticker", values = "Close")
# df_pivot = df_pivot.dropna(axis=1, how='all')

# corr_matrix = df_pivot.corr()

# print("\n Matriz de correlacao:")
# print(corr_matrix)

# out_dir = Path("/opt/figs"); out_dir.mkdir(exist_ok=True)

# plt.figure(figsize=(8,6))
# plt.imshow(corr_matrix, cmap = "coolwarm", vmin=-1, vmax=1)
# plt.colorbar(label = "correlacao")
# plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation =45)
# plt.yticks(range(len(corr_matrix.index)), corr_matrix.index)
# plt.title("Matriz de Correlacao entre Moedas (Close)")
# plt.tight_layout()

# out_file = out_dir / "Correlation_heatmap.png"
# plt.savefig(out_file, dpi=150)
# print("Heatmap salvo em:", out_file)

