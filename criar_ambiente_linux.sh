#!/bin/bash

# Cria um ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual
source venv/bin/activate

# Instala as dependências
pip install -r requirements.txt
