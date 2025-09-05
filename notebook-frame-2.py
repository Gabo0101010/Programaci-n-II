import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
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


fechaEntry = ttk.Entry(frame_pacientes,validate="key")
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

btn_registrar = tk.Button(btn_frame, text="Registrar", command="")
btn_registrar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(btn_frame, text="Eliminar", command="")
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
btnRegDoc = tk.Button(btn_frameD, text="Registrar", command="",bg="#27ae60", fg="white", 
                        activebackground="#1e874b")
btnRegDoc.grid(row=5, column=1, padx=(10,5), pady=10, sticky="e")

btnElimDoc = tk.Button(btn_frameD, text="Eliminar", command="",bg="#e74c3c", fg="white", 
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

# Iniciar ventana
ventanaPrincipal.mainloop()
