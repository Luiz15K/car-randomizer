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

    # Verificar se há carros disponíveis com os filtros aplicados
    if carros_filtrados.empty:
        return None, 0  # Nenhum carro disponível
    return carros_filtrados.sample(n=1).iloc[0], len(carros_filtrados)

def modo_avancado():
    print("=== Modo Avançado ===")
    print("\nEscolha filtros para o sorteio. Deixe vazio para incluir todos.\n")

    while True:
        ano_usuario = input("Digite o ano do carro (ou ENTER para incluir todos): ").strip()
        fabricante_usuario = input("Digite o fabricante do carro (ou ENTER para incluir todos): ").strip()
        grupo_usuario = input("Digite o grupo/tipo do carro (ou ENTER para incluir todos): ").strip()
        modelo_usuario = input("Digite o modelo do carro (ou ENTER para incluir todos): ").strip()

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
                carro, disponiveis = randomizar_carro(carros_disponiveis, ano_usuario, fabricante_usuario, grupo_usuario, modelo_usuario)
                
                # Verificar se não há carros disponíveis
                if disponiveis == 0:
                    print(f"\nNenhum carro encontrado com os filtros aplicados. Carros disponíveis para os filtros: {disponiveis}")
                    continuar = input("Deseja ajustar os filtros? (Digite 'sim' para ajustar ou 'não' para encerrar): ").strip().lower()
                    if continuar == 'sim':
                        break  # Retorna ao início do loop para ajustes
                    else:
                        print("\nEncerrando o programa.")
                        return

                # Adicionar o carro aos resultados e atualizar os carros disponíveis
                resultados.append(carro)
                carros_disponiveis = carros_disponiveis[carros_disponiveis['Fabricante'] != carro['Fabricante']]

            if resultados:
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
            break
        elif escolha == "nomes":
            nomes_pilotos = input("\nDigite os nomes dos pilotos (separe por vírgulas): ").split(',')
            nomes_pilotos = [nome.strip() for nome in nomes_pilotos]

            print(f"\nRandomizando carros para os pilotos: {', '.join(nomes_pilotos)}...\n")
            resultados = {}

            for nome in nomes_pilotos:
                carro, disponiveis = randomizar_carro(carros_disponiveis, ano_usuario, fabricante_usuario, grupo_usuario, modelo_usuario)
                
                # Verificar se não há carros disponíveis
                if disponiveis == 0:
                    print(f"\nNenhum carro encontrado para o piloto {nome} com os filtros aplicados. Carros disponíveis para os filtros: {disponiveis}")
                    continuar = input("Deseja ajustar os filtros? (Digite 'sim' para ajustar ou 'não' para encerrar): ").strip().lower()
                    if continuar == 'sim':
                        break  # Retorna ao início do loop para ajustes
                    else:
                        print("\nEncerrando o programa.")
                        return

                # Adicionar o carro ao resultado do piloto
                resultados[nome] = carro
                carros_disponiveis = carros_disponiveis[carros_disponiveis['Fabricante'] != carro['Fabricante']]

            if resultados:
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
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    modo_avancado()
