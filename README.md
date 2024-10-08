# Secure Pass4

**Secure Pass4** é um gerador e gerenciador de senhas básico com funcionalidades de criptografia. Ele permite criar senhas aleatórias com diferentes níveis de complexidade e armazená-las de maneira segura em um arquivo criptografado, protegendo suas informações.

Salve o arquivo `chave.key` em um local seguro, pois você precisará dele para descriptografar suas senhas futuramente.

## Funcionalidades

- **Geração de Senhas Fortes:** Criação de senhas aleatórias com opções de letras maiúsculas, minúsculas, números e símbolos.
- **Gerenciamento de Senhas:** Armazene suas senhas de forma criptografada, associadas a sites ou serviços específicos.
- **Descriptografia Segura:** Acesso seguro às senhas, exigindo a chave de criptografia para recuperação.
- **Avaliação de Força:** Verifique se suas senhas são fortes, médias ou fracas antes de utilizá-las.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/rferrari/secure_pass4.git
    cd secure_pass4
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

### Importar Módulos

```python
from secure_pass4.secure_pass4 import avaliar_forca, gerar_senha
from secure_pass4.crypt_pass4.crypt_pass4 import criptografar_senha
from secure_pass4.save_pass4.save_pass4 import salvar_senha, carregar_senhas
```

### Gerar uma Senha

Você pode gerar uma senha segura com parâmetros personalizados (comprimento, inclusão de letras, números e símbolos):

```python
senha = gerar_senha(comprimento=16, incluir_letras=True, incluir_numeros=True, incluir_simbolos=True)
print(f"Senha gerada: {senha}")
```

### Salvar Senhas Criptografadas

Para salvar suas senhas de forma segura, utilize a função `salvar_senha`:

```python
site = "meusite.com"
senha = "minhaSenhaSegura123!"
salvar_senha(site, senha)
```

### Carregar e Descriptografar Senhas

Para carregar senhas já salvas e descriptografá-las, basta executar:

1. Copie a chave criptográfica para o diretório seguro:
    ```bash
    cp ~/chave.key ~/secure_pass/
    ```

2. Carregue as senhas salvas:
    ```python
    senhas_salvas = carregar_senhas()
    for site, senha in senhas_salvas.items():
        print(f"{site}: {senha}")
    ```

### Avaliar Força da Senha

Utilize a função `avaliar_forca` para verificar se a senha é forte o suficiente:

```python
senha = gerar_senha(comprimento=16, incluir_letras=True, incluir_numeros=True, incluir_simbolos=True)
resultado = avaliar_forca(senha)
print(f"Força da senha gerada: {resultado}")

# Avaliar uma senha específica
senha_especifica = "MinhaSenhaFraca"
resultado = avaliar_forca(senha_especifica)
print(f"Força da senha: {resultado}")
```

## Criptografia

O **Secure Pass4** usa a biblioteca `cryptography` para garantir que as senhas sejam protegidas por criptografia simétrica. Isso significa que, ao salvar uma senha, ela será criptografada, e o acesso só será possível através da chave criptográfica (`chave.key`) gerada durante a configuração.

## Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request se tiver melhorias, sugestões ou correções.

## Licença

Este projeto está licenciado sob a MIT License.

---
