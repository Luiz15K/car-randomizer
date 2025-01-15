# 🚗 Gerador de Carros - Forza Horizon 5

Um projeto simples em Python para sortear carros do **Forza Horizon 5** de maneira personalizada para rolês entre amigos! 🎮

---

## ✨ Funcionalidades

- **Filtros Personalizados**:
  - 🎯 **Ano**: Exemplo: `2020`.
  - 🏎️ **Fabricante**: Exemplo: `Ferrari`.
  - 🚘 **Grupo/Tipo**: Exemplo: `Supercarros Modernos`.
  - 🔤 **Modelo**: Exemplo: `488 GTB`.
  - **Inclua tudo** ao deixar os filtros vazios.

- **Sorteio Flexível**:
  - Escolha entre sortear por:
    - **Quantidade de Pilotos**: Informe quantos carros quer sortear.
    - **Nomes de Pilotos**: Associe um carro a cada nome.

- **Fallback Inteligente**:
  - Se nenhum carro for encontrado com os filtros aplicados, o programa sorteará um carro aleatório disponível.

---

## 🛠️ Requisitos

- Python 3.7 ou superior.
- Dependência: `pandas`.

---

## 📋 Exemplo de Uso

### Entrada:
```plaintext
Digite o ano do carro (ou ENTER para incluir todos): 2020
Digite o fabricante do carro (ou ENTER para incluir todos): Ferrari
Digite o grupo/tipo do carro (ou ENTER para incluir todos): Supercarros Modernos
Digite o modelo do carro (ou ENTER para incluir todos): 488
Deseja sortear carros por quantidade de pilotos ou por nomes? (Digite 'quantidade' ou 'nomes'): quantidade
Quantos pilotos estarão no rolê? (Digite um número inteiro): 3
