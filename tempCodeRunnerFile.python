import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def open_main_interface():
    # Cerrar la ventana de inicio
    start_window.destroy()

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Modelo de Colas M/M/1")

    # Frame de entrada de datos
    input_frame = ttk.LabelFrame(root, text="Entradas")
    input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    # Descripciones y campos de entrada
    descriptions = [
        "Número de Servicios (S):",
        "Tasa de llegada (λ):",
        "Tasa de Servicio (μ):",
    ]

    entries = []  # Lista para guardar las entradas

    for i, desc in enumerate(descriptions):
        # Etiqueta de descripción
        desc_label = ttk.Label(input_frame, text=desc)
        desc_label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

        # Campo de entrada
        entry = ttk.Entry(input_frame)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    # Botón de cálculo
    def calculate():
        try:
            # Obtener valores ingresados
            s = int(entries[0].get())  # Número de servicios
            lam = float(entries[1].get())  # Tasa de llegada
            mu = float(entries[2].get())  # Tasa de servicio

            if s != 1:
                messagebox.showerror("Error", "El número de servicios debe ser 1 para un modelo M/M/1.")
                return
            
            if lam >= mu:
                messagebox.showerror("Error", "La tasa de llegada debe ser menor que la tasa de servicio.")
                return

            # Calcular métricas principales
            utilization = lam / mu  # Utilización del sistema
            wq = lam / (mu * (mu - lam))  # Tiempo promedio en cola
            ws = wq + (1 / mu)  # Tiempo promedio en el sistema
            lq = lam * wq  # Número promedio en cola
            ls = lam * ws  # Número promedio en el sistema
            idle_prob = 1 - utilization  # Probabilidad de sistema desocupado

            # Abrir la ventana de resultados
            open_results_interface(utilization, wq, ws, lq, ls, idle_prob, s, lam, mu)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    calculate_button = ttk.Button(root, text="Calcular", command=calculate)
    calculate_button.grid(row=1, column=0, padx=10, pady=10)

    # Iniciar el bucle principal de la interfaz
    root.mainloop()

