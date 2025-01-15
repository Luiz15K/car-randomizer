import simple_mode
import advanced_mode

if __name__ == "__main__":
    print("============================================")
    print("        Gerador de Rolezinhos - FH5")
    print("============================================\n")

    escolha = input("Escolha o modo: 'Simples' ou 'Avançado' (Digite 's' para Simples ou 'a' para Avançado): ").strip().lower()

    if escolha == 's':
        simple_mode.run()
    elif escolha == 'a':
        advanced_mode.modo_avancado()  # Atualizado para chamar a função correta
    else:
        print("\nOpção inválida! Encerrando o programa.")
