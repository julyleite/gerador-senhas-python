import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha():
    tamanho = int(entry_tamanho.get())
    usar_maiusculas = var_maiuscula.get()
    usar_minusculas = var_minuscula.get()
    usar_numeros = var_numeros.get()
    usar_simbolos = var_simbolos.get()

    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)

root = tk.Tk()
root.title("Gerador de Senhas")

tk.Label(root, text="Tamanho da senha:").grid(row=0, column=0, sticky='w')
entry_tamanho = tk.Entry(root)
entry_tamanho.insert(0, "12")
entry_tamanho.grid(row=0, column=1)

var_maiuscula = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Letras maiúsculas", variable=var_maiuscula).grid(row=1, columnspan=2, sticky='w')

var_minuscula = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Letras minúsculas", variable=var_minuscula).grid(row=2, columnspan=2, sticky='w')

var_numeros = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Números", variable=var_numeros).grid(row=3, columnspan=2, sticky='w')

var_simbolos = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Símbolos", variable=var_simbolos).grid(row=4, columnspan=2, sticky='w')

tk.Button(root, text="Gerar Senha", command=gerar_senha).grid(row=5, columnspan=2, pady=10)

entry_resultado = tk.Entry(root, width=30)
entry_resultado.grid(row=6, columnspan=2, pady=5)

root.mainloop()
