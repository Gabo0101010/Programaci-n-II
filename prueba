import tkinter as tk
from tkinter import ttk, messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de combobox")
ventana.geometry("300x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="Seleccione especialidad:")
etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Opciones del combobox
opciones = ["Cardiología", "Neurología", "Pediatría", "Dermatología"]
combo = ttk.Combobox(ventana, values=opciones, state="readonly")
combo.current(0)  # Selecciona primera opción por defecto
combo.grid(row=0, column=1, padx=10, pady=10)

# Función para mostrar selección
def mostrar():
    seleccion = combo.get()
    messagebox.showinfo("Selección", f"Has elegido: {seleccion}")

# Botón para confirmar
boton = tk.Button(ventana, text="Aceptar", command=mostrar)
boton.grid(row=1, column=0, columnspan=2, pady=15)

ventana.mainloop()
