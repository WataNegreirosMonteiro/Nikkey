from flask import Flask

meu_app = Flask(__name__)
@meu_app.route('/')
@meu_app.route('/inicio')
def inicio():
    return 'Olá, turma!. Sou o Flask'

@meu_app.route('/cadastro')
def cadastro():
    return 'Tela de cadastro'

@meu_app.route('/sobre')
def sobre():
    return 'Programa para aula de Flask'

def saudacao(nome):
    return (f'olá,{nome}')

#if __name__ == "__main__":
meu_app.run(port= 8000)
