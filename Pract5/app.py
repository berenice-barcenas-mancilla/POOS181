from flask import Flask, render_template,request
from flask_mysqldb import MySQL

#INICIALIZACION DEL APP
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
mysql=MySQL(app)

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html');

#ruta http:localhost:5000/guardar - tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo=request.form['txtTitulo']
        artista=request.form['txtArtista']
        anio=request.form['txtAnio']
        print(titulo,artista,anio)
        
    return "Se guardo en la BD"

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"

#ejecutar el servidor 
if __name__=='__main__':
    app.run(port=5000)
