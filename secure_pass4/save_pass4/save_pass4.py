import os
from secure_pass4.crypto_pass4.crypto_pass4 import criptografar_senha, descriptografar_senha

def salvar_senha(site, senha):
    """Salva uma senha criptografada para um site em um arquivo de texto."""
    senha_criptografada = criptografar_senha(senha)

    with open("securepass4.safe", "a") as arquivo_senhas:
        arquivo_senhas.write(f"{site}: {senha_criptografada.decode()}\n")

def carregar_senhas():
    """Carrega e descriptografa todas as senhas do arquivo de senhas."""
    if not os.path.exists("securepass4.safe"):
        return "Nenhuma senha salva."

    with open("securepass4.safe", "r") as arquivo_senhas:
        senhas = arquivo_senhas.readlines()

    senhas_descriptografadas = {}
    for linha in senhas:
        site, senha_criptografada = linha.strip().split(": ")
        senha_descriptografada = descriptografar_senha(senha_criptografada.encode())
        senhas_descriptografadas[site] = senha_descriptografada

    return senhas_descriptografadas
