import pandas as pd
import random

# Carregar o arquivo CSV
df = pd.read_csv('cars_db.csv')

def randomizar_carro(carros_disponiveis, ano=None, fabricante=None, grupo=None, modelo=None):
    carros_filtrados = carros_disponiveis

    if ano:
        carros_filtrados = carros_filtrados[carros_filtrados['Ano'].astype(str) == str(ano)]
    if fabricante:
        carros_filtrados = carros_filtrados[carros_filtrados['Fabricante'].str.contains(fabricante, case=False, na=False)]
    if grupo:
        carros_filtrados = carros_filtrados[carros_filtrados['Grupo'].str.contains(grupo, case=False, na=False)]
    if modelo:
        carros_filtrados = carros_filtrados[carros_filtrados['Modelo'].str.contains(modelo, case=False, na=False)]

    if carros_filtrados.empty:
        print("\nNenhum carro encontrado com os filtros aplicados. Randomizando qualquer carro!")
        carro = carros_disponiveis.sample(n=1).iloc[0]
    else:
        carro = carros_filtrados.sample(n=1).iloc[0]

    return carro

if __name__ == "__main__":
    print("============================================")
    print("        Gerador de Rolezinhos - FH5")
    print("============================================\n")

    # Mostrar opções únicas disponíveis para o filtro "Grupo"
    grupos_disponiveis = df['Grupo'].dropna().unique()
    print("Grupos disponíveis para filtro:")
    for grupo in grupos_disponiveis:
        print(f"- {grupo}")

    # Entrada de filtros
    print("\nEscolha filtros para o sorteio. Deixe vazio para incluir todos.\n")
    ano_usuario = input("Digite o ano do carro (ou ENTER para incluir todos): ").strip()
    fabricante_usuario = input("Digite o fabricante do carro (ou ENTER para incluir todos): ").strip()
    grupo_usuario = input("Digite o grupo/tipo do carro (ou ENTER para incluir todos): ").strip()
    modelo_usuario = input("Digite o modelo do carro (ou ENTER para incluir todos): ").strip()

    # Escolha do modo de sorteio
    escolha = input("\nDeseja sortear carros por quantidade de pilotos ou por nomes? (Digite 'quantidade' ou 'nomes'): ").strip().lower()

    carros_disponiveis = df.copy()

    if escolha == "quantidade":
        try:
            num_pilotos = int(input("\nQuantos pilotos estarão no rolê? (Digite um número inteiro): "))
        except ValueError:
            print("\nEntrada inválida! O número de pilotos será definido como 1 por padrão.\n")
            num_pilotos = 1

        print(f"\nRandomizando carros para {num_pilotos} pilotos...\n")
        resultados = []

        for _ in range(num_pilotos):
            carro = randomizar_carro(carros_disponiveis, ano_usuario, fabricante_usuario, grupo_usuario, modelo_usuario)
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
    elif escolha == "nomes":
        nomes_pilotos = input("\nDigite os nomes dos pilotos (separe por vírgulas): ").split(',')
        nomes_pilotos = [nome.strip() for nome in nomes_pilotos]

        print(f"\nRandomizando carros para os pilotos: {', '.join(nomes_pilotos)}...\n")
        resultados = {}

        for nome in nomes_pilotos:
            carro = randomizar_carro(carros_disponiveis, ano_usuario, fabricante_usuario, grupo_usuario, modelo_usuario)
            resultados[nome] = carro
            carros_disponiveis = carros_disponiveis[carros_disponiveis['Fabricante'] != carro['Fabricante']]

        print("============================================")
        print("          Carros escolhidos:")
        print("============================================\n")
        for nome, carro in resultados.items():
            print(f"Piloto: {nome}")
            print(f"  Ano: {carro['Ano']}")
            print(f"  Fabricante: {carro['Fabricante']}")
            print(f"  Grupo: {carro['Grupo']}")
            print(f"  Modelo: {carro['Modelo']}")
            print("--------------------------------------------")
    else:
        print("\nOpção inválida! Encerrando o programa.")
