# Leitor-Senhas-Wifi-Python

Script simples em Python para consultar perfis de Wi-Fi salvos no Windows e exibir a chave de segurança no terminal utilizando o comando nativo `netsh`.

## O que eu pratiquei neste projeto
- Execução de comandos do sistema operacional com `subprocess.check_output`
- Decodificação de saída de bytes e separação de linhas com `.decode()` e `.split()`
- Filtragem e limpeza de texto com `split()`, `.strip()` e laços `for`
- Tratamento de listas vazias com `try/except`
- Formatação de saída alinhada no terminal com f-strings

## Como executar
1. Certifique-se de ter o **Python 3** instalado em um ambiente **Windows**.
2. Clone ou baixe o repositório e entre na pasta do projeto:
   ```bash
   cd leitor-senhas-wifi-python
   ```
3. Execute o script no terminal:
   ```bash
   python main.py
   ```

## Observações
- Projetado para uso em Windows em português (dependendo do idioma ou codificação do sistema, pode ser necessário ajustar o `decode` ou os termos buscados na saída do `netsh`).
- Criado com foco educacional para estudo de lógica e automação básica em Python.
