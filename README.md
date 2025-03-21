# Fake Shop CI/CD Pipeline

Este repositório contém a configuração para automatizar o processo de build e deploy do e-commerce **Fake Shop** utilizando **GitHub Actions** e **Kubernetes**.

## Como executar

### Pré-requisitos

1. **Docker Hub**: Adicione suas credenciais do Docker Hub como **secrets** no GitHub:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`

2. **Kubernetes (DigitalOcean)**: Adicione o certificado da CA do Kubernetes e o token de acesso como **secrets** no GitHub:
   - `DO_K8S_CA`
   - `DO_TOKEN`

3. **GitHub Actions**: A pipeline será executada automaticamente quando houver push na branch `main`.

### Como funciona a pipeline

1. **Build da Imagem Docker**: A pipeline cria uma imagem Docker da aplicação Fake Shop e a publica no Docker Hub.
2. **Deploy no Kubernetes**: A pipeline aplica os manifestos do Kubernetes para fazer o deploy da aplicação no cluster.

### Instruções adicionais

- Acesse os logs do Kubernetes com o comando `kubectl logs <nome-do-pod>`.
- A pipeline aguarda o término do rollout da aplicação antes de finalizar o deploy.

## Como testar localmente

1. Faça o clone do repositório.
2. Certifique-se de ter o Kubernetes e Docker configurados localmente.
3. Aplique os manifestos do Kubernetes e execute o container Docker localmente para testar a aplicação.



# Fake Shop


## Variável de Ambiente
DB_HOST	=> Host do banco de dados PostgreSQL.

DB_USER => Nome do usuário do banco de dados PostgreSQL.

DB_PASSWORD	=> Senha do usuário do banco de dados PostgreSQL.

DB_NAME	=>	Nome do banco de dados PostgreSQL.

DB_PORT	=>	Porta de conexão com o banco de dados PostgreSQL.
