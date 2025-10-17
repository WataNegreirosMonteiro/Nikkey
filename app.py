from flask import Flask

app = Flask(__name__, template_folder='paginas') 

@app.route("/")   
def inicio():
    return ''                                            

if __name__ == "__main__": 
    app.run(port = 8000) 