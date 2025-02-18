#Importanto o flask
from flask import Flask, render_template

#Carregando o flask na variavel app
app = Flask (__name__,template_folder='views')

#Criando a primeira rota do site
@app.route('/')

#Criando função do python
def home():
    return render_template('index.html')

@app.route ('/games')
def games ():
    titulo = 'CS-GO'
    ano = 2012
    categoria = 'FPS Online'
    jogadores=['Midna','Vt','Leaf','Quemario','Trop','Aspax','maxxdiego']
    jogos=['GTA V','Valorant','Elden Ring','Sekiro','Free Fire','Mad Max','Dying Light']
    return render_template("games.html",titulo= titulo,ano=ano,categoria=categoria,jogadores=jogadores,jogos=jogos)

#Iniciando o servidor no localhost, porta 500, modo de depuração ativado
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)