import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
from tkinter import messagebox

#Guardamos los datos en un archivo de texto
def guardarArchivo():
    with open("doctoresRegistro.txt", "w", encoding="utf-8") as archivo:
        for doctores in doctores_data:
            archivo.write(
                f'{doctores["Nombre"]}|{doctores["Especialidad"]}|{doctores["AñosExperiencia"]}|'
                f'{doctores["Genero"]}|{doctores["Hospital"]}\n'
            )
#Caragar los datos del archivo en la pagina
def cargar_desde_archivo():
    try:
        with open("doctoresRegistro.txt", "r", encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 5:
                    doctores = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "AñosExperiencia": datos[2],
                        "Genero": datos[3],
                        "Hospital": datos[4]
                    }
                    doctores_data.append(doctores)
        cargar_treeview()
    except FileNotFoundError:
        open("doctoresRegistro.txt", "w", encoding="utf-8").close()
#Lista para guardar los datos
doctores_data = []
#Funcion para registrar los doctores
def registrardoctores():
    doctores={
        "Nombre":nombreEntry.get(),
        "Especialidad":especialidadCombo.get(),
        "AñosExperiencia":edadDocSpin.get(),
        "Genero":sexoVar.get(),
        "Hospital":hospiCombo.get()
    }
    doctores_data.append(doctores)
    guardarArchivo()
    cargar_treeview()
#Funcion para cargar los datos en el treeview
def cargar_treeview():
    for doctores in treeview.get_children():
        treeview.delete(doctores)
    for i , item in enumerate(doctores_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["AñosExperiencia"],
                item["Genero"],
                item["Hospital"]
            )
        )
#Configuracion de la ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("800x750")
#Pestañas
pestanas = ttk.Notebook(ventanaPrincipal)
#Pestaña Pacientes y Doctores
frame_pacientes = ttk.Frame(pestanas)   
frame_doctores = ttk.Frame(pestanas)
pestanas.add(frame_pacientes, text="Pacientes")
pestanas.add(frame_doctores, text="Doctores")
pestanas.pack(expand=True, fill="both")
#Titulo de la seccion doctores
tituloLabel = tk.Label(frame_doctores, text="Registro de Doctores", font=("Arial", 16))
tituloLabel.grid(row=0, column=0, columnspan=2, pady=5)
#Nombre y Entry
nombrePacLabel=tk.Label(frame_doctores, text="Nombre completo:")
nombrePacLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
nombreEntry = tk.Entry(frame_doctores)
nombreEntry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
#Especialidad y Combobox
espeDocLabel=tk.Label(frame_doctores, text="Especialidad:")
espeDocLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)
especialidades = ["Medicina General","Cardiología","Pediatría","Traumatología","Dermatología"]
especialidadCombo = ttk.Combobox(frame_doctores, values=especialidades, state="readonly", width=25)
especialidadCombo.current(0)
especialidadCombo.grid(row=2, column=1, sticky="w", padx=5, pady=5)
#Edad y Spinbox
edadDocLabel=tk.Label(frame_doctores, text="Años de experiencia:")
edadDocLabel.grid(row=3, column=0, sticky="w", padx=5, pady=5)
edadDocSpin = tk.Spinbox(frame_doctores, from_=1, to=100, width=5)
edadDocSpin.delete(0, "end"); edadDocSpin.insert(0, "1") 
edadDocSpin.grid(row=3, column=1, sticky="w", padx=5, pady=5)
#Genero y Radiobuttons
sexoPLabel=tk.Label(frame_doctores, text="Género:")
sexoPLabel.grid(row=4, column=0, sticky="w", padx=5, pady=5)
sexoVar = tk.StringVar(value="Masculino")
tk.Radiobutton(frame_doctores, text="Masculino", variable=sexoVar, value="Masculino").grid(row=4, column=1, sticky="w", padx=5)
tk.Radiobutton(frame_doctores, text="Femenino", variable=sexoVar, value="Femenino").grid(row=4, column=2, sticky="w", padx=5)
#Hospital y Combobox
hospitalLabel=tk.Label(frame_doctores, text="Hospital")
hospitalLabel.grid(row=6, column=0, sticky="w", padx=5, pady=5)
hospitales = ["Hospital central", "Hospital Norte", "Clínica Santa Maria","Clínica Vida"]
hospiCombo = ttk.Combobox(frame_doctores, values=hospitales, state="readonly")
hospiCombo.current(0)
hospiCombo.grid(row=6, column=1, sticky="w", padx=5, pady=5)
#Boton Frame
btn_frame = tk.Frame(frame_doctores)
btn_frame.grid(row=8, column=1, columnspan=2, pady=5, sticky="w")
#Boton Registrar
btn_registrar = tk.Button(btn_frame, text="Registrar", command=registrardoctores,bg="green", fg="white")
btn_registrar.grid(row=0, column=0, padx=5)
#Treeview
treeview = ttk.Treeview(frame_doctores, columns=("Nombre","Especialidad","AñosExperiencia","Genero","Hospital"),
                        show="headings")
#Encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("Especialidad", text="Especialidad") 
treeview.heading("AñosExperiencia", text="Años de Experiencia")
treeview.heading("Genero", text="Género")
treeview.heading("Hospital", text="Hospital")
#Columnas y su configuracion
treeview.column("Nombre", width=200)
treeview.column("Especialidad", width=130)
treeview.column("AñosExperiencia", width=180, anchor="center")
treeview.column("Genero", width=80, anchor="center")
treeview.column("Hospital", width=180, anchor="center")
#Posicion del treeview
treeview.grid(row=9, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#Scrollbar
scroll_y = ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=9, column=2, sticky="ns")
#Cargar datos al iniciar la aplicacion
cargar_desde_archivo()
#Iniciar la ventana principal
ventanaPrincipal.mainloop()