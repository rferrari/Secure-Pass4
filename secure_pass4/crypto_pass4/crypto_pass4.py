import os
from cryptography.fernet import Fernet

def gerar_chave():
    """Gera e salva uma chave para criptografia/descriptografia."""
    # attention to do not overwrite chave.key if it exist.
    # rename or delete it before creating a new key
    if not os.path.exists("chave.key"):
        chave = Fernet.generate_key()
        with open("chave.key", "wb") as chave_file:
            chave_file.write(chave)

def carregar_chave():
    """Carrega a chave usada para criptografar/descriptografar as senhas."""
    # return if key not loaded avoing execution error
    if not os.path.exists("chave.key"):
        print("Your chave.key File NOT FOUND. PLEASE RECOVERY IT.")
        return
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()


def criptografar_senha(senha):
    """Criptografa uma senha."""
    chave = carregar_chave()
    fernet = Fernet(chave)
    senha_criptografada = fernet.encrypt(senha.encode())
    return senha_criptografada

def descriptografar_senha(senha_criptografada):
    """Descriptografa uma senha."""
    chave = carregar_chave()
    fernet = Fernet(chave)
    senha = fernet.decrypt(senha_criptografada).decode()
    return senha

#gerar_chave()
#mykey = carregar_chave()
#if(mykey):
#    mykey = mykey.decode('utf-8')  # convert from bytes to string before print b``
#    print(f"{mykey}")

#cyper = criptografar_senha("ABC1234")
#print(cyper)
#print(descriptografar_senha(cyper))
