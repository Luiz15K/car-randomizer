import pandas as pd
import random

df = pd.read_csv('cars_db.csv')

def randomizar_carro(carros_disponiveis):
    return carros_disponiveis.sample(n=1).iloc[0]

def run():
    print("\n=== Modo Simples ===")
    try:
        num_pilotos = int(input("\nQuantos pilotos estarão no rolê? (Digite um número inteiro): "))
    except ValueError:
        print("\nEntrada inválida! O número de pilotos será definido como 1 por padrão.\n")
        num_pilotos = 1

    print(f"\nRandomizando carros para {num_pilotos} pilotos...\n")
    resultados = []

    carros_disponiveis = df.copy()
    for _ in range(num_pilotos):
        carro = randomizar_carro(carros_disponiveis)
        resultados.append(carro)
        carros_disponiveis = carros_disponiveis[carros_disponiveis['Fabricante'] != carro['Fabricante']]

    print("============================================")
    print("          Carros escolhidos:")
    print("============================================\n")
    for i, carro in enumerate(resultados, 1):
        print(f"Piloto {i}:")
        print(f"  Ano: {carro['Ano']}")
        print(f"  Fabricante: {carro['Fabricante']}")
        print(f"  Grupo: {carro['Grupo']}")
        print(f"  Modelo: {carro['Modelo']}")
        print("--------------------------------------------")
