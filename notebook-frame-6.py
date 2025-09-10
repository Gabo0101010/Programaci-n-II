import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
from tkinter import messagebox
#Enmascaramiento
def enmascararFecha(texto):
    limpio = ''.join(filter(str.isdigit, texto))
    formatoFinal=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formatoFinal=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formatoFinal=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formatoFinal=limpio
    if fechaEntry.get()!=formatoFinal:
        fechaEntry.delete(0,tk.END)
        fechaEntry.insert(0, formatoFinal)
    if len(fechaEntry.get())==10:
        fechaActual=datetime.now().date()
        fechaNacimiento = datetime.strptime(fechaEntry.get(), "%d-%m-%Y").date()
        edad=fechaActual.year-fechaNacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
#Guardar archivo Pacientes
def guardarArchivo():
    with open("paciente.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(
                f'{paciente["Nombre"]}|{paciente["Fecha de Nacimiento"]}|{paciente["Edad"]}|'
                f'{paciente["Genero"]}|{paciente["Grupo Sanguineo"]}|'
                f'{paciente["Tipo de Seguro"]}|{paciente["Centro Medico"]}\n'
            )
#Cargar desde archivo Pacientes
def cargar_desde_archivo():
    try:
        with open("paciente.txt", "r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Genero": datos[3],
                        "Grupo Sanguineo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Medico": datos[6]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        # Si no existe el archivo, lo crea vacío
        open("paciente.txt", "w", encoding="utf-8").close()
#Eliminar Paciente
def eliminarPaciente():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar paciente",f"¿Estás seguro de eliminar este paciente?'{treeview.item(id_item, 'values')[0]}'?"):
            del paciente_data[indice]
            guardarArchivo()
            cargar_treeview()
            messagebox.showinfo("Eliminado","Paciente eliminado correctamente")
    else:
        messagebox.showwarning("No seleccionado","selecciona un paciente para eliminar.")
        return

#Lista pacientes
paciente_data=[]
#Funcion registrar
def registrarPaciente():
    #DICCIONARIO PACIENTE
    paciente={
        "Nombre":nombreEntry.get(),
        "Fecha de Nacimiento":fechaEntry.get(),
        "Edad":edadVar.get(),
        "Genero":sexoVar.get(),
        "Grupo Sanguineo":grupoEntry.get(),
        "Tipo de Seguro":seguroCombo.get(),
        "Centro Medico":centroVar.get()
    }
    #Agregar Paciente a la lista
    paciente_data.append(paciente)
    #Cargar en archivo
    guardarArchivo()
    #Cargar el Treeview
    cargar_treeview()
    
#Cargar Treeview
def cargar_treeview():
    #Limpiar Treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar Cada Paciente
    for i , item in enumerate(paciente_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Medico"]
            )
        )
#Guardar archivo Doctores
def guardarArchivoDoc():
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(
                f'{doctor["Nombre"]}|{doctor["Especialidad"]}|{doctor["Edad"]}|'
                f'{doctor["Telefono"]}\n'
            )
#Cargar desde archivo Doctores
def cargar_desde_archivoDoc():
    try:
        with open("doctores.txt", "r", encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Edad": datos[2],
                        "Telefono": datos[3]
                    }
                    doctores_data.append(doctor)
        cargar_treeviewDoc()
    except FileNotFoundError:
        # Si no existe el archivo, lo crea vacío
        open("doctores.txt", "w", encoding="utf-8").close()
#Eliminar Doctores
def eliminarDoctores():
    seleccionado = treeviewDoctores.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Confirmar Eliminación",f"¿Estás seguro de eliminar este Doctor?'{treeview.item(id_item, 'values')[0]}'?"):
            del doctores_data[indice]
            guardarArchivoDoc()
            cargar_treeviewDoc()
            messagebox.showinfo("Eliminado","Doctores eliminado correctamente")
    else:
        messagebox.showwarning("No seleccionado","selecciona un Doctor para eliminar.")
        return
#Cargar Treeview Doctores
def cargar_treeviewDoc():
    #Limpiar Treeview
    for doctor in treeviewDoctores.get_children():
        treeviewDoctores.delete(doctor)
    #Insertar Cada Paciente
    for i , item in enumerate(doctores_data):
        treeviewDoctores.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Telefono"]
            )
        )
