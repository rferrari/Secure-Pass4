import unittest
from secure_pass4.crypt_pass4.crypto_pass import criptografar_senha, descriptografar_senha
from secure_pass4.save_pass4.save_pass import salvar_senha, carregar_senhas
from secure_pass4.secure_pass4 import gerar_senha, avaliar_forca

class TestSecurePass4(unittest.TestCase):
    def setUp(self):
        """Executado antes de cada teste."""
        self.senha = "MinhaSenha123$egura"
        self.senha_fraca = "123456"
        self.senha_criptografada = criptografar_senha(self.senha)
        self.senha_fraca_cripto = criptografar_senha(self.senha_fraca)

    def test_criptografar_senha(self):
        """Teste para verificar a criptografia da senha."""
        resultado = criptografar_senha(self.senha)
        #print(resultado)
        self.assertNotEqual(resultado, self.senha, "A senha criptografada deve ser diferente da senha original.")

        resultado = descriptografar_senha(resultado)
        #print(resultado)
        self.assertEqual(resultado, self.senha, "A senha criptografada deve ser igual aa senha original.")
        

    def test_descriptografar_senha(self):
        """Teste para verificar a descriptografia da senha."""
        # test strong passWW
        resultado = descriptografar_senha(self.senha_criptografada)
        #print(resultado)
        self.assertEqual(resultado, self.senha, "A senha criptografada deve ser igual a senha original.")
        
        # test week pass
        resultado = descriptografar_senha(self.senha_fraca_cripto)
        #print(resultado)
        self.assertEqual(resultado, self.senha_fraca, "A senha criptografada deve ser igual a senha original.")



if __name__ == "__main__":
    unittest.main()
