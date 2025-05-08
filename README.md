# 🩺 Medical Appointment Manager (MAM)

Sistema RESTful para gerenciamento de **consultas médicas**, desenvolvido com Django e Django REST Framework. O projeto utiliza **Docker**, **Poetry** para gerenciamento de dependências.

## 🧰 Tecnologias utilizadas

- Python 3.12
- Django 4+
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Poetry
- GitHub Actions (CI/CD)

---

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/mam.git
cd mam
```
### 2. Crie seu .env com base no .env.example
```bash
cp .env.example .env
```
### 3. Construa os containers
```bash
docker-compose build
```
### 4. Suba a aplicação
```bash
docker-compose up
```

##  🧪 Rodando os testes
```bash
docker-compose run web python manage.py test
```
## 🛠 Variáveis de ambiente
Consulte o arquivo .env.example para configurar corretamente as variáveis:
| Variável            | Descrição                                   |
| ------------------- | ------------------------------------------- |
| POSTGRES\_DB        | Nome do banco                               |
| POSTGRES\_USER      | Usuário do banco                            |
| POSTGRES\_PASSWORD  | Senha do banco                              |
| SECRET\_KEY | Chave secreta do Django                     |
| DEBUG               | Ativar/Desativar debug (True/False)         |
| ALLOWED\_HOSTS      | Hosts permitidos (ex: localhost, 127.0.0.1) |