#Lista Registar doctores
doctores_data=[]
#Funcion Registar Doctores
def registarDoctores():
    #DICCIONARIO PACIENTE
    doctor={
        "Nombre":nombreDocEntry.get(),
        "Especialidad":especialidadCombo.get(),
        "Edad":edadDocSpin.get(),
        "Telefono":telefonoDocEntry.get(),
    }
    #Agregar Paciente a la lista
    doctores_data.append(doctor)
    #Cargar en archivo
    guardarArchivoDoc()
    #Cargar el Treeview
    cargar_treeviewDoc()

# Ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de pacientes y Doctores")
ventanaPrincipal.geometry("700x650")

# Pestañas 
pestanas = ttk.Notebook(ventanaPrincipal)

# Frame de Pacientes 

frame_pacientes = ttk.Frame(pestanas)   
pestanas.add(frame_pacientes, text="Pacientes")

#Frame de Doctores 

frame_doctores = tk.Frame(pestanas, bg="#e8f2ff")
pestanas.add(frame_doctores, text="Doctores")

#Mostrar el Notebook
pestanas.pack(expand=True, fill="both")

#FORMULARIO PACIENTES

#Nombre
nombrePacLabel=tk.Label(frame_pacientes, text="Nombre completo:")
nombrePacLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreEntry = tk.Entry(frame_pacientes)
nombreEntry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

#Fecha Nacimiento
fechaNaciLabel=tk.Label(frame_pacientes, text="Fecha de nacimiento (dd/mm/aaaa):")
fechaNaciLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)

validacionFecha=ventanaPrincipal.register(enmascararFecha)


fechaEntry = ttk.Entry(frame_pacientes,validate="key",validatecommand=(validacionFecha,"%P"))
fechaEntry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

#Edad
edadPLabel=tk.Label(frame_pacientes, text="Edad:")
edadPLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadVar=tk.StringVar()
edadEntry = tk.Entry(frame_pacientes, textvariable=edadVar, state="readonly")
edadEntry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

#Sexo
sexoPLabel=tk.Label(frame_pacientes, text="Sexo:")
sexoPLabel.grid(row=3, column=0, sticky="w", padx=5, pady=5)
sexoVar = tk.StringVar(value="Masculino")
tk.Radiobutton(frame_pacientes, text="Masculino", variable=sexoVar, value="Masculino").grid(row=3, column=1, sticky="w", padx=5)
tk.Radiobutton(frame_pacientes, text="Femenino", variable=sexoVar, value="Femenino").grid(row=3, column=2, sticky="w", padx=5)

#Grupo S
grupoPLabel=tk.Label(frame_pacientes, text="Grupo sanguíneo:")
grupoPLabel.grid(row=5, column=0, sticky="w", padx=5, pady=5)
grupoEntry = tk.Entry(frame_pacientes)
grupoEntry.grid(row=5, column=1, sticky="w", padx=5, pady=5)

#Seguro
seguroPLabel=tk.Label(frame_pacientes, text="Tipo de seguro:")
seguroPLabel.grid(row=6, column=0, sticky="w", padx=5, pady=5)
seguros = ["Publico", "Privado", "Ninguno"]
seguroCombo = ttk.Combobox(frame_pacientes, values=seguros, state="readonly")
seguroCombo.current(0)
seguroCombo.grid(row=6, column=1, sticky="w", padx=5, pady=5)

#Centro
centroPLabel=tk.Label(frame_pacientes, text="Centro de salud:")
centroPLabel.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centros_medicos = ["Hospital Central", "Clínica Norte", "Centro Sur"]
centroVar = tk.StringVar(value="Hospital Central")
comboCentroMedico = ttk.Combobox(frame_pacientes, values=centros_medicos, textvariable=centroVar, state="readonly")
comboCentroMedico.current(0)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5) 

#Botones
btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=1, columnspan=2, pady=5, sticky="w")

btn_registrar = tk.Button(btn_frame, text="Registrar", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(btn_frame, text="Eliminar", command=eliminarPaciente)
btn_eliminar.grid(row=0, column=1, padx=5)

treeview = ttk.Treeview(frame_pacientes, columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM"),
                        show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")

# Anchos Pacientes
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)

treeview.grid(row=9, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)

scroll_y = ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=8, column=2, sticky="ns")

