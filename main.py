# site com os scripts: https://cdnjs.com/
#pip install python-socketio flask-socketio simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send #importa o tunel e a posibilidade de mandar mensagem


app = Flask(__name__) #Cria um app para o site
Socketio = SocketIO(app, cors_allowed_origins="*") #Cria um tunel para a comunicação entre o cliente e o servidor, e permite qualquer usuario mandar mensagem (sem restrição) 

#funcionalidade de enviar mensagem
@Socketio.on("message")  #função que será ativada quando o cliente enviar uma mensagem
def gerenciar_mensagem(mensagem):   #função que recebe a mensagem
    send(mensagem, broadcast=True)  #envia a mensagem para todos os clientes conectados


#Cria a nossa primeira pagina = primeira rota
@app.route("/")
def homepage():
    return render_template("homepage.html") #renderiza a pagina

#Roda o  nosso app
if __name__ == "__main__": 
    Socketio.run(app)  #inicia o servidor, e permite que o tunel seja ativado , e o servidor seja acessado por qualquer usuario que esteja na mesma rede que o servidor.

#Websocket= tunel que liga um computador no outro (ex: para mensagens)
