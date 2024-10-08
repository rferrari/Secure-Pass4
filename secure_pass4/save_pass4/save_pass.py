import os
from secure_pass4.crypt_pass4.crypto_pass import criptografar_senha, descriptografar_senha

def salvar_senha(site, senha):
    """Salva uma senha criptografada para um site em um arquivo de texto."""
    senha_criptografada = criptografar_senha(senha)

    with open("securepass4.safe", "a") as arquivo_senhas:
        arquivo_senhas.write(f"{site}: {senha_criptografada.decode()}\n")

def carregar_senhas():
    """Carrega e descriptografa todas as senhas do arquivo de senhas."""
