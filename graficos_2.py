import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\rosenclei.nunes\Documents\rosenclei.nunes.2\funcionarios.csv")

df_lucro = df[df["lucro"] > 0]


xpoints = df_lucro["nome"]
ypoints = df_lucro["lucro"]

bars = plt.barh(xpoints, ypoints)

plt.bar_label(bars, fmt="%.2f", padding=3)

plt.title("Grafico")
plt.xlabel("Plano X")
plt.ylabel("Plano Y")

plt.show()



