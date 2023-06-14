from flask import Flask
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
    return "Hola Mundo FLASK"

@app.route('/guardar')
def guardar():
    return "Se guardo en la BD"

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"

#ejecutar el servidor 
if __name__=='__main__':
    app.run(port=5000)
