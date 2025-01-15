#  Gerador de Carros - Forza Horizon 5

Um projeto simples em Python que utiliza um arquivo CSV como base de dados para sortear carros do **Forza Horizon 5** de maneira personalizada. 

---

## 🛠️ Funcionalidades Técnicas

- 📂 **Manipulação de Dados**: Utiliza a biblioteca pandas para carregar, filtrar e processar os dados de carros a partir de um arquivo CSV.

- 🎯 **Filtros Dinâmicos**: `Os usuários podem aplicar filtros como ano, fabricante, tipo, modelo, raridade, país e valor máximo para refinar a seleção de carros.

- 🎲 **Randomização**: `Os carros são sorteados de forma aleatória com base nos critérios escolhidos pelo usuário.

- 🧑‍💻 **Interatividade**: `O programa aceita entradas do usuário para configurar filtros e especificar se o sorteio será baseado na quantidade de pilotos ou nos nomes dos pilotos.

- 🔄 **Gestão de Dados Restantes:**: `Após cada sorteio, os carros já selecionados são removidos do pool para evitar repetições.

- 🛡️ **Fallback Inteligente:** `Se os filtros aplicados não encontrarem nenhum carro disponível, o programa notifica o usuário e oferece a opção de ajustar os filtros.

- 🖥️ **Interface em Terminal:** `A interação é feita diretamente no terminal, permitindo uma experiência simples e funcional.


##  Features

- **Filtros Personalizados**:
  - 🎯 **Ano**: Exemplo: `2020`.
  - 🏎️ **Fabricante**: Exemplo: `Ferrari`.
  - 🚘 **Grupo/Tipo**: Exemplo: `Supercarros Modernos`.
  - 🔤 **Modelo**: Exemplo: `488 GTB`.
  - 🌍 **País de Origem**: Exemplo: `Itália`.
  - 💎 **Raridade**: Exemplo: `Legendary`.
  - 💰 **Valor Máximo**: Exemplo: `250000`.
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

## 📜 Licenças:
**Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e compartilhar conforme necessário.**

## 📌 Observação
**Este projeto ainda está em processo de adaptação para o português e pode conter informações em inglês.**

## 🏷️ Versão
**Versão do Projeto: 1.11**

---

## 💡 Atualizações Futuras

- Implementar uma interface gráfica (GUI) para facilitar a interação com o programa. (Atualizações Futuras)
- Implementar em um sistema operacional Android & IOS, interativo. (Revisão)
- Adicionar estatísticas detalhadas sobre os carros sorteados (e.g., média de valores, tipos mais sorteados). (Revisão)
- Incluir uma opção de modo multiplayer, onde os usuários podem competir com base nos carros sorteados. (Revisão)
- Melhorar o desempenho da filtragem em datasets muito grandes. (Em Andamento)
- Traduzir o programa completamente para português. (Em Andamento)
- Criar uma API REST para acessar os dados e realizar sorteios online. (Revisão)
- Usar um dataset existente para consumir as informações sem precisar de um arquivo df local. (Em Andamento)

---

## 🧰 Instalação
Instale as dependências:
```bash
pip install -r requirements.txt
