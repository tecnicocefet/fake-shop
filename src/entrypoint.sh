#!/bin/bash

# Verifica se o banco de dados está pronto
while ! nc -z postgre 5432; do
  echo "Aguardando o banco de dados..."
  sleep 2
done

# Aplica as migrações
echo "Aplicando migrações..."
python -m flask db upgrade

# Inicia a aplicação
echo "Iniciando a aplicação..."
python -m gunicorn --bind 0.0.0.0:5000 index:app