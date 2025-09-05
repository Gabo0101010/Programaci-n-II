import tkinter as tk
from tkinter import messagebox, ttk
 
def mostrarEdad():
    tk.messagebox.showinfo("Edad", f"La edad seleccionada es: {spin.get()}")
   
def mostrarGenero():
    tk.messagebox.showinfo("Género", f"El género seleccionado es: {genero.get()}")
 
ventanaPrincipal=tk.Tk()
 
labelEdad=tk.Label(ventanaPrincipal, text="Edad:")
labelEdad.grid(row=0, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(ventanaPrincipal, from_=1, to=100)
spin.grid(row=0, column=1, padx=10, pady=10)
boton=tk.Button(ventanaPrincipal, text="Obtener valor", command=lambda:mostrarEdad())
boton.grid(row=3, column=0, padx=10, pady=10)
 
labelGenero=tk.Label(ventanaPrincipal, text="Género:")
labelGenero.grid(row=2, column=0, padx=5, pady=5, sticky="w")
genero=tk.Spinbox(ventanaPrincipal, values=("Masculino", "Femenino", "Otro"))
genero.grid(row=2, column=1, padx=10, pady=10)
botonGenero=tk.Button(ventanaPrincipal, text="Obtener género", command=lambda:mostrarGenero())
botonGenero.grid(row=3, column=1, padx=10, pady=10)
 
ventanaPrincipal.mainloop()

