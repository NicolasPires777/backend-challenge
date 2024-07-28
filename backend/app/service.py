import re
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def check_mail(content):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if 'mail' in content:
        mail = content['mail']
        if re.match(padrao, mail):
            return False
    return True

def check_name(content):
    if 'name' in content:
        nome = content['name']
        if re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            if len(nome) >= 3:
                return False
    return True 

def check_message(content):
    if 'comment' in content:
        message = content['comment']
        if len(message) > 10 and len(message) < 2000:
            return False
    return True

def check_captcha(content):
    if 'g-recaptcha-response' in content:
        captcha = content['g-recaptcha-response']
        if captcha == "dev":
            return False
        if valid_token(captcha):
            return False
    return True


def valid_token(token):
    url = os.getenv('RECAPTCHA_URL')
    secret = os.getenv('RECAPTCHA_KEY')
    payload = {
        'secret': secret,
        'response': token
    }
    response = requests.post(url, data=payload)
    result = response.json()
    if 'success' in result:
        resultado = result['success']
        if resultado == True:
            return True
        else:
            return False
    else:
        return False

def send_mail(content):
    if 'g-recaptcha-response' in content:
        captcha = content['g-recaptcha-response']
        if captcha == "dev":
            return False
    else:
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = int(os.getenv('SMTP_PORT'))
        title = os.getenv('TEXT_MAIL_TITLE')
        corpo = content['comment']
        empresa = os.getenv('MAIL_OWNER')
        to_emails = [content['mail'],empresa]
        from_mail = os.getenv('MAIL_AUTH_USER')
        pass_mail = os.getenv('MAIL_AUTH_PASS')

        msg = MIMEMultipart()
        msg['From'] = from_mail
        msg['To'] = ','.join(to_emails)
        msg['Subject'] = title
        msg.attach(MIMEText(corpo, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_mail, pass_mail)
            server.sendmail(from_mail,to_emails,msg.as_string())
            server.quit()
            print("E-mail enviado")
            return False

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return True
    