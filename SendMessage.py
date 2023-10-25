import pandas as pd
import pywhatkit as kit
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

lista = pd.read_excel("Lista.xlsx")
logindf = pd.read_excel("Login.xlsx")
numeroint = lista.iloc[:, 0].tolist()
char = "+"
numeros = [char + str(palavra) for palavra in numeroint]
emails = lista.iloc[:, 1].tolist()
nomes = lista.iloc[:, 2].tolist()

login = logindf.iloc[0, 0]
senha = logindf.iloc[0, 1]
smtp_server = "smtp.office365.com"
smtp_port = 587  # Porta para TLS/STARTTLS
username = login
password = senha

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Use TLS/STARTTLS para conexão segura
server.login(username, password)  # Faça login na sua conta do Outlook

de = login
assunto = "Teste Pythonn"

i = 0
j = 0

for email in emails:
    corpo = f"Isso é uma mensagem automática enviada pelo Python {nomes[i]}."
    msg = MIMEMultipart()
    msg["From"] = de
    msg["To"] = email
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain"))

    server.sendmail(de, email, msg.as_string())

    i += 1

server.quit()

for num in numeros:
    if j == 0:
        hora_atual = datetime.now().time()
        mensagem = f"Olá {nomes[j]}, esta é uma mensagem automática."
        kit.sendwhatmsg(num, mensagem, hora_atual.hour, hora_atual.minute+2)
    else:
        hora_atual = datetime.now().time()
        mensagem = f"Olá {nomes[j]}, esta é uma mensagem automática."
        kit.sendwhatmsg(num, mensagem, hora_atual.hour, hora_atual.minute+1)

    j += 1