import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(subject, body, to_emails):
    # Obtém as variáveis de ambiente
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    from_email = os.getenv('FROM_EMAIL')
    app_password = os.getenv('APP_PASSWORD')

    # Criação do objeto de mensagem
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    # Adiciona o corpo do e-mail à mensagem
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, app_password)
        server.sendmail(from_email, to_emails, msg.as_string())
        server.quit()

        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Uso da função
if __name__ == "__main__":
    subject = 'Teste do Nicolas'
    body = 'Isso é um teste, se receber, manda um OK (agora rodando com docker)'
    to_emails = ['nicolas@zedia.com.br', 'jose@zedia.com.br']
    send_email(subject, body, to_emails)
