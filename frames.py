import tkinter as tk
from tkinter import messagebox, ttk

# Ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de pacientes y Doctores")
ventanaPrincipal.geometry("500x800")

# Pestañas (Notebook)
pestanas = ttk.Notebook(ventanaPrincipal)

# Frame de Pacientes
frame_pacientes = ttk.Frame(pestanas)   # contenedor de la pestaña "Pacientes"
pestanas.add(frame_pacientes, text="Pacientes")

# Frame de Doctores
frame_doctores = ttk.Frame(pestanas)    # contenedor de la pestaña "Doctores"
pestanas.add(frame_doctores, text="Doctores")

# Mostrar el Notebook
pestanas.pack(expand=True, fill="both")

# --- FORMULARIO PACIENTES ---

# Nombre completo
tk.Label(frame_pacientes, text="Nombre completo:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreEntry = tk.Entry(frame_pacientes)
nombreEntry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

# Fecha de nacimiento
tk.Label(frame_pacientes, text="Fecha de nacimiento (dd/mm/aaaa):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
fechaEntry = tk.Entry(frame_pacientes)
fechaEntry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# Edad (solo lectura por ahora; se puede calcular luego)
tk.Label(frame_pacientes, text="Edad:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadEntry = tk.Entry(frame_pacientes, state="readonly")
edadEntry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Sexo (Radiobuttons)
tk.Label(frame_pacientes, text="Sexo:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
sexoVar = tk.StringVar(value="Masculino")  # valor por defecto
tk.Radiobutton(frame_pacientes, text="Masculino", variable=sexoVar, value="Masculino")\
    .grid(row=3, column=1, sticky="w", padx=5)
tk.Radiobutton(frame_pacientes, text="Femenino", variable=sexoVar, value="Femenino")\
    .grid(row=3, column=2, sticky="w", padx=5)

# (fila 4 la dejamos libre por si luego añadís algo más)

# Grupo sanguíneo (Entry libre: A, B, AB, O, con o sin Rh)
tk.Label(frame_pacientes, text="Grupo sanguíneo:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
grupoEntry = tk.Entry(frame_pacientes)
grupoEntry.grid(row=5, column=1, sticky="w", padx=5, pady=5)

# Tipo de seguro (Combobox)
tk.Label(frame_pacientes, text="Tipo de seguro:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
seguros = ["Publico", "Privado", "Ninguno"]
seguroCombo = ttk.Combobox(frame_pacientes, values=seguros, state="readonly")
seguroCombo.current(0)  # "Publico" por defecto
seguroCombo.grid(row=6, column=1, sticky="w", padx=5, pady=5)

# Centro médico (Combobox) — fila separada para evitar solape
tk.Label(frame_pacientes, text="Centro de salud:").grid(row=7, column=0, sticky="w", padx=5, pady=5)
centros_medicos = ["Hospital Central", "Clínica Norte", "Centro Sur"]
centroVar = tk.StringVar(value="Hospital Central")
comboCentroMedico = ttk.Combobox(frame_pacientes, values=centros_medicos, textvariable=centroVar, state="readonly")
comboCentroMedico.current(0)  # "Hospital Central" por defecto
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)

# Iniciar ventana
ventanaPrincipal.mainloop()
