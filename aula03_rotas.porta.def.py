"""
@author: Mariela
"""
from flask import Flask  

app_Mariela = Flask (__name__) #cria objeto da aplicação. 

@app_Mariela.route('/')    #rota para solicitação web
@app_Mariela.route('/rota1') #rota para solicitação web
def rota1():  # função a ser executa quando chamar rotas acima ('/') e ('/rota1')
    return 'Olá, turma!'

@app_Mariela.route('/rota2')
def rota2():
    resposta = "<H3> Essa é outra página da rota 2 <H3>"
    return resposta

#função que não pertence a nenhuma rota. 
def saudacoes (nome): 
    return f'Olá, {nome}'

if __name__ == "__main__" :
    app_Mariela.run(port = 8000)  #executa aplicação

