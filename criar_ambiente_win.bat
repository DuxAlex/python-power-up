@echo off

:: Cria um ambiente virtual
python -m venv venv

:: Ativa o ambiente virtual
call venv\Scripts\activate

:: Instala as dependências
pip install -r requirements.txt
