from flask import Flask, url_for

#inicializacao
app =Flask(__name__)


#rota
@app.route('/')
def ola_mundo():
    return f"<a href='{url_for('pagina_sobre')}'>pagina sobre<a>"

@app.route('/sobre')
def pagina_sobre():
    return "<b> olha esse link<b>"
  
#execucao
app.run(debug=True)