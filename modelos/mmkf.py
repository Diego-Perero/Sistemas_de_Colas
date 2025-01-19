import tkinter as tk
import math
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

            # Validaciones
            if lam <= 0 or mu <= 0:
                messagebox.showerror("Error", "λ y μ deben ser mayores que 0.")
                return
            if k <= 0 or f <= 0:
                messagebox.showerror("Error", "K y F deben ser números enteros positivos.")
                return
            if f < k:
                messagebox.showerror("Error", "F debe ser mayor o igual que K.")
                return
            if lam >= k * mu:
                messagebox.showerror("Error", "El sistema no es estable. λ debe ser menor que K * μ.")
                return

            # Probabilidades de estado
            rho = lam / mu
            p0 = 0

            # Suma para estados 0 a K-1
            for n in range(k):
                p0 += (rho ** n) / math.factorial(n)

            # Suma para estados K a F
            for n in range(k, f + 1):
                p0 += (rho ** n) / (math.factorial(k) * (k ** (n - k)))
            p0 = 1 / p0  # Probabilidad de que no haya clientes en el sistema

            # Probabilidad de rechazo (estado F lleno)
            p_f = (rho ** f) / (math.factorial(k) * (k ** (f - k))) * p0

            # Probabilidad de que todos los servidores estén ocupados
            pw = ((rho ** k) / math.factorial(k)) * (1 - (rho / k) ** (f - k + 1)) / (1 - (rho / k)) * p0

            # Rendimiento
            lq = pw * (rho / k) / (1 - (rho / k))  # Número promedio en la cola
            ls = lq + (rho * (1 - p_f))  # Número promedio en el sistema
            wq = lq / (lam * (1 - p_f))  # Tiempo promedio en la cola
            ws = wq + (1 / mu)  # Tiempo promedio en el sistema

            # Mostrar resultados
            open_results_interface("M/M/K/F", rho, wq, ws, lq, ls, p_f, lam, mu)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    calculate_button = ttk.Button(root, text="Calcular", command=calculate)
    calculate_button.grid(row=1, column=0, padx=10, pady=10)
