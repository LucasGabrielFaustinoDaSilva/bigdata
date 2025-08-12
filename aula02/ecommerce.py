import pandas as pd
import numpy as np
from datetime import datetime

#Simulação de dados de uma loja online

np.random.seed(42) #faz os numeros aleatorios serem sempre iguais (util para todos terem o mesmo resultado)
numero_vendas = 10000 #qtd de registros de vendas a serem simulados

print("Criando dados simulados de e-commerce...")

#dados simulados

dados_loja={
  #ids de usuarios de 1 a 1000
  'id_usuario':np.random.randint(1,1001,numero_vendas),

  #ids dos produtos
  'id_produto':np.random.randint(1,501,numero_vendas),

  #opcoes de categoria
  'categoria':np.random.choice(['Eletronicos','Roupas','Livros','Casa','Esportes'], numero_vendas),

  #nos precos usarei distribuição exponencial (mais produtos baratos, menos caros)
  'preco':np.random.exponential(50,numero_vendas),

  'quantidade':np.random.randint(1,5, numero_vendas)
}

#Transforma em dataframe
df_loja = pd.DataFrame(dados_loja)

#Calcular valor total de cada compra
df_loja['valor_total']=df_loja['preco']*df_loja['quantidade']

#mostrar as primeiras 5 linhas
print("Primeiras 5 vendas")
print(f"Colunas:{df_loja.columns.tolist()}")


print("==ANALISES DA LOJA ONLINE===")

#Estatisticas basicas (media, min,max, etc)

print("\nEstatisticas dos preços:")
print(f"Preço médio:R${df_loja['preco'].mean():.2f}")
print(f"Preço mais barato:R${df_loja['preco'].min():.2f}")
print(f"Preço mais caro:R${df_loja['preco'].max():.2f}")

#2. Vendas por categoria

print("\n2. Quantas vendas por categoria:")
vendas_categoria = df_loja['categoria'].value_counts()
print(vendas_categoria)

#3. Receita por categoria (somar valor_total de cada categoria)
print("\n3. Receita total por categoria:")
receita_categoria = df_loja.groupby('categoria')['valor_total'].sum()
print(receita_categoria.round(2))

#4. Ticktes médio por categoria(quanto cada categoria vende em media)
print("\n4. Ticket médio por categoria:")
ticket_medio=df_loja.groupby('categoria')['valor_total'].mean()
print(ticket_medio.round(2))



#Top 5 produtos mais vendidos
print("\n5. Top 5 produtos mais vendidos:")
top_produtos=df_loja['id_produto'].value_counts().head()
print(top_produtos)

import dask.dataframe as dd

print("==TRABALHANDO COM DADOS GRANDES==")

#Converter nosso dataframe pandas para dask
#npatitions=4=dividir os dados em 4 pedaços

df_dask = dd.from_pandas(df_loja, npartitions=4)

print("DataFrame convertido em Dask!")
print(f"Tipo original:{type(df_loja)}")
print(f"Tipo Dask: {type(df_dask)}")

#Calcular receita por categoria com Dask
receita_dask = df_dask.groupby('categoria')['valor_total'].sum()
print(f"Tipos da operação: {type(receita_dask)}")#ainda nao foi executada

#Agora executar a operação
resultado = receita_dask.compute()
print("Receita por categoria(calculada com Dask):")
print(resultado.round(2))

import matplotlib.pyplot as plt

print("==CRIANDO GRÁFICOS==")

#Configurar o tamanho da figura(largura=12,altura=8)
plt.figure(figsize=(12,8))

#Criar 4 graficos numa grade 2x2
#subplot(2,2,1)=grade 2x2, posiçao 1
plt.subplot(2,2,1)
#Grafico de barras: vendas por categoria
vendas_categoria=df_loja['categoria'].value_counts()
plt.bar(vendas_categoria.index, vendas_categoria.values)
plt.title('Número de vendas por Categoria')
plt.xticks(rotation=45)#Girar nomes das categorias

#Grafico 2: Histograma de preços
plt.hist(df_loja['preco'],bins=30,alpha=0.7,color='green')
plt.title('Distribuição dos Preços')
plt.xlabel('Preço(R$)')
plt.ylabel('Quantidade de produtos')

#Grafico 3: Receita por categoria
plt.subplot(2,2,3)
receita_categoria = df_loja.groupby('categoria')['valor_total'].sum()
plt.bar(receita_categoria.index, receita_categoria.values, color='orange')
plt.xticks(rotation=45)

#Grafico 4: Scatter plot(dispersão)- Preço vs Quantidade
plt.subplot(2,2,4)
#Pegar apenas uma amostra para não ficar muito poluido
amostra=df_loja.sample(1000)
plt.scatter(amostra['preco'],amostra['quantidade'],alpha=0.5)
plt.title("Preço vs Quantidade(Amostra)")
plt.xlabel("Preço(R$)")
plt.ylabel("Quantidade")

#Ajustar layout para não sobrepor

plt.tight_layout()
plt.show()

print("Graficos criados! Verifique a janela que abriu")


