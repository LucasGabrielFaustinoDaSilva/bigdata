import pandas as pd
df = pd.read_csv("clientes.csv")

df_filtrado = df [(df["idade"]>=40) & (df["renda_mensal"] >= 12000)]

print(f"Total de clientes:{len(df)}")
print(f"Clientes filtrados (idade >= 40 e renda >= 12000): {len(df_filtrado)}")

print("\nPrimeiros clientes filtrados")
print(df_filtrado.head())

print("\nMédia de renda mensal dos clientes filtrados:", round(df_filtrado["renda_mensal"].mean (), 2 ))

print("Idade média dos clientes filtrados:", round(df_filtrado["idade"].mean(), 1))