import pandas as pd
import random

df = pd.read_csv('carros_db.csv')

def randomizar_carro(ano=None, fabricante=None, grupo=None, modelo=None):
    carros_filtrados = df
    if ano:
        carros_filtrados = carros_filtrados[carros_filtrados['Ano'].astype(str).str.contains(ano, case=False, na=False)]
    if fabricante:
        carros_filtrados = carros_filtrados[carros_filtrados['Fabricante'].str.contains(fabricante, case=False, na=False)]
    if grupo:
        carros_filtrados = carros_filtrados[carros_filtrados['Grupo'].str.contains(grupo, case=False, na=False)]
    if modelo:
        carros_filtrados = carros_filtrados[carros_filtrados['Modelo'].str.contains(modelo, case=False, na=False)]

    if carros_filtrados.empty:
        print("\nNenhum carro encontrado com os filtros aplicados. Randomizando qualquer carro!")
        carro = df.sample(n=1).iloc[0]
    else:
        carro = carros_filtrados.sample(n=1).iloc[0]

    return {
        "Ano": carro['Ano'],
        "Fabricante": carro['Fabricante'],
        "Grupo": carro['Grupo'],
        "Modelo": carro['Modelo'],
    }

if __name__ == "__main__":
    print("============================================")
    print("        Gerador de Rolezinhos - FH5")
    print("============================================\n")

    print("Escolha filtros para o sorteio. Deixe vazio para incluir todos.\n")

    ano_usuario = input("Digite o ano do carro (ou ENTER para incluir todos): ").strip()
    fabricante_usuario = input("Digite o fabricante do carro (ou ENTER para incluir todos): ").strip()
    grupo_usuario = input("Digite o grupo/tipo do carro (ou ENTER para incluir todos): ").strip()
    modelo_usuario = input("Digite o modelo do carro (ou ENTER para incluir todos): ").strip()

    escolha = input("\nDeseja sortear carros por quantidade de pilotos ou por nomes? (Digite 'quantidade' ou 'nomes'): ").strip().lower()

    if escolha == "quantidade":
        try:
            num_pilotos = int(input("\nQuantos pilotos estarão no rolê? (Digite um número inteiro): "))
        except ValueError:
            print("\nEntrada inválida! O número de pilotos será definido como 1 por padrão.\n")
            num_pilotos = 1

        print(f"\nRandomizando carros para {num_pilotos} pilotos...\n")
        resultados = [randomizar_carro(ano_usuario, fabricante_usuario, grupo_usuario, modelo_usuario) for _ in range(num_pilotos)]

        print("============================================")
        print("          Carros escolhidos:")
        print("============================================\n")
        for i, resultado in enumerate(resultados, 1):
            print(f"Piloto {i}:")
            for key, value in resultado.items():
                print(f"  {key}: {value}")
            print("--------------------------------------------")
    elif escolha == "nomes":
        nomes_pilotos = input("\nDigite os nomes dos pilotos (separe por vírgulas): ").split(',')
        nomes_pilotos = [nome.strip() for nome in nomes_pilotos]

        print(f"\nRandomizando carros para os pilotos: {', '.join(nomes_pilotos)}...\n")
        resultados = {nome: randomizar_carro(ano_usuario, fabricante_usuario, grupo_usuario, modelo_usuario) for nome in nomes_pilotos}

        print("============================================")
        print("          Carros escolhidos:")
        print("============================================\n")
        for nome, resultado in resultados.items():
            print(f"Piloto: {nome}")
            for key, value in resultado.items():
                print(f"  {key}: {value}")
            print("--------------------------------------------")
    else:
        print("\nOpção inválida! Encerrando o programa.")
