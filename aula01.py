from flask import Flask

app_Mariela = Flask (__name__)

@app_Mariela.route('/')
def raiz():
    return 'Olá, turma!'

app_Mariela.run()
