import pandas as pd  

dados = {  
    "produto": ["Notebook", "Celular", "Tablet"],  
    "preco": [3500, 1500, 1200],  
    "quantidade": [3, 10, 5]  
}  
#Ver informações basicas da planilha
df = pd.DataFrame(dados)  
print(df) 
print("Formato da panilha(linhas,colunas)",df.shape)
print("Nomes das colunas", df.columns.tolist())
print("Tipo de dados",df.dtypes)

# Calcular o valor de cada venda
# Multiplica preco x quantidade para cada linha

df['valor_total']=df['preco']*df['quantidade']

print("\nPlanilha com valor total:")
print(df)