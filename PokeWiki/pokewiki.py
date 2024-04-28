# Importações
import tkinter as tk
from tkinter import simpledialog, messagebox
import requests
import matplotlib.pyplot as plt

# Função para obter dados de um Pokémon
def get_pokemon_data(identifier):
    url = f"https://pokeapi.co/api/v2/pokemon/{identifier.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Erro", "Falha ao obter dados da PokeAPI")
        return None

# Função para obter fraquezas e fortes de um tipo de Pokémon
def get_weaknesses_and_strengths(pokemon_type):
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weaknesses = [weakness['name'] for weakness in data['damage_relations']['double_damage_from']]
        strengths = [strength['name'] for strength in data['damage_relations']['double_damage_to']]
        return weaknesses, strengths
    else:
        messagebox.showerror("Erro", "Falha ao obter dados da PokeAPI")
        return None, None

# Função para comparar tamanho, peso e tipos de dois Pokémon
def compare_size_weight_types(pokemon1, pokemon2):
    data_pokemon1 = get_pokemon_data(pokemon1)
    data_pokemon2 = get_pokemon_data(pokemon2)

    if data_pokemon1 and data_pokemon2:
        height_pokemon1 = data_pokemon1['height']
        height_pokemon2 = data_pokemon2['height']
        weight_pokemon1 = data_pokemon1['weight']
        weight_pokemon2 = data_pokemon2['weight']

        types_pokemon1 = [t['type']['name'] for t in data_pokemon1['types']]
        types_pokemon2 = [t['type']['name'] for t in data_pokemon2['types']]

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.bar([pokemon1, pokemon2], [height_pokemon1, height_pokemon2], color=['skyblue', 'salmon'])
        plt.title('Comparação de Altura entre Pokémon')
        plt.ylabel('Altura')

        plt.subplot(1, 2, 2)
        plt.bar([pokemon1, pokemon2], [weight_pokemon1, weight_pokemon2], color=['skyblue', 'salmon'])
        plt.title('Comparação de Peso entre Pokémon')
        plt.ylabel('Peso')

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        labels1 = types_pokemon1
        sizes1 = [types_pokemon1.count(t) for t in set(types_pokemon1)]
        plt.pie(sizes1, labels=labels1, autopct='%1.1f%%', colors=plt.cm.tab10.colors)
        plt.title(pokemon1)
        plt.axis('equal')

        plt.subplot(1, 2, 2)
        labels2 = types_pokemon2
        sizes2 = [types_pokemon2.count(t) for t in set(types_pokemon2)]
        plt.pie(sizes2, labels=labels2, autopct='%1.1f%%', colors=plt.cm.tab10.colors)
        plt.title(pokemon2)
        plt.axis('equal')

        plt.show()
    else:
        messagebox.showerror("Erro", "Não foi possível obter os dados de ambos os Pokémon.")

# Função para exibir o menu e processar as opções
def menu(option):
    option = option.lower()  # Convertendo para minúsculas
    if option == '1':
        name = simpledialog.askstring("Obter dados do Pokémon", "Nome do Pokémon (em minúsculo):")
        if name:
            result = get_pokemon_data(name)
            if result:
                types = [t['type']['name'] for t in result['types']]
                messagebox.showinfo("Resultado", f"Nome do Pokémon: {result['name']}\nTipos: {', '.join(types)}")
    elif option == '2':
        pokemon1 = simpledialog.askstring("Comparar Tamanho, Peso e Tipos", "Nome do primeiro Pokémon (em minúsculo):")
        pokemon2 = simpledialog.askstring("Comparar Tamanho, Peso e Tipos", "Nome do segundo Pokémon (em minúsculo):")
        if pokemon1 and pokemon2:
            compare_size_weight_types(pokemon1, pokemon2)
    elif option == '3':
        pokemon_type = simpledialog.askstring("Obter fraquezas e fortes de um tipo de Pokémon", "Tipo do Pokémon (em minúsculo):")
        if pokemon_type:
            weaknesses, strengths = get_weaknesses_and_strengths(pokemon_type)
            if weaknesses:
                messagebox.showinfo("Fraquezas e Fortes", f"Fraquezas do tipo {pokemon_type}: {', '.join(weaknesses)}\nFortes contra: {', '.join(strengths)}")
    elif option == '0':
        root.quit()
    else:
        messagebox.showwarning("Opção inválida", "Escolha uma opção válida.")

# Configurações da interface gráfica
root = tk.Tk()
root.title("PokeWiki")
root.geometry("600x300")

# Botões do menu
btn_obter_dados = tk.Button(root, text="Dados do Pokémon", command=lambda: menu('1'))
btn_obter_dados.pack(side="left", padx=10, pady=10)

btn_comparar_tipos = tk.Button(root, text="Comparar Tamanho, Peso e Tipos", command=lambda: menu('2'))
btn_comparar_tipos.pack(side="left", padx=10, pady=10)

btn_obter_fraquezas = tk.Button(root, text="Fraquezas e Fortes", command=lambda: menu('3'))
btn_obter_fraquezas.pack(side="left", padx=10, pady=10)

btn_sair = tk.Button(root, text="Sair", command=lambda: menu('0'))
btn_sair.pack(side="right", padx=10, pady=10)

root.mainloop()
