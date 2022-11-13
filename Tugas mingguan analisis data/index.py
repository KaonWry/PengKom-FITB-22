# Import packages
import pandas as p
import numpy as np

# Import csv
inpDf = p.read_csv("data.csv")
# print(inp)

# Terbanyak
print("Provinsi yang paling parah terdampak bencana")
for i in range(1, len(inpDf.columns)-1):
    bruh = (f"{inpDf.columns[i]}")
    province =  inpDf.loc[inpDf[bruh].idxmax(), "Provinsi"]
    amount = inpDf[bruh].max()
    print(f"{bruh} : {province} ({amount} desa)")
print("\n")

# Low 5 banjir
placement = (inpDf.sort_values(["Banjir"], ascending=[1]).head(5))["Provinsi"].tolist()
placement = ", ".join(placement)
print(f"5 provinsi yang paling jarang mengalami banjir : {placement}")

# Bencana terbanyak
maxBruh = inpDf[["Longsor","Banjir","Banjir Bandang","Gempa Bumi","Tsunami","Gelombang Pasang","Angin kencang","Gunung Meletus","Kebakaran Hutan","Kekeringan"]].max().tolist()
i, c = np.where(inpDf == max(maxBruh))
print(f"\n\nBencana yang paling banyak terjadi : {inpDf.columns[c][0]}")

# Bencana tersedikit
minbruh = inpDf[["Longsor","Banjir","Banjir Bandang","Gempa Bumi","Tsunami","Gelombang Pasang","Angin kencang","Gunung Meletus","Kebakaran Hutan","Kekeringan"]].min().tolist()
i, c = np.where(inpDf == min(maxBruh))
print(f"\n\nBencana yang paling sedikit terjadi : {inpDf.columns[c][0]}")
print("\n")

# Terbanyak persen
print("Provinsi yang paling parah terdampak bencana")
for i in range(1, len(inpDf.columns)-1):
    bruh = (f"{inpDf.columns[i]}")
    province =  inpDf.loc[inpDf[bruh].idxmax(), "Provinsi"]
    provinceList = inpDf["Provinsi"].tolist()
    villages = inpDf.sum(numeric_only=True, axis=1).tolist()
    amount = inpDf[bruh].max()
    percentage = amount/villages[provinceList.index(province)]
    print(f"{bruh} : {province} ({percentage:.2%} desa)")
