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

    def test_gerar_senha(self):
        """Teste para verificar geração de senha."""
        resultado = gerar_senha()
        #print("Senha Gerada: " + resultado)
        forca = avaliar_forca(resultado)
        self.assertEqual(forca, "Forte", "A senha gerada deve ser considerada 'Forte'.")
        self.assertNotEqual(resultado, "", "A senha gerada não deve estar vazia.")

        resultado = gerar_senha(6, True, False, False)
        #print("Senha Gerada: " + resultado)
        forca = avaliar_forca(resultado)
        self.assertEqual(forca, "Fraca", "A senha gerada deve ser considerada 'Fraca'.")
        self.assertNotEqual(resultado, "", "A senha gerada não deve estar vazia.")

        resultado = gerar_senha(8, True, True, False)
        #print("Senha Gerada: " + resultado)
        forca = avaliar_forca(resultado)
        self.assertEqual(forca, "Moderada", "A senha gerada deve ser considerada 'Moderada'.")
        self.assertNotEqual(resultado, "", "A senha gerada não deve estar vazia.")

        


if __name__ == "__main__":
    unittest.main()
