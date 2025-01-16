import tkinter as tk
from tkinter import ttk, messagebox
from utilidades.resultados import open_results_interface

def open_mmkf_interface():
    root = tk.Toplevel()
    root.title("Modelo de Colas M/M/K/F")

    input_frame = ttk.LabelFrame(root, text="Entradas")
    input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    descriptions = [
        "Tasa de llegada (λ):",
        "Tasa de servicio (μ):",
        "Número de servidores (K):",
        "Capacidad del sistema (F):",
    ]

    entries = []
    for i, desc in enumerate(descriptions):
        desc_label = ttk.Label(input_frame, text=desc)
        desc_label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

        entry = ttk.Entry(input_frame)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    def calculate():
        try:
            lam = float(entries[0].get())
            mu = float(entries[1].get())
            k = int(entries[2].get())
            f = int(entries[3].get())

            if lam >= k * mu:
                messagebox.showerror("Error", "La tasa de llegada debe ser menor que K * μ.")
                return

            rho = lam / (k * mu)
            utilization = rho

            # Cálculo de métricas (1plificado para M/M/K/F)
            lq = rho / (1 - rho)  # Aproximación
            ws = 1 / mu
            wq = lq / lam
            ls = lam * ws

            open_results_interface("M/M/K/F", utilization, wq, ws, lq, ls, None, lam, mu)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    calculate_button = ttk.Button(root, text="Calcular", command=calculate)
    calculate_button.grid(row=1, column=0, padx=10, pady=10)
