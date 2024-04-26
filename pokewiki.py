import pandas as pd
import requests

def obter_dados_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        print("Falha ao obter dados da PokeAPI")
        return None

nome_pokemon = input("Digite o nome do Pokémon: ")
dados_pokemon = obter_dados_pokemon(nome_pokemon)

if dados_pokemon:
    tipos = ', '.join([tipo['type']['name'] for tipo in dados_pokemon['types']])
    habilidades = ', '.join([habilidade['ability']['name'] for habilidade in dados_pokemon['abilities']])
    altura = dados_pokemon['height']
    peso = dados_pokemon['weight']
    movimentos = [movimento['move']['name'] for movimento in dados_pokemon['moves']]

    df_tipos = pd.DataFrame({'Nome': [nome_pokemon], 'Tipo': [tipos]})
    df_movimentos = pd.DataFrame({'Nome': [nome_pokemon]*len(movimentos), 'Movimento': movimentos})

    df_pokemon = pd.merge(df_tipos, df_movimentos, on='Nome')

    df_pokemon['Altura'] = altura
    df_pokemon['Peso'] = peso
    df_pokemon['Habilidades'] = habilidades

    print(df_pokemon)
else:
    print("Não foi possível obter os dados do Pokémon.")