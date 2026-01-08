# Agendamento API

API simples de **agendamento** desenvolvida em **Python + Flask**, com persistência em **SQLite** e envio de **e-mails automáticos** para confirmação, cancelamento e atualização de agendamentos.

---

## 📌 Funcionalidades

* Criar agendamentos
* Listar agendamentos
* Atualizar agendamentos
* Cancelar agendamentos
* Envio automático de e-mails:

  * Confirmação
  * Cancelamento
  * Atualização

---

## 🛠️ Tecnologias Utilizadas

* Python 3.11+
* Flask
* SQLite
* SMTP (Gmail)
* python-dotenv

---

## 📂 Estrutura do Projeto

```
agendamento_api/
│── app.py              # Aplicação Flask (rotas)
│── database.py         # Conexão e criação do banco SQLite
│── models.py           # Operações no banco de dados
│── email_service.py    # Serviço de envio de e-mails
│── requirements.txt    # Dependências do projeto
│── agendamentos.db     # Banco de dados (gerado automaticamente)
│── .env.example        # Variáveis de ambiente (exemplo)
```

---

## ⚙️ Instalação e Configuração

### 1️⃣ Clone o repositório

```bash
git clone <url-do-repositorio>
cd agendamento_api
```

### 2️⃣ Crie e ative um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Variáveis de Ambiente

Crie um arquivo **.env** na raiz do projeto:

```env
EMAIL_REMETENTE=seu_email@gmail.com
SENHA_APP=sua_senha_de_app_gmail
```

---

## ▶️ Executando a Aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 📡 Endpoints da API

### ➕ Criar Agendamento

**POST** `/agendar`

```json
{
    "nome": "Seu Nome Aqui",
  "email": "seu_email@email.com",
  "data": "2026-01-10",
  "horario": "14:00"
}
```

---

### 📋 Listar Agendamentos

**GET** `/agendamentos`

---

### ✏️ Atualizar Agendamento

**PUT** `/atualizar/<email>`

```json
{
  "data": "2026-01-12",
  "horario": "16:00"
}
```

---

### ❌ Cancelar Agendamento

**DELETE** `/cancelar/<email>`

---

## 🗄️ Banco de Dados

* Banco: **SQLite**
* Tabela criada automaticamente ao iniciar a aplicação

```sql
CREATE TABLE agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    data TEXT NOT NULL,
    horario TEXT NOT NULL
);
```

---

## 📧 Envio de E-mails

Os e-mails são enviados automaticamente quando:

* Um agendamento é criado
* Um agendamento é atualizado
* Um agendamento é cancelado

O envio é feito via **SMTP do Gmail**.

---

## 🧑‍💻 Autor

Desenvolvido para fins educacionais e aprendizado de APIs REST com Flask.

---

## 📄 Licença

Este projeto é livre para uso e estudo.