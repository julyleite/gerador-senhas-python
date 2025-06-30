import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
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
        return "Você precisa escolher pelo menos um tipo de caractere."

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("=== Gerador de Senhas ===")
tamanho = int(input("Informe o tamanho da senha: "))
usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

senha_gerada = gerar_senha(
    tamanho=tamanho,
    usar_maiusculas=usar_maiusculas,
    usar_minusculas=usar_minusculas,
    usar_numeros=usar_numeros,
    usar_simbolos=usar_simbolos
)

print("\nSenha gerada:", senha_gerada)
