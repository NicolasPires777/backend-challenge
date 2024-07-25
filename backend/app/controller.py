from flask import jsonify, request # type: ignore
from .service import check_mail, check_name, check_message, check_captcha

def process_ticket():
    content = request.get_json()
    if not request.is_json:
        retorno = {
            "type": "about:blank",
            "title": "Bad Request",
            "detail": "A requisição não foi enviada como JSON",
            "instance": "/ticket"
        }
        return jsonify(retorno), 400
    
    if check_captcha(content):
        retorno = {
            "type": "about:blank",
            "title": "Unauthorized",
            "detail": "Captcha inválido",
            "instance": "/ticket"
        }
        return jsonify(retorno), 401
    
    if check_mail(content):
        retorno = {
            "type": "about:blank",
            "title": "Bad Request",
            "detail": "Mail não é válido ou não está presente na requisição",
            "instance": "/ticket"
        }
        return jsonify(retorno), 400
    
    if check_name(content):
        retorno = {
            "type": "about:blank",
            "title": "Bad Request",
            "detail": "O campo nome está vazio ou possui caracteres inválidos",
            "instance": "/ticket"
        }
        return jsonify(retorno), 400
    
    if check_message(content):
        retorno = {
            "type": "about:blank",
            "title": "Bad Request",
            "detail": "O campo mensagem deve ter de 10 a 2000 caracteres",
            "instance": "/ticket"
        }
        return jsonify(retorno), 400
    
    return jsonify(content), 201
