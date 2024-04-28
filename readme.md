# Projeto de Consulta de Livros e Pokémon

Este projeto consiste em dois scripts Python que utilizam interfaces gráficas (GUI) para interagir com APIs e exibir informações relevantes para o usuário. Um script é responsável por consultar livros na API do **[Gutendex](https://gutendex.com/)** e exibir os resultados em uma interface gráfica, enquanto o outro script consulta informações sobre Pokémon na API da **[PokeAPI](https://pokeapi.co/)** e realiza comparações entre eles.

## Consulta de Livros

O script `consulta_livros.py` permite ao usuário pesquisar livros por título, autor, gênero ou faixa de datas. Ele usa a biblioteca **`tkinter`** para criar uma interface gráfica onde o usuário pode inserir os parâmetros de pesquisa. As consultas são feitas à API do Gutendex usando a biblioteca **`requests`**, e os resultados são exibidos em uma janela de mensagem ou em um gráfico de barras, dependendo da opção selecionada pelo usuário.

### Funcionalidades:

- Consulta de livros por título, autor, gênero ou faixa de datas.
- Exibição dos resultados em uma interface gráfica.


## Consulta de Pokémon

O script `consulta_pokemon.py` permite ao usuário obter informações sobre Pokémon, como tipos, alturas, pesos e fraquezas. Ele também oferece a funcionalidade de comparar dois Pokémon em termos de tamanho, peso e tipos. Assim como o script de consulta de livros, ele utiliza a biblioteca **`tkinter`** para criar uma interface gráfica interativa.

### Funcionalidades:

- Obtenção de dados de um Pokémon específico via nome e ID.
- Comparação de tamanho, peso e tipos de dois Pokémon.
- Obtenção de fraquezas e forças de um tipo de Pokémon.
-  Exibição dos resultados em uma interface gráfica.

## Repositório do GitHub

O código-fonte desses projetos está disponível também em um repositório do GitHub:
[Projetos API Python](https://github.com/ArthurRochaGarcia/Projetos_API_Python)
