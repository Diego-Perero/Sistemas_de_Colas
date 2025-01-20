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

            if lam >= k * mu:
                messagebox.showerror("Error", "La tasa de llegada debe ser menor que K * μ.")
                return

            # Factor de utilización
            rho = lam / mu
            utilization = rho / k

            # Probabilidad de que no haya clientes en el sistema (P0)
            p0_sum = sum((rho ** n) / math.factorial(n) for n in range(k))
            p0_sum += sum((rho ** n) / (math.factorial(k) * (k ** (n - k))) for n in range(k, f + 1))
            p0 = 1 / p0_sum

            # Probabilidad de que el sistema esté lleno (P(F))
            pf = (rho ** f) / (math.factorial(k) * (k ** (f - k))) * p0

            # Número promedio de clientes en la cola (Lq)
            if lam / (k * mu) < 1:
                lq = (p0 * ((rho ** k) * (lam / (k * mu)) / (math.factorial(k) * (1 - lam / (k * mu)) ** 2)) *
                    (1 - (lam / (k * mu)) ** (f - k + 1) - (1 - lam / (k * mu)) * (f - k + 1) * (lam / (k * mu)) ** (f - k)))
            else:
                lq = 0

            # Número promedio de clientes en el sistema (Ls)
            ls = lq + (lam / mu) * (1 - pf)

            # Tiempo promedio en la cola (Wq)
            wq = lq / (lam * (1 - pf))

            # Tiempo promedio en el sistema (Ws)
            ws = wq + (1 / mu)

            # Mostrar resultados
            open_results_interface("M/M/K/F", utilization, wq, ws, lq, ls, pf, p0, lam, mu, k, f)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    calculate_button = ttk.Button(root, text="Calcular", command=calculate)
    calculate_button.grid(row=1, column=0, padx=10, pady=10)
