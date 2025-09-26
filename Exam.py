#Importamos las librerias
import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
from tkinter import messagebox

#Funciones del Paciente

#Enmascaramiento de la Fecha
def enmascararFechaPaciente(texto):
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
    if fechaPacienteEntry.get()!=formatoFinal:
        fechaPacienteEntry.delete(0,tk.END)
        fechaPacienteEntry.insert(0, formatoFinal)
    if len(fechaPacienteEntry.get())==10:
        fechaActual=datetime.now().date()
        fechaNacimiento = datetime.strptime(fechaPacienteEntry.get(), "%d-%m-%Y").date()
        edad=fechaActual.year-fechaNacimiento.year
        edadPacienteVar.set(edad)
    else:
        edadPacienteVar.set("")
    return True

#Guardar archivo Pacientes
def guardarArchivoPaciente():
    with open("pacientePeso.txt", "w", encoding="utf-8") as archivo:
        for paciente in pacientes_data:
            archivo.write(
                f'{paciente["Nombre"]}|{paciente["Fecha de Nacimiento"]}|{paciente["Edad"]}|'
                f'{paciente["Genero"]}|{paciente["Grupo Sanguineo"]}|'
                f'{paciente["Tipo de Seguro"]}|{paciente["Centro Medico"]}|{paciente["Peso"]}\n'
            )
            
#Cargar desde archivo Pacientes
def cargarDesdeArchivoPaciente():
    try:
        with open("pacientePeso.txt", "r", encoding="utf-8") as archivo:
            pacientes_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 8:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Genero": datos[3],
                        "Grupo Sanguineo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Medico": datos[6],
                        "Peso": datos[7]
                    }
                    pacientes_data.append(paciente)
        cargarTreeviewPaciente()
    except FileNotFoundError:
        # Si no existe el archivo, lo crea vacío
        open("pacientePeso.txt", "w", encoding="utf-8").close()
        
#Eliminar Paciente
def eliminarPaciente():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar paciente",f"¿Estás seguro de eliminar este paciente?'{treeview.item(id_item, 'values')[0]}'?"):
            del pacientes_data[indice]
            guardarArchivoPaciente()
            cargarTreeviewPaciente()
            messagebox.showinfo("Eliminado","Paciente eliminado correctamente")
    else:
        messagebox.showwarning("No seleccionado","selecciona un paciente para eliminar.")
        return
    
# --- Handler: recarga al cambiar de pestaña ---
def alCambiarPestana(evento):
    indice_activo = pestanas.index(pestanas.select())
    if indice_activo == 0:          # Pacientes
        cargarDesdeArchivoPaciente()      # ya incluye cargar_treeview()
    elif indice_activo == 1:        # Doctores
        cargarDesdeArchivoDoctor()   # ya incluye cargar_treeviewDoc()

#Lista pacientes
pacientes_data=[]

#Funcion registrar
def registrarPaciente():
    #DICCIONARIO PACIENTE
    paciente={
        "Nombre":nombrePacienteEntry.get(),
        "Fecha de Nacimiento":fechaPacienteEntry.get(),
        "Edad":edadPacienteVar.get(),
        "Genero":sexoPacienteVar.get(),
        "Grupo Sanguineo":grupoPacienteEntry.get(),
        "Tipo de Seguro":seguroPacienteCombo.get(),
        "Centro Medico":centroPacienteVar.get(),
        "Peso":pesoPacienteEntry.get()
    }
    #Agregar Paciente a la lista
    pacientes_data.append(paciente)
    #Cargar en archivo
    guardarArchivoPaciente()
    #Cargar el Treeview
    cargarTreeviewPaciente()
    
#Cargar Treeview Paciente
def cargarTreeviewPaciente():
    #Limpiar Treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar Cada Paciente
    for i , item in enumerate(pacientes_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Medico"],
                item["Peso"]
            )
        )
        
#Funciones del Doctor

#Guardar archivo Doctores
def guardarArchivoDoctor():
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(
                f'{doctor["Nombre"]}|{doctor["Especialidad"]}|{doctor["Edad"]}|'
                f'{doctor["Telefono"]}\n'
            )
            
#Cargar desde archivo Doctores
def cargarDesdeArchivoDoctor():
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
        cargarTreeviewDoctor()
    except FileNotFoundError:
        # Si no existe el archivo, lo crea vacío
        open("doctores.txt", "w", encoding="utf-8").close()
        
