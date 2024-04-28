# Importações
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Consultar livros com base nos parâmetros fornecidos
def consultar_livros(parametros, exibir_grafico=False):
    url_base = "https://gutendex.com/books"
    resposta = requests.get(url_base, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()
        if dados["count"] > 0:
            livros_encontrados = []
            for livro in dados["results"]:
                detalhes_livro = f"Título: {livro['title']}\nAutor(es): {', '.join(autor['name'] for autor in livro['authors'])}\nGênero(s): {', '.join(livro['subjects'])}\nNúmero de Downloads: {livro['download_count']}\n"
                livros_encontrados.append(detalhes_livro)
            resultado = "\n".join(livros_encontrados)
            if exibir_grafico:
                exibir_resultado_grafico(resultado)
            else:
                exibir_resultado_texto(resultado)
        else:
            if exibir_grafico:
                exibir_resultado_grafico("Nenhum livro encontrado com esses critérios.")
            else:
                exibir_resultado_texto("Nenhum livro encontrado com esses critérios.")
    else:
        if exibir_grafico:
            exibir_resultado_grafico("Falha ao consultar a API Gutendex.")
        else:
            exibir_resultado_texto("Falha ao consultar a API Gutendex.")

# Exibir os detalhes de um livro em uma janela de texto
def exibir_resultado_texto(resultado):
    messagebox.showinfo("Resultado da Consulta", resultado)

# Exibir os detalhes de um livro em uma janela gráfica
def exibir_resultado_grafico(resultado):
    root = tk.Tk()
    root.title("Resultado da Consulta")

    frame = tk.Frame(root)
    frame.pack()

    label = tk.Label(frame, text=resultado, padx=10, pady=10)
    label.pack()

    root.mainloop()

# Criar um gráfico de barras dos gêneros de livros
def criar_grafico_generos(parametros):
    url_base = "https://gutendex.com/books"
    resposta = requests.get(url_base, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()
        if dados["count"] > 0:
            generos = [genero for livro in dados["results"] for genero in livro["subjects"]]
            generos_counts = pd.Series(generos).value_counts()

            # Criando o gráfico de barras
            plt.figure(figsize=(10, 6))
            sns.barplot(x=generos_counts.values, y=generos_counts.index, palette="viridis")
            plt.title("Distribuição dos Gêneros de Livros")
            plt.xlabel("Número de Livros")
            plt.ylabel("Gênero")
            plt.show()
        else:
            messagebox.showinfo("Resultado do Gráfico", "Nenhum livro encontrado com esses critérios.")
    else:
        messagebox.showinfo("Resultado do Gráfico", "Falha ao consultar a API Gutendex para criar o gráfico de gêneros.")

# Abrir uma nova janela de consulta com base no tipo de consulta selecionado
def abrir_janela_consulta(tipo_consulta):
    consulta_window = tk.Toplevel()
    consulta_window.title("Consulta")

    if tipo_consulta == "Título":
        label = tk.Label(consulta_window, text="Digite o título do livro (em minúsculas):")
        label.pack()
        entry = tk.Entry(consulta_window)
        entry.pack()
        button = tk.Button(consulta_window, text="Consultar", command=lambda: consultar_livros({"search": entry.get()}))
        button.pack()
    elif tipo_consulta == "Autor":
        label = tk.Label(consulta_window, text="Digite o nome do autor (em minúsculas):")
        label.pack()
        entry = tk.Entry(consulta_window)
        entry.pack()
        button = tk.Button(consulta_window, text="Consultar", command=lambda: consultar_livros({"search": entry.get()}))
        button.pack()
    elif tipo_consulta == "Gênero":
        label = tk.Label(consulta_window, text="Digite o gênero do livro (em minúsculas):")
        label.pack()
        entry = tk.Entry(consulta_window)
        entry.pack()
        button = tk.Button(consulta_window, text="Consultar", command=lambda: consultar_livros({"topic": entry.get()}, exibir_grafico=True))
        button.pack()
    elif tipo_consulta == "Faixa de Datas":
        label1 = tk.Label(consulta_window, text="Ano de início:")
        label1.pack()
        entry1 = tk.Entry(consulta_window)
        entry1.pack()
        label2 = tk.Label(consulta_window, text="Ano de fim:")
        label2.pack()
        entry2 = tk.Entry(consulta_window)
        entry2.pack()
        button = tk.Button(consulta_window, text="Consultar", command=lambda: consultar_livros({"author_year_start": entry1.get(), "author_year_end": entry2.get()}))
        button.pack()

# Menu principal
def menu_grafico():
    root = tk.Tk()
    root.title("Menu")

    button1 = tk.Button(root, text="Consultar pelo Título", command=lambda: abrir_janela_consulta("Título"))
    button1.pack()
    button2 = tk.Button(root, text="Consultar pelo Autor", command=lambda: abrir_janela_consulta("Autor"))
    button2.pack()
    button3 = tk.Button(root, text="Consultar por Gênero", command=lambda: abrir_janela_consulta("Gênero"))
    button3.pack()
    button4 = tk.Button(root, text="Consultar por Faixa de Datas", command=lambda: abrir_janela_consulta("Faixa de Datas"))
    button4.pack()
    button0 = tk.Button(root, text="Sair", command=root.quit)
    button0.pack()

    root.mainloop()

if __name__ == "__main__":
    menu_grafico()
