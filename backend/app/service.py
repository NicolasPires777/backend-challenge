import re

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
    if 'message' in content:
        message = content['message']
        if len(message) > 10 and len(message) < 2000:
            return False
    return True
