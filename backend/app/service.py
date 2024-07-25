import re
import requests

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
        if valid_token(captcha):
            return False
    return True


def valid_token(token):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': "6LfxgxgqAAAAABx95eubEPpyRk83xBdIbuclTPwG",
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