#Eliminar Doctores
def eliminarDoctor():
    seleccionado = treeviewDoctores.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Confirmar Eliminación",f"¿Estás seguro de eliminar este Doctor?'{treeviewDoctores.item(id_item, 'values')[0]}'?"):
            del doctores_data[indice]
            guardarArchivoDoctor()
            cargarTreeviewDoctor()
            messagebox.showinfo("Eliminado","Doctores eliminado correctamente")
    else:
        messagebox.showwarning("No seleccionado","selecciona un Doctor para eliminar.")
        return
    
#Cargar Treeview Doctores
def cargarTreeviewDoctor():
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
def registarDoctor():
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
    guardarArchivoDoctor()
    #Cargar el Treeview
    cargarTreeviewDoctor()

# Ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de pacientes y Doctores")
ventanaPrincipal.geometry("700x650")

# Pestañas 
pestanas = ttk.Notebook(ventanaPrincipal)

# Frame de Pacientes 
framePacientes = ttk.Frame(pestanas)   
pestanas.add(framePacientes, text="Pacientes")

#Frame de Doctores 
frameDoctores = tk.Frame(pestanas, bg="#e8f2ff")
pestanas.add(frameDoctores, text="Doctores")

#Mostrar el Notebook
pestanas.pack(expand=True, fill="both")

#FORMULARIO PACIENTES

#Titulo 
tituloPacienteLabel=tk.Label(framePacientes, text="Registro del Paciente")
tituloPacienteLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

#Nombre
nombrePacienteLabel=tk.Label(framePacientes, text="Nombre completo:")
nombrePacienteLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
nombrePacienteEntry = tk.Entry(framePacientes)
nombrePacienteEntry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

#Fecha Nacimiento
fechaNacimientoPacienteLabel=tk.Label(framePacientes, text="Fecha de nacimiento (dd/mm/aaaa):")
fechaNacimientoPacienteLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)

validacionFecha=ventanaPrincipal.register(enmascararFechaPaciente)


fechaPacienteEntry = ttk.Entry(framePacientes,validate="key",validatecommand=(validacionFecha,"%P"))
fechaPacienteEntry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

#Edad
edadPacienteLabel=tk.Label(framePacientes, text="Edad:")
edadPacienteLabel.grid(row=3, column=0, sticky="w", padx=5, pady=5)
edadPacienteVar=tk.StringVar()
edadPacienteEntry = tk.Entry(framePacientes, textvariable=edadPacienteVar, state="readonly")
edadPacienteEntry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

#Sexo
sexoPacienteLabel=tk.Label(framePacientes, text="Sexo:")
sexoPacienteLabel.grid(row=4, column=0, sticky="w", padx=5, pady=5)
sexoPacienteVar = tk.StringVar(value="Masculino")
tk.Radiobutton(framePacientes, text="Masculino", variable=sexoPacienteVar, value="Masculino").grid(row=4, column=1, sticky="w", padx=5)
tk.Radiobutton(framePacientes, text="Femenino", variable=sexoPacienteVar, value="Femenino").grid(row=4, column=2, sticky="w", padx=5)

#Grupo S
grupoPacienteLabel=tk.Label(framePacientes, text="Grupo sanguíneo:")
grupoPacienteLabel.grid(row=5, column=0, sticky="w", padx=5, pady=5)
grupoPacienteEntry = tk.Entry(framePacientes)
grupoPacienteEntry.grid(row=5, column=1, sticky="w", padx=5, pady=5)

#Seguro
seguroPacienteLabel=tk.Label(framePacientes, text="Tipo de seguro:")
seguroPacienteLabel.grid(row=6, column=0, sticky="w", padx=5, pady=5)
seguros = ["Publico", "Privado", "Ninguno"]
seguroPacienteCombo = ttk.Combobox(framePacientes, values=seguros, state="readonly")
seguroPacienteCombo.current(0)
seguroPacienteCombo.grid(row=6, column=1, sticky="w", padx=5, pady=5)

#Centro
centroPacienteLabel=tk.Label(framePacientes, text="Centro de salud:")
centroPacienteLabel.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centros_medicos = ["Hospital Central", "Clínica Norte", "Centro Sur"]
centroPacienteVar = tk.StringVar(value="Hospital Central")
comboPacienteCentroMedico = ttk.Combobox(framePacientes, values=centros_medicos, textvariable=centroPacienteVar, state="readonly")
comboPacienteCentroMedico.current(0)
comboPacienteCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5) 

# Peso (Kg) - PACIENTES
pesoPacienteLabel = tk.Label(framePacientes, text="Peso (Kg): ")
pesoPacienteLabel.grid(row=8, column=0, sticky="w", padx=5, pady=5)

