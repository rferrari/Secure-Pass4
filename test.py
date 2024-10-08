import unittest

from secure_pass4.secure_pass4 import criptografar_senha, descriptografar_senha

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
        self.assertNotEqual(resultado, self.senha, "A senha criptografada deve ser diferente da senha original.")
        
        resultado = descriptografar_senha(resultado)
        self.assertEqual(resultado, self.senha, "A senha criptografada deve ser igual aa senha original.")
        

    def test_descriptografar_senha(self):
        # test strong passWW
        resultado = descriptografar_senha(self.senha_criptografada)
        self.assertEqual(resultado, self.senha, "A senha criptografada deve ser igual a senha original.")
        
        # test week pass
        resultado = descriptografar_senha(self.senha_fraca_cripto)
        self.assertEqual(resultado, self.senha_fraca, "A senha criptografada deve ser igual a senha original.")
        
        

if __name__ == "__main__":
    unittest.main()
