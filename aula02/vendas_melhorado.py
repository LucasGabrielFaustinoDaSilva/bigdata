import pandas as pd  # Importação da biblioteca Pandas para análise de dados

# Dicionário contendo dados de produtos de e-commerce
dados = {
    "produto": ["Notebook", "Celular", "Tablet"],  # Nomes dos produtos
    "preco": [3500, 1500, 1200],  # Preços unitários dos produtos
    "quantidade": [3, 10, 5]  # Quantidades vendidas de cada produto
}

# Criação do DataFrame a partir do dicionário
# Um DataFrame é uma estrutura de dados tabular do Pandas (similar a uma planilha Excel)
df = pd.DataFrame(dados)

# Análise exploratória inicial dos dados
print("Dados dos produtos:")  # Título para a saída
print(df)  # Exibe todo o DataFrame
print("\nFormato da planilha (linhas, colunas):", df.shape)  # Mostra a dimensão (3 linhas, 3 colunas)
print("Nomes das colunas:", df.columns.tolist())  # Lista os nomes das colunas disponíveis
print("Tipo de dados de cada coluna:\n", df.dtypes)  # Exibe os tipos de dados (int, float, object)

# Cálculo do valor total de cada venda
# Operação vetorizada (aplicada a toda a coluna de uma vez)
# Multiplica o preço pela quantidade para cada linha do DataFrame
df['valor_total'] = df['preco'] * df['quantidade']

# Exibição dos resultados após o cálculo
print("\nPlanilha com valor total calculado:")
print(df)  # Mostra o DataFrame com a nova coluna 'valor_total'
