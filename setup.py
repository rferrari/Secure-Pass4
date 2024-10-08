from setuptools import setup, find_packages

setup(
    name='secure_pass4',
    version='0.1',  
    description='Gerador e gerenciador de senhas básico com funcionalidades de criptografia.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Adam Ferrari',
    author_email='rferrariwd@gmail.com',
    url='https://github.com/rferrari/secure_pass4',
    packages=find_packages(),   
    include_package_data=True,  
    install_requires=[
        'cryptography',         # Dependência necessária para criptografia
    ],
    classifiers=[
        'Programming Language :: Python :: 3',      # Versão do Python
        'License :: OSI Approved :: MIT License',  # Licença
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                        # Versão mínima do Python necessária
)
