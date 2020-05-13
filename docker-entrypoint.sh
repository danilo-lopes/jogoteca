#!/bin/bash

# Aguardando conexao com o banco
echo "Aguardando conexao com o banco"
python3 valida-conexao-db.py
sleep 2

# Aplica as migracoes do banco
echo "Aplicando migracoes do banco"
python3 migrations/prepara_banco.py
sleep 2

# Subindo a aplicacao
echo "Subindo a aplicacao"
python3 jogoteca.py
