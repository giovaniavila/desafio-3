from flask import Flask, render_template
app = Flask(__name__,template_folder='templates', static_folder='static')
from flask_mysql import mysql

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['mysql_db'] = 'contatos'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quemsomos')
def somos():
    return render_template("quemsomos.html")

#contato sofre alteração devido ao formulário
@app.route('/contato', methods = ['GET', 'POST'])
def contatos():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['email']
        descricao = request.form['email']

        cur = mysql.connection.cursor() #faz a conexão com o banco
        cur.execute('insert into contato (email, assunto, descricao)') #executa o insert into

        mysql.connection.commit() #commita as informações do usuário

        cur.close() #fecha o post

        return 'sucesso' #indica que foi enviado com sucesso
    return render_template('contato.html')

#rota usuários para listar todos o usuários no banco de dados
def userr():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT *FROM contatos")

    if users > o:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails = userDetails)
