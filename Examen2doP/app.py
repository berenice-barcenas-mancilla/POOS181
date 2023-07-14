from flask import Flask,render_template, request, redirect, url_for #importacion del framework 
from flask_mysqldb import MySQL
from flask import flash

#inicio
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbfloreria'
mysql = MySQL(app)
app.secret_key = "mi_clave_secreta"

#MOSTRAR 
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("Select * from tbflores")
    QueryFlores= cursor.fetchall() 
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    if result:
        return render_template('index.html',listFlores = QueryFlores)
    else:
        return "No se pudo conectar a la base de datos"


#REGISTRAR FLOR
@app.route('/guardar', methods=['POST']) 
def guardar():
    if request.method == 'POST':
        varFlor = request.form['txtnombre']
        varCantidad = request.form['txtcantidad']
        varPrecio = request.form['txtprecio']
        gcursor= mysql.connection.cursor()
        gcursor.execute('INSERT INTO tbflores (nombre,cantidad,precio) values (%s,%s,%s)',(varFlor,varCantidad,varPrecio))
        mysql.connection.commit()
    flash('La flor agregada correctamente!')
    return redirect(url_for('index'))


#ELIMINAR FLOR
@app.route('/editD/<id>')
def editD(id):
    dcs = mysql.connection.cursor()
    dcs.execute('Select * from tbflores where id = %s',(id,))
    QueryIdD = dcs.fetchone()
    print (QueryIdD)
    return render_template('deleteFlores.html',listIdDlt = QueryIdD)

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        if request.form.get('action') == 'delete':
            dCur = mysql.connection.cursor()
            dCur.execute('delete from tbflores where id = %s', (id,))
            mysql.connection.commit()
            flash('La Flor fue eliminada correctamente')
        elif request.form.get('action') == 'cancel':
            flash('Eliminacion cancelada')
    return redirect(url_for('flores'))


#MOSTRAR TODAS LAS FLORES
@app.route('/flores')
def flores():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tbflores")
    flores = cursor.fetchall()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    if result:
        return render_template('Flores.html', listFlores=flores)
    else:
        return "No se pudo conectar a la base de datos"

if __name__ =='__main__':
    app.run(port=5000,debug=True)