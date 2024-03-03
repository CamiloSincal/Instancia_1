from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostname = 'localhost'
puerto_server = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/check':
            self.send_response(200)  # Código de estado 200
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Ok')
        elif self.path == "/":
            data = {
                "Instancia": "Instancia #1 - API #1",
                "Curso": "Seminario de Sistemas 1",
                "Estudiante":"Estudiante - <202000605>"
            }
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))
            
def iniciar_servidor():
    webServer = HTTPServer((hostname,puerto_server), MyServer)
    print(f'Servidor iniciado http://{hostname}:{puerto_server}')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    iniciar_servidor()