#FORMULARIO DOCTORES

#Titulo
tituloDoctor = tk.Label(frame_doctores, text="Registro de Doctores", bg="#e8f2ff")
tituloDoctor.grid(row=0, column=0, columnspan=4, pady=(20, 10))

#Nombre
nombreDocLabel=tk.Label(frame_doctores, text="Nombre:", bg="#e8f2ff")
nombreDocLabel.grid(row=1, column=0, sticky="e", padx=10, pady=6)
nombreDocEntry = tk.Entry(frame_doctores, width=28)
nombreDocEntry.grid(row=1, column=1, sticky="w", padx=10, pady=6)

#Especialidad
espeDocLabel=tk.Label(frame_doctores, text="Especialidad:", bg="#e8f2ff")
espeDocLabel.grid(row=2, column=0, sticky="e", padx=10, pady=6)
especialidades = ["Medicina General","Cardiología","Pediatría","Traumatología","Dermatología"]
especialidadCombo = ttk.Combobox(frame_doctores, values=especialidades, state="readonly", width=25)
especialidadCombo.current(0)
especialidadCombo.grid(row=2, column=1, sticky="w", padx=10, pady=6)

#Edad
edadDocLabel=tk.Label(frame_doctores, text="Edad:", bg="#e8f2ff")
edadDocLabel.grid(row=3, column=0, sticky="e", padx=10, pady=6)
edadDocSpin = tk.Spinbox(frame_doctores, from_=18, to=100, width=5)
edadDocSpin.delete(0, "end"); edadDocSpin.insert(0, "27")  # como la imagen
edadDocSpin.grid(row=3, column=1, sticky="w", padx=10, pady=6)

#Teléfono
telLabel=tk.Label(frame_doctores, text="Teléfono:", bg="#e8f2ff")
telLabel.grid(row=4, column=0, sticky="e", padx=10, pady=6)
telefonoDocEntry = tk.Entry(frame_doctores, width=28)
telefonoDocEntry.grid(row=4, column=1, sticky="w", padx=10, pady=6)

#Frame pacientes
btn_frameD = tk.Frame(frame_doctores, bg="#e8f2ff")
btn_frameD.grid(row=5, column=0, columnspan=2, pady=5, sticky="nsew")
# Botones 
btnRegDoc = tk.Button(btn_frameD, text="Registrar", command=registarDoctores,bg="#27ae60", fg="white", 
                        activebackground="#1e874b")
btnRegDoc.grid(row=5, column=1, padx=(10,5), pady=10, sticky="e")

btnElimDoc = tk.Button(btn_frameD, text="Eliminar", command=eliminarDoctores,bg="#e74c3c", fg="white", 
                        activebackground="#c44134")
btnElimDoc.grid(row=5, column=2, padx=(5,10), pady=10, sticky="w")

# Tabla 
treeviewDoctores = ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad","Edad","Telefono"),
                                show="headings", height=10)

treeviewDoctores.heading("Nombre", text="Nombre")
treeviewDoctores.heading("Especialidad", text="Especialidad")
treeviewDoctores.heading("Edad", text="Edad")
treeviewDoctores.heading("Telefono", text="Teléfono")

# Anchos Doctores 
treeviewDoctores.column("Nombre", width=180)
treeviewDoctores.column("Especialidad", width=180)
treeviewDoctores.column("Edad", width=60, anchor="center")
treeviewDoctores.column("Telefono", width=140)

treeviewDoctores.grid(row=6, column=0, columnspan=3, padx=15, sticky="nsew")

# Scroll vertical 
scroll_y_doc = ttk.Scrollbar(frame_doctores, orient="vertical", command=treeviewDoctores.yview)
treeviewDoctores.configure(yscrollcommand=scroll_y_doc.set)
scroll_y_doc.grid(row=6, column=3, sticky="ns")
#Cargar datos desde archivo
cargar_desde_archivo()
#Cargae datos doctores desde archivo
cargar_desde_archivoDoc()
# Iniciar ventana
ventanaPrincipal.mainloop()
