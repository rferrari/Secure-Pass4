import string
import secrets

def gerar_senha(comprimento=12, incluir_letras=True, incluir_numeros=True, incluir_simbolos=True):
    """Gera uma senha aleatória de acordo com as preferências do usuário."""
    caracteres = ""
    
    if incluir_letras:
        caracteres += string.ascii_letters  
    if incluir_numeros:
        caracteres += string.digits  
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Nenhum tipo de caractere foi selecionado para gerar a senha.")

    senha = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
    return senha

def avaliar_forca(senha):
    """Avalia a força da senha com base em seu comprimento e complexidade."""
    comprimento = len(senha)
    tem_maiusculas = any(c.isupper() for c in senha)
    tem_minusculas = any(c.islower() for c in senha)
    tem_numeros = any(c.isdigit() for c in senha)
    tem_simbolos = any(c in string.punctuation for c in senha)

    pontuacao = 0

    if comprimento >= 8:
        pontuacao += 1
    if comprimento >= 12:
        pontuacao += 1
    if tem_maiusculas and tem_minusculas:
        pontuacao += 1
    if tem_numeros:
        pontuacao += 1
    if tem_simbolos:
        pontuacao += 1

    if pontuacao >= 4:
        return "Forte"
    elif pontuacao == 3:
        return "Moderada"
    else:
        return "Fraca"
