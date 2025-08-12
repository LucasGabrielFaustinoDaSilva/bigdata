import pandas as pd
import numpy as np
from datetime import datetime
# Nota: Idealmente, todos os imports (incluindo dask e matplotlib) deveriam estar aqui no topo

# Configuração inicial
np.random.seed(42)  # Seed fixa para reproduzibilidade - excelente prática!
numero_vendas = 10000  # Tamanho adequado para testes, mas poderia ser aumentado para simular "Big Data"

# Geração de dados simulados (muito bem estruturado)
print("Criando dados simulados de e-commerce...")

dados_loja = {
    'id_usuario': np.random.randint(1, 1001, numero_vendas),  # 1000 usuários únicos
    'id_produto': np.random.randint(1, 501, numero_vendas),   # 500 produtos diferentes
    'categoria': np.random.choice(['Eletronicos','Roupas','Livros','Casa','Esportes'], numero_vendas),
    'preco': np.random.exponential(50, numero_vendas),  # Distribuição exponencial - boa escolha para e-commerce
    'quantidade': np.random.randint(1, 5, numero_vendas)  # Quantidades realistas
}

# Criação do DataFrame Pandas (base para todas análises)
df_loja = pd.DataFrame(dados_loja)

# Cálculo do valor total (operações vetorizadas - ótimo desempenho)
df_loja['valor_total'] = df_loja['preco'] * df_loja['quantidade']

# Análises descritivas (bem organizadas em seções)
print("\n== ANÁLISES DA LOJA ONLINE ===")

# 1. Estatísticas básicas (poderia adicionar mediana e desvio padrão)
print("\nEstatisticas dos preços:")
print(f"Preço médio: R${df_loja['preco'].mean():.2f}")
print(f"Preço mais barato: R${df_loja['preco'].min():.2f}")
print(f"Preço mais caro: R${df_loja['preco'].max():.2f}")

# 2. Vendas por categoria (value_counts é a função ideal)
print("\n2. Quantas vendas por categoria:")
print(df_loja['categoria'].value_counts())  # Poderíamos normalizar para %

# 3. Receita por categoria (groupby + sum - padrão ouro para agregações)
print("\n3. Receita total por categoria:")
print(df_loja.groupby('categoria')['valor_total'].sum().round(2))

# 4. Ticket médio (cálculo correto da média por grupo)
print("\n4. Ticket médio por categoria:")
print(df_loja.groupby('categoria')['valor_total'].mean().round(2))

# 5. Produtos mais vendidos (boa visualização do top 5)
print("\n5. Top 5 produtos mais vendidos:")
print(df_loja['id_produto'].value_counts().head())

# ========= PARTE DE BIG DATA ==========
import dask.dataframe as dd  # Sugestão: mover para o topo com outros imports

print("\n== TRABALHANDO COM DADOS GRANDES ==")

# Conversão para Dask (npartitions=4 é razoável para testes)
df_dask = dd.from_pandas(df_loja, npartitions=4)

# Demonstração de lazy evaluation (excelente para explicar o conceito)
receita_dask = df_dask.groupby('categoria')['valor_total'].sum()
resultado = receita_dask.compute()  # Compute() é o correto (não computed())

# Visualização (bem implementada, mas faltou subplot(2,2,2))
import matplotlib.pyplot as plt  # Sugestão: mover para o topo

plt.figure(figsize=(12,8))

# Gráfico 1: Vendas por categoria (barras verticais são adequadas)
plt.subplot(2,2,1)
vc = df_loja['categoria'].value_counts()
plt.bar(vc.index, vc.values)
plt.title('Vendas por Categoria')
plt.xticks(rotation=45)

# Gráfico 2: Distribuição de preços (30 bins é uma boa quantidade)
plt.subplot(2,2,2)  # Este estava faltando no original!
plt.hist(df_loja['preco'], bins=30, alpha=0.7, color='green')
plt.title('Distribuição de Preços')
plt.xlabel('Preço (R$)')

# Gráfico 3: Receita por categoria (cores diferenciadas)
plt.subplot(2,2,3)
rc = df_loja.groupby('categoria')['valor_total'].sum()
plt.bar(rc.index, rc.values, color='orange')
plt.title('Receita por Categoria')
plt.xticks(rotation=45)

# Gráfico 4: Relação preço-quantidade (amostra reduzida - boa prática)
plt.subplot(2,2,4)
amostra = df_loja.sample(1000)  # Amostragem evita overplotting
plt.scatter(amostra['preco'], amostra['quantidade'], alpha=0.5)
plt.title("Relação Preço x Quantidade")
plt.xlabel("Preço (R$)")

plt.tight_layout()
plt.show()