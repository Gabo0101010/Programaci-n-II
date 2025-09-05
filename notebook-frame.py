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

# Iniciar ventana
ventanaPrincipal.mainloop()
