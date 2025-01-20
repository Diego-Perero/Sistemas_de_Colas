import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.mm1 import open_mm1_interface
from modelos.mmk import open_mmk_interface
from modelos.mg1 import open_mg1_interface
from modelos.mmkf import open_mmkf_interface

def main():
    root = tk.Tk()
    root.title("Seleccionar un Modelo")
    root.geometry("400x175")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    title_label = ttk.Label(frame, text="Título del Problema:")
    title_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    title_entry = ttk.Entry(frame)
    title_entry.grid(row=0, column=1, padx=5, pady=5)

    modelo_label = tk.Label(frame, text="Escoja un modelo:")
    modelo_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    opciones = ["M/M/1", "M/M/K", "M/G/1", "M/M/K/F"]
    combobox = ttk.Combobox(frame, values=opciones, state="readonly", width=20)
    combobox.grid(row=1, column=1, padx=5, pady=5)
    combobox.current(0)

    def manejar_seleccion():
        seleccion = combobox.get()
        if seleccion == "M/M/1":
            open_mm1_interface()
        elif seleccion == "M/M/K":
            open_mmk_interface()
        elif seleccion == "M/G/1":
            open_mg1_interface()
        elif seleccion == "M/M/K/F":
            open_mmkf_interface()
        else:
            messagebox.showinfo("Información", f"El modelo {seleccion} no está implementado.")

    boton_ok = ttk.Button(root, text="Ok", command=manejar_seleccion)
    boton_ok.pack(pady=5)

    boton_cancelar = ttk.Button(root, text="Cancelar", command=root.destroy)
    boton_cancelar.pack(pady=0)

    root.mainloop()


if __name__ == "__main__":
    main()