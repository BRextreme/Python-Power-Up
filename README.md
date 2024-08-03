# Automação de Cadastro de Produtos

Este projeto automatiza o processo de cadastro de produtos em um sistema web utilizando o Python e a biblioteca `pyautogui`.

## Arquivos

- `Automacao.py`: O principal script do projeto que realiza toda a automação.
- `posicao.py`: Script utilizado para obter as coordenadas do mouse na página.
- `produtos.csv`: Base de dados com os produtos a serem cadastrados no sistema.

## Pré-requisitos

- Python 3.x
- Bibliotecas: `pyautogui`, `pandas`

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/BRextreme/Python-Power-Up
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd Python-Power-Up
    ```
3. Instale as dependências:
    ```sh
    pip install pyautogui pandas
    ```

## Uso

1. Certifique-se de que o arquivo `produtos.csv` está no mesmo diretório que `Automacao.py`.
2. Execute o script `Automacao.py`:
    ```sh
    python Automacao.py
    ```

### Automacao.py

Este script realiza os seguintes passos:
1. Abre o navegador e acessa o sistema de login da empresa.
2. Realiza o login no sistema utilizando as credenciais fornecidas no código.
3. Carrega a base de dados de produtos a partir do arquivo `produtos.csv`.
4. Para cada produto na base de dados, preenche os campos no formulário web e submete o cadastro.

### posicao.py

Este script é utilizado para obter as coordenadas X e Y do mouse na página web, que são necessárias para a automação. Utilize este script para ajustar as coordenadas caso a interface do sistema web seja alterada.

### produtos.csv

Arquivo CSV contendo os produtos a serem cadastrados. O arquivo deve seguir o seguinte formato:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
MOLO000192,Logitech,Mouse,2,19.95,5.00,
...
