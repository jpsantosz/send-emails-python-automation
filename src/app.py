import pandas as pd
import smtplib
import os
import ssl
import email.message

data = pd.read_csv("../data/external/teste-emails.csv")

email = data["email"][0]

def send_email():
    corpo_email = """
    <p>Olá, isso é um teste!</p>
    <p><lalalalalalalala/p>
    """
    msg = email.message.Message()
    msg['Subject'] = 'Email automático'
    msg['From'] = email
    msg['To'] = email
    password = senha
    msg.add_header('Content_Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gemail.com: 587')
    s.starttls()
    
    s.login(msg['From'],password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email Enviado')
    
send_email()