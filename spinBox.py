import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo Spinbox con grid")
ventana.geometry("300x150")

# Etiqueta en fila 0, columna 0
labelEdad = tk.Label(ventana, text="Seleccione su edad")
labelEdad.grid(row=0, column=0, padx=10, pady=10)

# Spinbox en fila 0, columna 1 (valores del 1 al 10)
spin = tk.Spinbox(ventana, from_=1, to=120)
spin.grid(row=0, column=1, padx=10, pady=10)

# Función para mostrar el valor seleccionado
def mostrar_edad():
    valor = spin.get()
    messagebox.showinfo("Edad", f"La edad elegida fue :{valor}")

# Botón en fila 1, columna 0 (ocupa 2 columnas)
boton = tk.Button(ventana, text="Enviar", command=mostrar_edad)
boton.grid(row=1, column=0, columnspan=2, pady=10)

ventana.mainloop()
