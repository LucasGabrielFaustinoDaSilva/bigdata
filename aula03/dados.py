import csv
import random
from faker import Faker
faker = Faker ('pt-br')

estados = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"

]

with open("clientes.csv", "w", newline="",encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["id", "nome", "idade", "sexo", "estado", "renda_mensal"])

    for i in range(1,1001):
        nome = faker.name()
        idade = random.randint(18,90)
        sexo = random.choice (["M","F"])
        estado = random.choice(estados)
        renda_mensal =  round (random.uniform(1000,20000), 2)

        writer.writerow([i, nome,idade,sexo,estado,renda_mensal])

        print("Arquivo csv criado com sucesso")