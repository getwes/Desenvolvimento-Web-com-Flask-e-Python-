from flask import Flask, url_for

#inicializacao
app =Flask(__name__)


#rota
@app.route('/')
def ola_mundo():
    return "eae suave"

@app.route('/sobre')
def ola_mundo():
    return "<"
  
#execucao
app.run(debug=True)