import tkinter as tk
from tkinter import ttk, messagebox
import math

def open_results_interface(model, utilization, wq, ws, lq, ls, idle_prob, lam, mu, k=None, f=None):
    def open_waiting_probabilities_interface():
        def calculate_waiting_probability():
            try:
                # Obtener los minutos ingresados
                t = float(minutes_entry.get())
                if t < 0:
                    messagebox.showerror("Error", "El número de minutos debe ser mayor o igual a 0.")
                    return

                # Calcular las probabilidades de espera
                if model == "M/M/1":
                    P_W_t = math.exp(-(mu - lam) * t)
                    P_Wq_t = utilization * math.exp(-(mu - lam) * t)
                elif model == "M/M/K":
                    # Fórmulas para M/M/K
                    P_W_t = ...  # Ajustar fórmula
                    P_Wq_t = ...  # Ajustar fórmula
                elif model == "M/G/1":
                    # Fórmulas para M/G/1
                    P_W_t = ...  # Ajustar fórmula
                    P_Wq_t = ...  # Ajustar fórmula
                elif model == "M/M/K/F":
                    # Fórmulas para M/M/K/F
                    P_W_t = ...  # Ajustar fórmula
                    P_Wq_t = ...  # Ajustar fórmula

                # Mostrar los resultados
                result_label.config(text=f"Probabilidad de esperar más de {t} minutos en el sistema: {P_W_t:.4f}")
                result_queue_label.config(text=f"Probabilidad de esperar más de {t} minutos en la cola: {P_Wq_t:.4f}")

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido.")

        # Crear ventana para ingresar minutos
        waiting_prob_window = tk.Toplevel()
        waiting_prob_window.title("Calcular Probabilidad de Espera")

        ttk.Label(waiting_prob_window, text="Ingrese los minutos a esperar:").grid(row=0, column=0, padx=10, pady=10)
        minutes_entry = ttk.Entry(waiting_prob_window)
        minutes_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = ttk.Button(waiting_prob_window, text="Calcular", command=calculate_waiting_probability)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        result_label = ttk.Label(waiting_prob_window, text="")
        result_label.grid(row=2, column=0, columnspan=2, pady=10)
        result_queue_label = ttk.Label(waiting_prob_window, text="")
        result_queue_label.grid(row=3, column=0, columnspan=2, pady=10)

    def open_probabilities_interface():
        def calculate_probabilities():
            try:
                n = int(prob_entry.get())
                if n < 0:
                    messagebox.showerror("Error", "El número debe ser mayor o igual a 0.")
                    return

                probabilities_window = tk.Toplevel()
                probabilities_window.title("Probabilidades de Estado")

                table_frame = ttk.Frame(probabilities_window)
                table_frame.grid(row=0, column=0, padx=10, pady=10)

                # Configurar tabla
                tree = ttk.Treeview(
                    table_frame,
                    columns=("Estado", "Probabilidad", "Prob. Acumulativa"),
                    show="headings",
                )
                tree.heading("Estado", text="Estado (n)")
                tree.heading("Probabilidad", text="P(n)")
                tree.heading("Prob. Acumulativa", text="P(n) Acumulativa")
                tree.column("Estado", anchor="center", width=100)
                tree.column("Probabilidad", anchor="center", width=150)
                tree.column("Prob. Acumulativa", anchor="center", width=150)
                tree.pack(padx=10, pady=10)

                # Calcular probabilidades
                prob_sum = 0
                for i in range(n + 1):
                    if model == "M/M/1":
                        prob = (lam / mu) ** i * (1 - lam / mu)
                    elif model == "M/M/K":
                        # Fórmulas para M/M/K
                        prob = ...  # Ajustar fórmula
                    elif model == "M/G/1":
                        # Fórmulas para M/G/1
                        prob = ...  # Ajustar fórmula
                    elif model == "M/M/K/F":
                        # Fórmulas para M/M/K/F
                        prob = ...  # Ajustar fórmula
                    prob_sum += prob
                    prob_sumn = 1 - prob_sum  # suma total
                    tree.insert("", "end", values=(i, f"{prob:.4f}", f"{prob_sum:.4f}"))

                # Mostrar probabilidad acumulada total
                total_prob_label.config(text=f"Probabilidad acumulada total para n={n}: {prob_sumn:.2%}")

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")

        probabilities_window = tk.Toplevel()
        probabilities_window.title("Calcular Probabilidades")

        ttk.Label(probabilities_window, text="Ingrese el número de estados (n):").grid(row=0, column=0, padx=10, pady=10)
        prob_entry = ttk.Entry(probabilities_window)
        prob_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = ttk.Button(probabilities_window, text="Calcular", command=calculate_probabilities)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        total_prob_label = ttk.Label(probabilities_window, text="")
        total_prob_label.grid(row=2, column=0, columnspan=2, pady=10)

    results_window = tk.Toplevel()
    results_window.title(f"Resultados del Modelo {model}")

    results_frame = ttk.Frame(results_window)
    results_frame.grid(row=0, column=0, padx=10, pady=10)

    tree = ttk.Treeview(results_frame, columns=("Metric", "Result"), show="headings")
    tree.heading("Metric", text="Métrica")
    tree.heading("Result", text="Resultado")
    tree.column("Metric", anchor="w", width=300)
    tree.column("Result", anchor="center", width=150)

    results = [
        ("Utilización del sistema (P)", f"{utilization:.2f}"),
        ("Tiempo promedio en cola (Wq)", f"{wq:.2f} minutos"),
        ("Tiempo promedio en el sistema (Ws)", f"{ws:.2f} minutos"),
        ("Número promedio en cola (Lq)", f"{lq:.2f}"),
        ("Número promedio en el sistema (Ls)", f"{ls:.2f}"),
    ]
    if idle_prob is not None:
        results.append(("Probabilidad de sistema desocupado", f"{idle_prob:.2%}"))

    # if model == "M/M/K/F":
        # Añadir métricas específicas para M/M/K/F
        # results.append(("Probabilidad de rechazo (P_rechazo)", f"{idle_prob:.2%}"))
        # results.append(("Número promedio de clientes en el sistema (L)", f"{ls:.2f}"))
        # results.append(("Tiempo promedio en el sistema (W)", f"{ws:.2f} minutos"))

    if model in ["M/M/1", "M/M/K", "M/G/1", "M/M/K/F"]:
        waiting_prob_button = ttk.Button(results_window, text="Calcular Probabilidad de Esperar Más de X Minutos",
                                         command=open_waiting_probabilities_interface)
        waiting_prob_button.grid(row=2, column=0, padx=10, pady=10)

        prob_button = ttk.Button(results_window, text="Calcular Probabilidades de Estado",
                                 command=open_probabilities_interface)
        prob_button.grid(row=3, column=0, padx=10, pady=10)

    for metric, result in results:
        tree.insert("", "end", values=(metric, result))

    tree.pack(padx=10, pady=10)