import os
from cryptography.fernet import Fernet

def gerar_chave():
    """Gera e salva uma chave para criptografia/descriptografia."""
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

def carregar_chave():
    """Carrega a chave usada para criptografar/descriptografar as senhas."""
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()

def criptografar_senha(senha):
    """Criptografa uma senha."""
    senha_criptografada = ""
    return senha_criptografada

def descriptografar_senha(senha_criptografada):
    """Descriptografa uma senha."""
    senha = ""
    return senha


gerar_chave()
mykey = carregar_chave()
print(mykey)
