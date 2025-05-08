# Usa imagem oficial do Python
FROM python:3.12-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Instala o Poetry e as dependências do projeto
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copia o restante dos arquivos
COPY . .

# Expõe a porta 8000 (padrão do Django)
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
