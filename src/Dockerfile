FROM python:3.11.0

# Expondo a porta 5000
EXPOSE 5000

# Copia as dependências e as instala
COPY requirements.txt .
RUN python -m pip install -r requirements.txt && \
    python -m pip cache purge

# Instala o `nc` (Netcat) para verificar a disponibilidade do banco de dados
RUN apt-get update && apt-get install -y netcat

# Configura o diretório de trabalho e copia o código da aplicação
WORKDIR /app
COPY . /app

# Torna o `entrypoint.sh` executável
RUN chmod +x /app/entrypoint.sh

# Configura variáveis de ambiente
ENV PROMETHEUS_MULTIPROC_DIR=/tmp/metrics
ENV FLASK_APP=index.py
ENV FLASK_ENV=production
ENV DATABASE_URL="postgresql+psycopg://fakeshop:Pg1234@postgre:5432/fakeshop?sslmode=disable"

# Cria o diretório necessário para métricas
RUN mkdir -p /tmp/metrics

# Define o comando de inicialização
CMD ["/app/entrypoint.sh"]
