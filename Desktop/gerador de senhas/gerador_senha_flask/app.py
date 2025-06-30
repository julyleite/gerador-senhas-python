from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
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
        return "Selecione pelo menos um tipo de caractere."

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

@app.route('/', methods=['GET', 'POST'])
def index():
    senha = ''
    if request.method == 'POST':
        tamanho = int(request.form.get('tamanho'))
        usar_maiusculas = 'maiusculas' in request.form
        usar_minusculas = 'minusculas' in request.form
        usar_numeros = 'numeros' in request.form
        usar_simbolos = 'simbolos' in request.form

        senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)

    return render_template('index.html', senha=senha)

if __name__ == '__main__':
    app.run(debug=True)
