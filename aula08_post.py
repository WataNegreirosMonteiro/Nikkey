from flask import Flask, render_template
from flask import request  
#adicionar para trabalhar com os métodos GET e POST

app_Mariela = Flask(__name__, template_folder='t_templates') 
# os templates coloca em outra pasta. 
# Por padrão, fica na pasta templates e não precisa informar no template_folder,
# mas se quiser armazenar em outra pasta indique nesse parâmetro.

@app_Mariela.route("/")       #se no navegador digitar / ou /index
@app_Mariela.route("/index")  
def indice():
    return render_template ("t_index.html")                                               #optei por prefixar com t_ os nomes dos arquivos que usam template

@app_Mariela.route("/contato")
def contato():
    return render_template("t_contato.html") 

#rota /usuarios COM passagem de argumentos
@app_Mariela.route("/usuarios/<nome_usuario>;<nome_profissao>")
#rota /usuarios SEM passagem de argumentos --> definir valor padrão com defaults
@app_Mariela.route("/usuarios", defaults={"nome_usuario":"usuário?","nome_profissao":""})  
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  

#new
@app_Mariela.route("/login")
def login():
    return render_template("t_login.html") 

#new
"""
Para poder recuperar os argumentos passados nos parâmetros na URL precisa importar o pacote
from flask import request

Também precisa colocar que essa página aceita requisições de tipo GET ou POST
O GET é padrão, mas no caso do POST altere no html method="POST"
"""
@app_Mariela.route("/autenticar", methods=['POST'] ) 
def autenticar():
    #método GET - recebe pela URL ==> (args)
    #usuario = request.args.get('nome_usuario')
    #senha = request.args.get('senha')

    #, methods=['POST'] método POST - pega nos fields (campos) do formulário => form
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    return f"usuario: {usuario} e senha: {senha}"

if __name__ == "__main__": 
     app_Mariela.run(port = 8000) 
     