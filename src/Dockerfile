FROM python:3.11.0
EXPOSE 5000

# Instala as dependências e limpa o cache
COPY requirements.txt .
RUN python -m pip install -r requirements.txt && \
    python -m pip cache purge

# Configura o diretório de trabalho e copia o código
WORKDIR /app
COPY . /app

# Torna o entrypoint.sh executável
RUN chmod +x /app/entrypoint.sh

# Configura variáveis de ambiente
ENV PROMETHEUS_MULTIPROC_DIR=/tmp/metrics
ENV FLASK_APP=index.py
ENV FLASK_ENV=production
ENV DATABASE_URL="postgresql+psycopg://fakeshop:Pg1234@postgre:5432/fakeshop?sslmode=disable"

# Cria o diretório para métricas
RUN mkdir -p /tmp/metrics

# Define o comando de inicialização
CMD ["/app/entrypoint.sh"]
