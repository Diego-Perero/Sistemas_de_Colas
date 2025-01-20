import tkinter as tk
import math
from tkinter import ttk, messagebox
from utilidades.resultados import open_results_interface

def open_mmk_interface():
    root = tk.Toplevel()
    root.title("Modelo de Colas M/M/K")

    input_frame = ttk.LabelFrame(root, text="Entradas")
    input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    descriptions = [
        "Tasa de llegada (λ):",
        "Tasa de servicio (μ):",
        "Número de servidores (K):",
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

            if lam >= k * mu:
                messagebox.showerror("Error", "La tasa de llegada debe ser menor que K * μ.")
                return

            rho = lam / (k * mu)
            utilization = rho

            # Verificar que el denominador de wq no sea cero ni negativo
            denominator = k * mu - lam
            if denominator <= 0:
                messagebox.showerror("Error", "El valor de (K * μ - λ) debe ser mayor que cero.")
                return

            # Cálculo de Wq con factorial y denominador seguro
            wq = ((lam * mu) / (math.factorial(k) * denominator ** 2))  # Aproximación para Wq
            ws = wq + (1 / mu)
            lq = lam * wq
            ls = lam * ws

            # Ahora pasamos lam y mu a open_results_interface
            open_results_interface("M/M/K", utilization, wq, ws, lq, ls, None, None, lam, mu)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    calculate_button = ttk.Button(root, text="Calcular", command=calculate)
    calculate_button.grid(row=1, column=0, padx=10, pady=10)
