"""
@author: Wata
"""
#página usuario.html dinâmica
from flask import Flask, render_template

app_Wata = Flask(__name__ , template_folder='t_templates')
#cria o objeto da aplicação

@app_Wata.route("/")  #rota para solicitação web
def homepage():          #função
    return render_template ("t_index.html")

@app_Wata.route("/contato")
def contato():
    return render_template("t_contato.html") 

@app_Wata.route("/index")
def indice():
    return render_template ("t_index.html") 

@app_Wata.route("/usuario")
def dados_usuario():
    #nome_usuario="Mariela"
    dados_usu = {"nome": "Mariela", "profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", dados = dados_usu)
                                           #parâmetro recebe argumento
                                           #colocar o site no ar

if __name__ == "__main__": 
     app_Wata.run(port = 8000) 
                                