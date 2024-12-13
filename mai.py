from flask import Flask, url_for, render_template

#inicializacao
app =Flask(__name__)


#rota
@app.route('/')
def ola_mundo():
    return render_template("index.html")

@app.route('/sobre')
def pagina_sobre():
    return "<b> olha esse link<b>"
  
#execucao
app.run(debug=True)