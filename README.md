# Gerador de Rolezinhos - Forza Horizon 5

Este é um projeto simples em Python que sorteia carros do jogo **Forza Horizon 5** para um grupo de pilotos. Você pode personalizar o sorteio com base em filtros, como **Ano**, **Fabricante**, **Grupo/Tema**, e **Modelo**, ou deixar tudo aleatório.

## Funcionalidades

- **Filtros Personalizados**:
  - Filtre os carros por:
    - **Ano**: Exemplo: `2020`.
    - **Fabricante**: Exemplo: `Ferrari`.
    - **Grupo** (tipo): Exemplo: `Supercarros Modernos`.
    - **Modelo**: Exemplo: `458 Italia`.
  - Caso nenhum filtro seja especificado, todos os carros estarão incluídos.
  
- **Sorteio por Pilotos**:
  - Escolha o número de pilotos para gerar os carros aleatórios.
  - Associe carros diretamente a nomes de pilotos fornecidos.

- **Fallback Inteligente**:
  - Caso nenhum carro atenda aos filtros, o programa sorteia aleatoriamente um carro qualquer.

## Requisitos

- Python 3.7 ou superior.
- Dependência: `pandas`.

## Como Usar

### 1. Instale as Dependências
Certifique-se de que o `pandas` está instalado:
```bash
pip install pandas
