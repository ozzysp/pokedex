# Pokedex
 Projeto para listagem de pokemons com o uso da API pokeapi utilizando PyQt5

<p align="center">
  <img alt="Layout da aplicação" width="100%" src="./.github/layout.png" />
</p>

## Projeto
Desenvolvimento de um aplicativo desktop para listagem e visualização de pokémons, utilizando a linguagem de programação Python, o framework PyQt5 e a API REST [PokéApi](https://pokeapi.co/).

### Funcionalidades
- [x] **Listagem dos pokémons**: Listar os pokémons com o uso da API REST.
- [x] **Buscar pokémons**: Método para filtrar os pokémons a partir do seu nome.

### Funcionalidades futuras
- [ ] **Selecionar pokémon**: Criar uma página na aplicação com mais detalhes sobre o pokémon escolhido.

- [ ] **Criar seções do pokémons**: Separar as informações do pokémon em três seções: Sobre, Estatísticas, Evoluções.

- [ ] **Seção Sobre**: Dados básicos sobre o pokémon, como altura, peso, fraquezas.

- [ ] **Seção Estatísticas**: Pontos de batalha do pokémon, como vida, ataque, defesa, velocidade, especial ataque e especial defesa.

- [ ] **Seção Evoluções**: Construir a árvore de evolução do pokémon.

### Conceitos abordados

- Consumo de API com o uso do cliente HTTP [HTTPX](https://www.python-httpx.org/)
- Construção de GUI com [PyQt5](https://pypi.org/project/PyQt5/)

## Instalação e execução

Faça um clone desse repositório e acesse o diretório.
```bash
git clone git@github.com:rafatosta/pokedex.git && cd pokedex
```

Instalando as dependências
```bash
pip install -r requirements.txt
```

Executanto aplicação
```bash
python main.py
```

## Agradecimentos

Agradeço ao [Leo Vargas](https://github.com/LeeonardoVargas/pokedex) por colaborar, indiretamente, com a minha falta de criatividade de construção da interface gráfica.  