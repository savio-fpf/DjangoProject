# LibBook 1.0

> *Versão*: 1.0.0

## Descrição

Uma biblioteca virtual criada para adicionar itens, livros e autores diversos. Adicionar, remover e editar são as principais funcionalidades da aplicação. 

## Pré-requisitos

- Python 3
- venv (já incluso no Python 3)
- Django
- DbsQlite

## Instalação e Configuração

1. *Crie um ambiente virtual*
   bash
   python3 -m venv .venv  # cria o virtualenv na pasta .venv
   

2. *Ative o ambiente virtual*
   - *Linux/macOS*:
     bash
     source .venv/bin/activate
     
   - *Windows PowerShell*:
     powershell
     .venv\Scripts\activate
     

3. *Instale as dependências*
   bash
   pip install Django
   

## Migrações do Banco de Dados

bash
python manage.py makemigrations
python manage.py migrate


## Executando o Servidor

bash
python manage.py runserver


## Acesso

Abra o navegador e acesse:


http://127.0.0.1:8000/


## Versão

- ## LibBook 1.0

## Equipe

- *Nome da equipe*: LifeAI
- *Tech Leader*: João
- *Dev1*: Guilherme
- *Dev2*: Gustavo
- *Dev3*: Amilton