from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
#INICIALIZACION DEL APP
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
app.secret_key='mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    #creamos un cursor y le decimos que ejecute la consulta para traer todos los albums y que los guarde en QueryAlbums
    #con la funcion fetchall y los imprimimos en la consola por el momento
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM albums")
    QueryAlbums = cursor.fetchall()
    return render_template('index.html', listAlbums=QueryAlbums)

#ruta http:localhost:5000/guardar - tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':  #se pasa a variables el contenido de los input
        titulo=request.form['txtTitulo']
        artista=request.form['txtArtista']
        anio=request.form['txtAnio']
        #print(titulo,artista,anio)
        
        #se conecta y ejecuta el insert
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO albums (titulo,artista,anio) VALUES(%s,%s,%s)',(titulo,artista,anio))#se prepara la sentencia de insert para ingresar
        mysql.connection.commit() #se ejecuta el insert 
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"

#ejecutar el servidor 
if __name__=='__main__':
    app.run(port=5000)



