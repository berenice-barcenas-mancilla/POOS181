from flask import Flask,render_template, request, redirect, url_for #importacion del framework 
from flask_mysqldb import MySQL
from flask import flash

#inicio
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdfruteria'
mysql = MySQL(app)
app.secret_key = "mi_clave_secreta"

#MOSTRAR FRUTAS
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("Select * from tbfrutas")
    QueryFrutas= cursor.fetchall() 
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    if result:
        return render_template('index.html',listFrutas = QueryFrutas)
    else:
        return "No se pudo conectar a la base de datos"


#REGISTRAR FRUTAS
@app.route('/guardar', methods=['POST']) 
def guardar():
    if request.method == 'POST':
        varFruta = request.form['txtfruta']
        varTemporada = request.form['txttemporada']
        varPrecio = request.form['txtprecio']
        varStock = request.form['txtstock']
        gcursor= mysql.connection.cursor()
        gcursor.execute('INSERT INTO tbfrutas (fruta,temporada,precio,stock) values (%s,%s,%s,%s)',(varFruta,varTemporada,varPrecio,varStock))
        mysql.connection.commit()
    flash('La fruta fue agregada correctamente')
    return redirect(url_for('index'))


#EDITAR FRUTA
@app.route('/editU/<id>')
def editU(id):
    eupcs = mysql.connection.cursor()
    eupcs.execute('Select * from tbfrutas where id = %s',(id,))
    QueryIdEU = eupcs.fetchone()
    print (QueryIdEU)
    return render_template('editFruta.html',listId = QueryIdEU)

@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        varUFruta = request.form['txtfruta']
        varUTemporada = request.form['txttemporada']
        varUPrecio = request.form['txtprecio']
        varUStock = request.form['txtstock']
        updCur = mysql.connection.cursor()
        updCur.execute('UPDATE tbfrutas SET fruta=%s, temporada=%s, precio=%s, stock=%s WHERE id=%s', (varUFruta, varUTemporada, varUPrecio, varUStock, id))

        mysql.connection.commit()
    flash('La informacion de la fruta fue actualizada correctamente')
    return redirect(url_for('frutas'))

#ELIMINAR FRUTA
@app.route('/editD/<id>')
def editD(id):
    dcs = mysql.connection.cursor()
    dcs.execute('Select * from tbfrutas where id = %s',(id,))
    QueryIdD = dcs.fetchone()
    print (QueryIdD)
    return render_template('deleteFruta.html',listIdDlt = QueryIdD)

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        if request.form.get('action') == 'delete':
            dCur = mysql.connection.cursor()
            dCur.execute('delete from tbfrutas where id = %s', (id,))
            mysql.connection.commit()
            flash('La Fruta fue eliminada correctamente')
        elif request.form.get('action') == 'cancel':
            flash('Eliminacion cancelada')
    return redirect(url_for('frutas'))


#MOSTRAR FRUTAS
@app.route('/frutas')
def frutas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tbfrutas")
    frutas = cursor.fetchall()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    if result:
        return render_template('Fruta.html', listFrutas=frutas)
    else:
        return "No se pudo conectar a la base de datos"

# Ruta para filtrar por fruta
@app.route('/filtrar', methods=['GET', 'POST'])
def filtrar_fruta():
    if request.method == 'POST':
        fruta = request.form['fruta']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tbfrutas WHERE fruta LIKE %s", ('%' + fruta + '%',))
        frutas_encontradas = cursor.fetchall()

        return render_template('filtro.html', frutas=frutas_encontradas)

    return render_template('filtro.html')

if __name__ =='__main__':
    app.run(port=5000,debug=True)