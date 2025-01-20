import tkinter as tk
from tkinter import ttk, messagebox
from utilidades.resultados import open_results_interface

def open_mg1_interface():
    root = tk.Toplevel()
    root.title("Modelo de Colas M/G/1")

    input_frame = ttk.LabelFrame(root, text="Entradas")
    input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    descriptions = [
        "Tasa de llegada (λ):",
        "Tasa de servicio (μ):",
        "Varianza del tiempo de servicio (σ^2):",
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
            sigma_squared = float(entries[2].get())

            if lam >= mu:
                messagebox.showerror("Error", "La tasa de llegada debe ser menor que la tasa de servicio.")
                return

            utilization = lam / mu
            wq = (lam * sigma_squared + utilization ** 2) / (2 * (1 - utilization))
            ws = wq + (1 / mu)
            lq = lam * wq
            ls = lam * ws

            open_results_interface("M/G/1", utilization, wq, ws, lq, ls, None, None, lam, mu)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    calculate_button = ttk.Button(root, text="Calcular", command=calculate)
    calculate_button.grid(row=1, column=0, padx=10, pady=10)
