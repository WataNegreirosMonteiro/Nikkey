"""
@author: Mariela
"""
#página usuario.html dinâmica
from flask import Flask, render_template

app_Mariela = Flask(__name__ , template_folder='templates')
#cria o objeto da aplicação

@app_Mariela.route("/")  #rota para solicitação web
def homepage():          #função
    return render_template ("homepage.html")

@app_Mariela.route("/contato")
def contato():
    return render_template("contato.html") 

@app_Mariela.route("/index")
def indice():
    return render_template ("index.html") 

@app_Mariela.route("/usuario")
def dados_usuario():
    #nome_usuario="Mariela"
    dados_usu = {"nome": "Mariela", "profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", dados = dados_usu)
                                           #parâmetro recebe argumento
                                           #colocar o site no ar

if __name__ == "__main__": 
     app_Mariela.run(port = 8000) 
                                