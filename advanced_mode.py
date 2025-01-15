import pandas as pd
import random

# Carregar o arquivo CSV
df = pd.read_csv('cars_db.csv')

def randomizar_carro(carros_disponiveis, ano=None, fabricante=None, tipo=None, modelo=None, raridade=None, pais=None, valor=None):
    carros_filtrados = carros_disponiveis

    if ano:
        carros_filtrados = carros_filtrados[carros_filtrados['Ano'].astype(str) == str(ano)]
    if fabricante:
        carros_filtrados = carros_filtrados[carros_filtrados['Fabricante'].str.contains(fabricante, case=False, na=False)]
    if tipo:
        carros_filtrados = carros_filtrados[carros_filtrados['Tipo'].str.contains(tipo, case=False, na=False)]
    if modelo:
        carros_filtrados = carros_filtrados[carros_filtrados['Modelo'].str.contains(modelo, case=False, na=False)]
    if raridade:
        carros_filtrados = carros_filtrados[carros_filtrados['Raridade'].str.contains(raridade, case=False, na=False)]
    if pais:
        carros_filtrados = carros_filtrados[carros_filtrados['Pais'].str.contains(pais, case=False, na=False)]
    if valor:
        try:
            valor = float(valor)
            carros_filtrados = carros_filtrados[carros_filtrados['Valor'].astype(float) <= valor]
        except ValueError:
            print("Valor inválido fornecido. Ignorando filtro de valor.")

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
        tipo_usuario = input("Digite o tipo do carro (ou ENTER para incluir todos): ").strip()
        modelo_usuario = input("Digite o modelo do carro (ou ENTER para incluir todos): ").strip()
        raridade_usuario = input("Digite a raridade do carro (ou ENTER para incluir todos): ").strip()
        pais_usuario = input("Digite o país do carro (ou ENTER para incluir todos): ").strip()
        valor_usuario = input("Digite o valor máximo do carro (ou ENTER para incluir todos): ").strip()

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
                carro, disponiveis = randomizar_carro(carros_disponiveis, ano_usuario, fabricante_usuario, tipo_usuario, modelo_usuario, raridade_usuario, pais_usuario, valor_usuario)
                
                if disponiveis == 0:
                    print("\nNenhum carro encontrado com os filtros aplicados.")
                    continuar = input("Deseja ajustar os filtros? (Digite 'sim' para ajustar ou 'não' para encerrar): ").strip().lower()
                    if continuar == 'sim':
                        break
                    else:
                        print("\nEncerrando o programa.")
                        return

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
                    print(f"  Tipo: {carro['Tipo']}")
                    print(f"  Modelo: {carro['Modelo']}")
                    print(f"  Raridade: {carro['Raridade']}")
                    print(f"  País: {carro['Pais']}")
                    print(f"  Valor: {carro['Valor']}")
                    print("--------------------------------------------")
            break
        elif escolha == "nomes":
            nomes_pilotos = input("\nDigite os nomes dos pilotos (separe por vírgulas): ").split(',')
            nomes_pilotos = [nome.strip() for nome in nomes_pilotos]

            print(f"\nRandomizando carros para os pilotos: {', '.join(nomes_pilotos)}...\n")
            resultados = {}

            for nome in nomes_pilotos:
                carro, disponiveis = randomizar_carro(carros_disponiveis, ano_usuario, fabricante_usuario, tipo_usuario, modelo_usuario, raridade_usuario, pais_usuario, valor_usuario)
                
                if disponiveis == 0:
                    print(f"\nNenhum carro encontrado para o piloto {nome} com os filtros aplicados.")
                    continuar = input("Deseja ajustar os filtros? (Digite 'sim' para ajustar ou 'não' para encerrar): ").strip().lower()
                    if continuar == 'sim':
                        break
                    else:
                        print("\nEncerrando o programa.")
                        return

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
                    print(f"  Tipo: {carro['Tipo']}")
                    print(f"  Modelo: {carro['Modelo']}")
                    print(f"  Raridade: {carro['Raridade']}")
                    print(f"  País: {carro['Pais']}")
                    print(f"  Valor: {carro['Valor']}")
                    print("--------------------------------------------")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    modo_avancado()
