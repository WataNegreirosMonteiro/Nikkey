#Criamos no decorador "app_Wata" com 2 páginas HTML estáticas.
"""
@author: Wata
"""
#nova biblioteca importada chamada render_template
from flask import Flask, render_template

app_Wata = Flask(__name__ , template_folder='.')
#cria o objeto da aplicação

@app_Wata.route("/")  #rota para solicitação web
def homepage():          #função
    return render_template("homepage.html")

@app_Wata.route("/contato")
def contato():
    return render_template("contato.html") 

if __name__ == "__main__": 
     app_Wata.run(port = 8000) 
                                
