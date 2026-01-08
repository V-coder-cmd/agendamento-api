import smtplib
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_APP = os.getenv("SENHA_APP")

def enviar_confirmacao(nome, email, data, horario):
    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = email
    mensagem["Subject"] = "Confirmação de Agendamento"

    html = f"""
    <html>
        <body>
            <h2>Olá, {nome}</h2>
            <p>Seu agendamento foi confirmado com sucesso.</p>
            <ul>
                <li><b>Data:</b> {data}</li>
                <li><b>Horário:</b> {horario}</li>
            </ul>
            <p>Obrigado por utilizar nosso sistema.</p>
        </body>
    </html>
    """
    mensagem.attach(MIMEText(html, "html", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_APP)
        servidor.send_message(mensagem)

def enviar_cancelamento(nome, email, data, horario):
    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = email
    mensagem["Subject"] = "Agendamento cancelado."

    html = f"""
    <html>
        <body>
            <h2>Olá, {nome}</h2>
            <p>Seu agendamento foi <b>Cancelado com sucesso</b></p>
            <ul>
                <li><b>Data:</b> {data}</li>
                <li><b>Horário:</b> {horario}</li>
            </ul>
            <p>Se precisar, fique à vontade para agendar novamente.</p>
        </body>
    </html>
    """

    mensagem.attach(MIMEText(html, "html", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_APP)
        servidor.send_message(mensagem)

def enviar_atualizacao(nome, email, data, horario):
    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = email
    mensagem["Subject"] = "Agendamento atualizado com sucesso!"

    html = f"""
    <html>
        <body>
            <h2>Olá, {nome}</h2>
            <p>Seu agendamento foi <b>Atualizado com sucesso!</b></p>
            <ul>
                <li><b>Data:</b> {data}</li>
                <li><b>Horário:</b> {horario}</li>
            </ul>
            <p>Se precisar, fique à vontade para atualizar seu agendamento novamente.</p>
        </body>
    </html>    
    """

    mensagem.attach(MIMEText(html, "html", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_APP)
        servidor.send_message(mensagem)