pesoPacienteEntry = tk.Entry(framePacientes, width=10)
pesoPacienteEntry.grid(row=8, column=1, sticky="w", padx=5, pady=5)

#Botones
btnPacienteFrame = tk.Frame(framePacientes)
btnPacienteFrame.grid(row=9, column=1, columnspan=2, pady=5, sticky="w")

btnPacienteRegistrar = tk.Button(btnPacienteFrame, text="Registrar", command=registrarPaciente)
btnPacienteRegistrar.grid(row=0, column=0, padx=5)

btnPacienteEliminar = tk.Button(btnPacienteFrame, text="Eliminar", command=eliminarPaciente)
btnPacienteEliminar.grid(row=0, column=1, padx=5)

treeview = ttk.Treeview(framePacientes, columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM","Peso"),
                        show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
treeview.heading("Peso", text="Peso (Kg)")

# Anchos Pacientes
treeview.column("Nombre", width=210)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=80, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
treeview.column("Peso", width=80)

treeview.grid(row=10, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)

scroll_y = ttk.Scrollbar(framePacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=10, column=2, sticky="ns")

#FORMULARIO DOCTORES

#Titulo
tituloDoctor = tk.Label(frameDoctores, text="Registro de Doctores", bg="#e8f2ff")
tituloDoctor.grid(row=0, column=0, columnspan=4, pady=(20, 10))

#Nombre
nombreDocLabel=tk.Label(frameDoctores, text="Nombre:", bg="#e8f2ff")
nombreDocLabel.grid(row=1, column=0, sticky="e", padx=10, pady=6)
nombreDocEntry = tk.Entry(frameDoctores, width=28)
nombreDocEntry.grid(row=1, column=1, sticky="w", padx=10, pady=6)

#Especialidad
espeDocLabel=tk.Label(frameDoctores, text="Especialidad:", bg="#e8f2ff")
espeDocLabel.grid(row=2, column=0, sticky="e", padx=10, pady=6)
especialidades = ["Medicina General","Cardiología","Pediatría","Traumatología","Dermatología"]
especialidadCombo = ttk.Combobox(frameDoctores, values=especialidades, state="readonly", width=25)
especialidadCombo.current(0)
especialidadCombo.grid(row=2, column=1, sticky="w", padx=10, pady=6)

#Edad
edadDocLabel=tk.Label(frameDoctores, text="Edad:", bg="#e8f2ff")
edadDocLabel.grid(row=3, column=0, sticky="e", padx=10, pady=6)
edadDocSpin = tk.Spinbox(frameDoctores, from_=18, to=100, width=5)
edadDocSpin.delete(0, "end"); edadDocSpin.insert(0, "27")  # como la imagen
edadDocSpin.grid(row=3, column=1, sticky="w", padx=10, pady=6)

#Teléfono
telLabel=tk.Label(frameDoctores, text="Teléfono:", bg="#e8f2ff")
telLabel.grid(row=4, column=0, sticky="e", padx=10, pady=6)
telefonoDocEntry = tk.Entry(frameDoctores, width=28)
telefonoDocEntry.grid(row=4, column=1, sticky="w", padx=10, pady=6)

#Frame pacientes
btn_frameD = tk.Frame(frameDoctores, bg="#e8f2ff")
btn_frameD.grid(row=5, column=0, columnspan=2, pady=5, sticky="nsew")
# Botones 
btnRegDoc = tk.Button(btn_frameD, text="Registrar", command=registarDoctor,bg="#27ae60", fg="white", 
                        activebackground="#1e874b")
btnRegDoc.grid(row=5, column=1, padx=(10,5), pady=10, sticky="e")

btnElimDoc = tk.Button(btn_frameD, text="Eliminar", command=eliminarDoctor,bg="#e74c3c", fg="white", 
                        activebackground="#c44134")
btnElimDoc.grid(row=5, column=2, padx=(5,10), pady=10, sticky="w")

# Tabla 
treeviewDoctores = ttk.Treeview(frameDoctores,columns=("Nombre","Especialidad","Edad","Telefono"),
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
scroll_y_doc = ttk.Scrollbar(frameDoctores, orient="vertical", command=treeviewDoctores.yview)
treeviewDoctores.configure(yscrollcommand=scroll_y_doc.set)
scroll_y_doc.grid(row=6, column=3, sticky="ns")

#Cargar datos desde archivo
cargarDesdeArchivoPaciente()

#Cargae datos doctores desde archivo
cargarDesdeArchivoDoctor()

# Iniciar ventana
ventanaPrincipal.mainloop()
