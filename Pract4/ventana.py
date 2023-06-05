import tkinter as tk
from tkinter import ttk, font
from tkinter import *
from mainClass import *

controlador = Bebidas()

Ventana = Tk()
Ventana.title("Almacen")
Ventana.geometry("800x500")
# Configuración de estilos
bg_color = "#C997A9"
button_color = "#F5EBCE"
font_family = "Montserrat"
style = ttk.Style()
style.configure("TFrame", background=bg_color)
style.configure("TButton", background=button_color, font=(font_family, 12, "bold"))
style.configure("Treeview", background="white", font=(font_family, 10))
style.configure("TLabel", background=bg_color, font=(font_family, 12, "bold"))
# Modificar estilo de la tabla
style = ttk.Style()
style.configure("Treeview", background="#F5EBCE", foreground="black", font_family = "Montserrat")
style.map("Treeview", background=[('selected', '#C997A9')])
# Configurar colores de encabezado de tabla
style.configure("Treeview.Heading", background="#C997A9", foreground="black")
# Vincular estilos a los botones
style.configure("TButton", background="#F5EBCE",font_family = "Montserrat")
# Modificar estilo de la pestaña seleccionada
style.configure("TNotebook", background="#F5EBCE")
style.map("TNotebook.Tab", background=[("selected", "#C997A9")], foreground=[("selected", "#F5EBCE")])


def nuevo():
    titulo.configure(text="Agregar")
    panel.add(pestana2, text='Agregar')
    txtNom.delete("0", "end")
    txtClasif.delete("0", "end")
    txtMarca.delete("0", "end")
    txtPrecio.delete("0", "end")
    panel.select(1)
    btna.pack()
    btnactu.pack_forget()
    btnDelete.pack_forget()
def agregar():
    if controlador.guardar_bebida(varNom.get(), varClasif.get(), varMarca.get(), varPrecio.get()):
        txtNom.delete("0", "end")
        txtClasif.delete("0", "end")
        txtMarca.delete("0", "end")
        txtPrecio.delete("0", "end")
        panel.forget(1)
        panel.select(0)
def modificar():
    titulo.configure(text="Modificar")
    panel.add(pestana2, text='Modificar')
    btnactu.pack()
    btnDelete.pack()
    btna.pack_forget()
    txtNom.delete("0", "end")
    txtClasif.delete("0", "end")
    txtMarca.delete("0", "end")
    txtPrecio.delete("0", "end")
    selected = tree.selection()[0]
    values = tree.item(selected)['values']
    txtId.insert(0, values[0])
    txtNom.insert(0, values[1])
    txtClasif.insert(0, values[2])
    txtMarca.insert(0, values[3])
    txtPrecio.insert(0, values[4])
    panel.select(1)
def actualizar():
    if controlador.actualizar_bebida(varIdUp.get(), varNom.get(), varClasif.get(), varMarca.get(), varPrecio.get()):
        txtId.delete("0", "end")
        txtNom.delete("0", "end")
        txtClasif.delete("0", "end")
        txtMarca.delete("0", "end")
        txtPrecio.delete("0", "end")
        panel.forget(1)
        panel.select(0)
def DeleteProd():
    if controlador.eliminar_bebida(varIdUp.get()):
        txtId.delete("0", "end")
        txtNom.delete("0", "end")
        txtClasif.delete("0", "end")
        txtMarca.delete("0", "end")
        txtPrecio.delete("0", "end")
        panel.forget(1)
        panel.select(0)
def Promedio():
    controlador.precio_promedio_bebidas()
def ventanaEmergente():
    global varVE, ventanaMarcas
    ventanaMarcas = tk.Toplevel()
    ventanaMarcas.title("Ventana emergente")
    varVE = tk.StringVar()
    combobox = ttk.Combobox(ventanaMarcas, textvariable=varVE, values=controlador.GetMarcas())
    combobox.pack()
    boton = Button(ventanaMarcas, text="Cantidad de bebidas", command=ObtenerMarca)
    boton.pack()
def ObtenerMarca():
    controlador.cantidad_por_marca(varVE.get())
    ventanaMarcas.destroy()
def Clasificacion_Bebida():
    controlador.cantidad_por_clasificacion()
    
panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
panel.add(pestana1, text='Consultar')
fuente = font.Font(family='Montserrat', size=12, weight='bold')
TituloCons = Label(pestana1, text="Consultar Bebida", fg="black", font=fuente)
TituloCons.pack()
columns = ('ID', 'Nombre', 'Clasificación', 'Marca', 'Precio')
tree = ttk.Treeview(pestana1, columns=columns, show='headings')
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Clasificación", text="Clasificación")
tree.heading("Marca", text="Marca")
tree.heading("Precio", text="Precio")
tree.pack()
btnUpdate = Button(pestana1, text='Actualizar', command=modificar)
btnUpdate.pack_forget()
buttonContainer = Frame(pestana1)
buttonContainer.pack(anchor='center')
BtnAdd = Button(buttonContainer, text='Nueva Bebida', command=nuevo)
BtnAdd.pack(side='left')
btnPrecioPromedio = Button(buttonContainer, text='Precio Promedio', command=Promedio)
btnPrecioPromedio.pack(side='left')
btnBebidasXMarca = Button(buttonContainer, text='Marcas', command=ventanaEmergente)
btnBebidasXMarca.pack(side='left')
btnBebidasXClasificacion = Button(buttonContainer, text='Clasificacion', command=Clasificacion_Bebida)
btnBebidasXClasificacion.pack(side='left')
titulo = Label(pestana2, text="Agregar Bebida", fg="black", font=fuente)
titulo.pack()
varIdUp = tk.StringVar()
txtId = Entry(pestana2, textvariable=varIdUp)
varNom = tk.StringVar()
lblNom = Label(pestana2, text="Nombre de la bebida: ")
lblNom.pack()
txtNom = Entry(pestana2, textvariable=varNom)
txtNom.pack()
varClasif = tk.StringVar()
lblClasif = tk.Label(pestana2, text="Clasificación: ")
lblClasif.pack()
txtClasif = ttk.Combobox(pestana2, textvariable=varClasif, values=["Bebida Azucarada", "Bebida sin Azúcar", "Bebida Gaseosa", "Bebida Energética"])
txtClasif.pack()
varMarca = tk.StringVar()
lblMarca = tk.Label(pestana2, text="Marca: ")
lblMarca.pack()
txtMarca = Entry(pestana2, textvariable=varMarca)
txtMarca.pack()
varPrecio = tk.StringVar()
lblPrecio = tk.Label(pestana2, text="Precio: ")
lblPrecio.pack()
txtPrecio = Entry(pestana2, textvariable=varPrecio)
txtPrecio.pack()
btna = Button(pestana2, text="Agregar", command=agregar)
btnDelete = Button(pestana2, bg="#C997A9", fg="white", text="Eliminar", command=DeleteProd)

btnactu = Button(pestana2, text="Actualizar", command=actualizar)
def Consultar(event):
    current_tab = event.widget.tab('current')['text']
    if current_tab == 'Consultar':
        for row in tree.get_children():
            tree.delete(row)
        a=controlador.consultar_bebidas()
        while a:
            row = a.pop(0)  
            tree.insert('', tk.END, values=(row))   
panel.bind('<<NotebookTabChanged>>', Consultar)
def Mostrarboton(event):
    if tree.selection():
        btnUpdate.pack()
    else:
        btnUpdate.pack_forget()
tree.bind('<<TreeviewSelect>>', Mostrarboton)
Ventana.mainloop()
