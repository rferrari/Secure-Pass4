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
