import pandas as pd
import smtplib
import os
import email.message
import time

# Carrega os e-mails do CSV
data = pd.read_csv("../data/external/teste-emails.csv")
emails = data["email"]

def send_email(destinatario):
    corpo_email = """
    <p>Olá, isso é um teste!</p>
    <p>lalalalalalalala</p>
    """
    # Configura mensagem
    msg = email.message.Message()
    msg['Subject'] = 'Email automático'
    remetente = 'seuemail@gmail.com'  # Seu e-mail
    msg['From'] = remetente
    msg['To'] = destinatario
    password = os.getenv('EMAIL_PASSWORD')  # Variável de ambiente para a senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    try:
        # Configura o servidor SMTP
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(remetente, password)
        
        # Envia o e-mail
        s.sendmail(remetente, destinatario, msg.as_string().encode('utf-8'))
        print(f'E-mail enviado com sucesso para: {destinatario}')
    except Exception as e:
        print(f"Erro ao enviar e-mail para {destinatario}: {e}")
    finally:
        s.quit()

# Loop para enviar o e-mail para todos os destinatários
for email in emails:
    send_email(email)
    time.sleep(2)