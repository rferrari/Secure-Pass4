import unittest
import os

from secure_pass4.crypto_pass4.crypto_pass4 import criptografar_senha, descriptografar_senha, gerar_chave, carregar_chave
from secure_pass4.save_pass4.save_pass4 import salvar_senha, carregar_senhas
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

        senha = gerar_senha(10, True, True, False)
        resultado = criptografar_senha(senha)
        self.assertNotEqual(resultado, senha, "A senha criptografada deve ser diferente da senha original.")        
        

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

    def test_gerar_senha_forte(self):
        """Teste para verificar geração de senha."""
        resultado = gerar_senha()
        #print("Senha Gerada: " + resultado)
        forca = avaliar_forca(resultado)
        self.assertEqual(forca, "Forte", "A senha gerada deve ser considerada 'Forte'.")
        self.assertNotEqual(resultado, "", "A senha gerada não deve estar vazia.")

    def test_gerar_senha_fraca(self):
        resultado = gerar_senha(6, True, False, False)
        #print("Senha Gerada: " + resultado)
        forca = avaliar_forca(resultado)
        self.assertEqual(forca, "Fraca", "A senha gerada deve ser considerada 'Fraca'.")
        self.assertNotEqual(resultado, "", "A senha gerada não deve estar vazia.")

    def test_gerar_senha_moderada(self):
        resultado = gerar_senha(10, True, True, False)
        #print("Senha Gerada: " + resultado)
        forca = avaliar_forca(resultado)
        self.assertEqual(forca, "Moderada", "A senha gerada deve ser considerada 'Moderada'.")
        self.assertNotEqual(resultado, "", "A senha gerada não deve estar vazia.")

    def test_salvar_e_carregar_senhas(self):
        """Teste para salvar e carregar senhas."""
        site = 'site.com.br'
        
        salvar_senha(site, self.senha)
        senhas_carregadas = carregar_senhas()
    
        # Verificar se a senha está associada corretamente ao site
        self.assertIn(site, senhas_carregadas, "O site deve estar presente nas senhas carregadas.")
        self.assertEqual(senhas_carregadas[site], self.senha, "A senha deve estar correta para o site.")

    def test_gerar_chave(self):
        gerar_chave()
        chave = carregar_chave()

        self.assertIsNotNone(chave, "A chave gerada não deve ser None.")
        self.assertEqual(len(chave), 44, "O comprimento da chave deve ser 44 bytes.")  # Fernet keys are 44 bytes
        self.assertTrue(os.path.exists("chave.key"), "O arquivo chave.key deve existir após gerar a chave.")


if __name__ == "__main__":
    unittest.main()
