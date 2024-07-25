from .controller import process_ticket

def configure_routes(app):
    @app.route('/hello')
    def hello():
        return "Hello, World!"

    @app.route('/ticket', methods=['POST'])
    def ticket_process():
        return process_ticket()
