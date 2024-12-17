from flask import Flask, url_for, render_template

#inicializacao
app =Flask(__name__)


#rota
@app.route('/')
def ola_mundo():
    titulo = "gestão de usuarios"
    usuarios = [
        {"nome":"renan", "membro_ativo": True},
         {"nome":"rwesley", "membro_ativo": False},
          {"nome":"maria", "membro_ativo": False},
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return "<b> olha esse link<b>"
  
#execucao
app.run(debug=True)