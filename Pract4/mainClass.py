import sqlite3
from tkinter import messagebox


class Bebidas:
    def __init__(self):
        pass
    #CONEXION A LA BASE DE DATOS
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/bere1/Documents/GitHub/Programacion-Orientada-A-Objetos-S-181/Pract4/bebidas.db")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar a la base de datos")

    def guardar_bebida(self, nombre, clasificacion, marca, precio):
        #conexion a la base de datos
        conx = self.conexionBD()
        #validacion de parametros vacios
        if nombre == "" or clasificacion == "" or marca == "" or precio == "":
            messagebox.showwarning("Error", "Formulario incompleto")
            conx.close()
            return False
        if clasificacion not in ["Bebida Azucarada", "Bebida sin Azúcar", "Bebida Gaseosa", "Bebida Energética"]:
            messagebox.showwarning("Error", "La clasificación debe ser una de las opciones válidas.")
            return False
        try:
            #por ultimo validamos que el precio sea un número flotante, si es así se ejecuta la consulta de agregar producto, de lo contrario manda error.
            int(precio)
            #3. Preparamos el cursor, datos que voy a insertar y el querySQL
            cursor= conx.cursor()
            datos=(nombre,clasificacion,marca,precio)
            qrInsert="insert into bebidas (nombre, clasificacion, marca, precio) values (?,?,?,?)" 
            #4.Ejecutamos el insert y cerramos la conexion
            cursor.execute(qrInsert,datos)           
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Bebida Guardada")
            conx.close()
            return True
        except ValueError:
            messagebox.showwarning("Error", "Ingresa un numero válido.")
            conx.close
            return False


    def consultar_bebidas(self):
        #conectamos a la bd
        conx = self.conexionBD()
        try:
            cursor = conx.cursor()
            query = "SELECT * FROM bebidas"
            #ejecuta y guarda la consulta
            cursor.execute(query)
            resultados = cursor.fetchall()
            conx.close()
            #Retornar resultados 
            lista = []
            for row in resultados:
                lista.append(row)
            conx.close()
            return lista
        except sqlite3.OperationalError:
            print("Consulta ERROR")
            conx.close()
            

    def actualizar_bebida(self, id, nombre, clasificacion, marca, precio):
        #CONEXION A BD
        conx = self.conexionBD()
        #VALIDACION DE PARAMETROS VACIOS
        if nombre == "" or clasificacion == "" or marca == "" or precio == "":
            messagebox.showwarning("Error", "No puedes actualizar un formulario y dejar campos vacíos")
            return False
        if clasificacion not in ["Bebida Azucarada", "Bebida sin Azúcar", "Bebida Gaseosa", "Bebida Energética"]:
            messagebox.showwarning("Error", "La clasificación debe ser una de las opciones válidas.")
            return False
        try:
            float(precio)
            cursor = conx.cursor()
            datos = (nombre, clasificacion, marca, precio, id)
            query = "UPDATE bebidas SET Nombre=?, Clasificacion=?, Marca=?, Precio=? WHERE id=?"
            #EJECUTAMOS LA CONSULTA Y SE CIERRA CONEXION
            cursor.execute(query, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("SUCCESSFUL", "Bebida actualizada")
            return True
        except ValueError:
            messagebox.showwarning("Error", "El precio debe ser un número válido.")
            return False

    def eliminar_bebida(self, id):
        #CONEXION A BD
        conx = self.conexionBD()
        #PREGUNTAR AL USUARIO SI DESEA ELIMINAR
        confirmar = messagebox.askyesno("Eliminar Bebida", "¿Estás seguro que deseas eliminar esta bebida? Esta acción no se puede deshacer.")
        if confirmar:
            try:
                cursor = conx.cursor()
                query = "DELETE FROM bebidas WHERE id=?"
                cursor.execute(query, (id,))
                #EJECUTA Y GUARDA LA CONSULTA
                conx.commit()
                conx.close()
                return True
            except sqlite3.OperationalError:
                print("Error en la consulta")
        else:
            messagebox.showerror("Error", "No se pudo eliminar la bebida.")
            conx.close()
            return False

    def precio_promedio_bebidas(self):
       #CONEXION A BD
        conx = self.conexionBD()
        try:
            cursor = conx.cursor()
            query = "SELECT AVG(Precio) AS PrecioPromedio FROM bebidas"
            cursor.execute(query)
            promedio = cursor.fetchone()[0]
            messagebox.showinfo("Precio promedio de bebidas", f"El precio promedio de las bebidas es: {promedio}")
            conx.close()
        except sqlite3.OperationalError:
            print("Error en la consulta")
            conx.close()
            
    def cantidad_por_clasificacion(self):
        #CONEXION A BD
        conx = self.conexionBD()
        try:
            cursor = conx.cursor()
            query = "SELECT Clasificacion, COUNT(*) AS CantidadDeBebidas FROM bebidas GROUP BY Clasificacion"
            cursor.execute(query)
            resultados = cursor.fetchall()
            conx.close()

            if len(resultados) == 0:
                messagebox.showinfo("Cantidad de bebidas por clasificación", "No hay bebidas registradas en la base de datos.")
            else:
                mensaje = ""
                for resultado in resultados:
                    clasificacion = resultado[0]
                    cantidad = resultado[1]
                    mensaje += f"Clasificación: {clasificacion}\nCantidad: {cantidad}\n\n"
                messagebox.showinfo("Cantidad de bebidas por clasificación", mensaje)

        except sqlite3.OperationalError:
            print("Error en la consulta")
            conx.close()

    def GetMarcas(self):
        conx=self.conexionBD()
        try:
            cursor = conx.cursor()
            consulta = "SELECT DISTINCT Marca FROM bebidas;"
            cursor.execute(consulta)
            marcas = cursor.fetchall()
            conx.close()
            return [marca[0] for marca in marcas]
        except sqlite3.OperationalError:
            print("Error en la consulta")
            conx.close()


    def cantidad_por_marca(self, marca):
        if marca == "":
            messagebox.showwarning("Campos incompletos", "No puedes consultar si tienes los campos vacíos, por favor selecciona un campo")
        else:
            try:
                conx = self.conexionBD()
                cursor = conx.cursor()
                query = f"SELECT COUNT(*) FROM bebidas WHERE Marca='{marca}'"
                cursor.execute(query)
                cantidad = cursor.fetchone()[0]
                conx.close()

                if cantidad is not None:
                    messagebox.showinfo("Cantidad de bebidas por marca", f"La cantidad de bebidas de la marca '{marca}' es: {cantidad}")
                else:
                    messagebox.showinfo("Cantidad de bebidas por marca", f"No se encontraron bebidas de la marca '{marca}'.")
            except sqlite3.OperationalError:
                print("Error en la consulta")
                conx.close()