def open_results_interface(utilization, wq, ws, lq, ls, idle_prob, s, lam, mu):
    # Crear la ventana de resultados
    results_window = tk.Toplevel()
    results_window.title("Resultados del Modelo M/M/1")

    # Frame para resultados
    results_frame = ttk.Frame(results_window)
    results_frame.grid(row=0, column=0, padx=10, pady=10)

    # Tabla de resultados
    tree = ttk.Treeview(results_frame, columns=("Metric", "Result"), show="headings")
    tree.heading("Metric", text="Métrica")
    tree.heading("Result", text="Resultado")
    tree.column("Metric", anchor="w", width=300)
    tree.column("Result", anchor="center", width=150)

    # Inicializar la lista de resultados
    results = [
        ("Utilización del sistema (P)", f"{utilization:.2f}"),
        ("Tiempo promedio en cola (Wq)", f"{wq:.2f} minutos"),
        ("Tiempo promedio en el sistema (Ws)", f"{ws:.2f} minutos"),
        ("Número promedio en cola (Lq)", f"{lq:.2f}"),
        ("Número promedio en el sistema (Ls)", f"{ls:.2f}"),
        ("Probabilidad de sistema desocupado", f"{idle_prob:.2%}")
    ]

    # Si el número de servicios es 1, insertar al inicio "Sistema: M/M/1"
    if s == 1:
        results.insert(0, ("Sistema", "M/M/1"))

    # Insertar los resultados en la tabla
    for metric, result in results:
        tree.insert("", "end", values=(metric, result))

    tree.pack(padx=10, pady=10)

    # Función para calcular probabilidades de espera
    def open_waiting_probabilities_interface():
        def calculate_waiting_probability():
            try:
                # Obtener los minutos ingresados
                t = float(minutes_entry.get())
                if t < 0:
                    messagebox.showerror("Error", "El número de minutos debe ser mayor o igual a 0.")
                    return

                # Calcular la probabilidad de esperar más de t minutos en el sistema
                P_W_t = math.exp(-(mu - lam) * t)

                # Calcular la probabilidad de esperar más de t minutos en la cola
                P_Wq_t = utilization * math.exp(-(mu - lam) * t)

                # Mostrar los resultados
                result_label = ttk.Label(waiting_prob_window, text=f"Probabilidad de esperar más de {t} minutos en el sistema: {P_W_t:.4f}")
                result_label.grid(row=2, column=0, padx=10, pady=10)

                result_queue_label = ttk.Label(waiting_prob_window, text=f"Probabilidad de esperar más de {t} minutos en la cola: {P_Wq_t:.4f}")
                result_queue_label.grid(row=3, column=0, padx=10, pady=10)

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido.")

        # Crear la ventana para ingresar minutos
        waiting_prob_window = tk.Toplevel()
        waiting_prob_window.title("Calcular Probabilidad de Espera")

        minutes_label = ttk.Label(waiting_prob_window, text="Ingrese los minutos a esperar:")
        minutes_label.grid(row=0, column=0, padx=10, pady=10)

        minutes_entry = ttk.Entry(waiting_prob_window)
        minutes_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = ttk.Button(waiting_prob_window, text="Calcular", command=calculate_waiting_probability)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Botón para calcular la probabilidad de esperar más de t minutos
    waiting_prob_button = ttk.Button(results_window, text="Calcular Probabilidad de Esperar Más de X Minutos", command=open_waiting_probabilities_interface)
    waiting_prob_button.grid(row=2, column=0, padx=10, pady=10)

    # Función para calcular las probabilidades de los estados
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

                # Configurar Treeview con columnas
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

            # Calcular probabilidades y acumulativas
                # Inicializar una variable para la suma acumulativa de las probabilidades
                prob_sum = 0
                for i in range(n + 1):
                    prob = (lam / mu) ** i * (1 - lam / mu)  # P(n)
                    prob_sum += prob  # Suma acumulativa
                    prob_sumn = 1- prob_sum #suma total
                    tree.insert("", "end", values=(i, f"{prob:.4f}", f"{prob_sum:.4f}"))

                # Mostrar resultado adicional (probabilidad acumulada total)
                result_label = ttk.Label(
                    probabilities_window,
                    text=f"Probabilidad acumulada total para n={n}: {prob_sumn:.2%}",
                )
                result_label.grid(row=1, column=0, padx=10, pady=10)

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")

        probabilities_window = tk.Toplevel()
        probabilities_window.title("Calcular Probabilidades")

        prob_label = ttk.Label(probabilities_window, text="Ingrese el número de estados (n):")
        prob_label.grid(row=0, column=0, padx=10, pady=10)

        prob_entry = ttk.Entry(probabilities_window)
        prob_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = ttk.Button(probabilities_window, text="Calcular", command=calculate_probabilities)
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Botón para calcular probabilidades de los estados
    prob_button = ttk.Button(results_window, text="Calcular Probabilidades de Estado", command=open_probabilities_interface)
    prob_button.grid(row=3, column=0, padx=10, pady=10)

# Crear la ventana inicial
start_window = tk.Tk()
start_window.title("Especificación del Problema")

# Configurar la interfaz inicial
frame = ttk.LabelFrame(start_window, text="Problem Specification")
frame.grid(row=0, column=0, padx=10, pady=10)

title_label = ttk.Label(frame, text="Título del Problema:")
title_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
title_entry = ttk.Entry(frame)
title_entry.grid(row=0, column=1, padx=5, pady=5)

# Botones
button_frame = ttk.Frame(start_window)
button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

ok_button = ttk.Button(button_frame, text="OK", command=open_main_interface)
ok_button.grid(row=0, column=0, padx=5, pady=5)

cancel_button = ttk.Button(button_frame, text="Cancel", command=start_window.destroy)
cancel_button.grid(row=0, column=1, padx=5, pady=5)

# Iniciar la ventana de inicio
start_window.mainloop()
