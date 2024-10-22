import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

class PuntoEquilibrioApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Punto de Equilibrio")

        # Variables para almacenar los valores
        self.costos_fijos = tk.DoubleVar()
        self.precio_unitario = tk.DoubleVar()
        self.costo_variable = tk.DoubleVar()

        # Título principal
        self.label_title = tk.Label(master, text="Calculadora de Punto de Equilibrio", font=("Arial", 16, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        # Etiqueta y campo de entrada para Costos Fijos
        self.label_cf = tk.Label(master, text="Costos Fijos (Q):", font=("Arial", 12))
        self.label_cf.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_cf = tk.Entry(master, textvariable=self.costos_fijos, font=("Arial", 12))
        self.entry_cf.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para Precio por Unidad
        self.label_pu = tk.Label(master, text="Precio Unitario (Q):", font=("Arial", 12))
        self.label_pu.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_pu = tk.Entry(master, textvariable=self.precio_unitario, font=("Arial", 12))
        self.entry_pu.grid(row=2, column=1, padx=10, pady=5)

        # Etiqueta y campo de entrada para Costo Variable
        self.label_cv = tk.Label(master, text="Costo Variable por Unidad (Q):", font=("Arial", 12))
        self.label_cv.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_cv = tk.Entry(master, textvariable=self.costo_variable, font=("Arial", 12))
        self.entry_cv.grid(row=3, column=1, padx=10, pady=5)

        # Botón para calcular el Punto de Equilibrio
        self.button_calculate = tk.Button(master, text="Calcular Punto de Equilibrio", command=self.calcular_y_graficar, font=("Arial", 12))
        self.button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

        # Etiqueta para mostrar los resultados
        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def calcular_y_graficar(self):
        try:
            costos_fijos = self.costos_fijos.get()
            precio_unitario = self.precio_unitario.get()
            costo_variable = self.costo_variable.get()

            # Validación de datos
            if precio_unitario <= costo_variable:
                messagebox.showerror("Error", "El precio unitario debe ser mayor que el costo variable.")
                return

            # Cálculo del punto de equilibrio
            punto_equilibrio_unidades = costos_fijos / (precio_unitario - costo_variable)
            punto_equilibrio_quetzales = precio_unitario * punto_equilibrio_unidades

            # Mostrar resultados
            self.result_label.config(
                text=f"Punto de Equilibrio:\nUnidades: {punto_equilibrio_unidades:.2f}\nQuetzales: {punto_equilibrio_quetzales:.2f}",
                fg="green"
            )

            # Graficar
            self.graficar_punto_equilibrio(costos_fijos, precio_unitario, costo_variable)

        except tk.TclError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def graficar_punto_equilibrio(self, costos_fijos, precio_unitario, costo_variable):
        # Preparar datos para la gráfica
        unidades = []
        ingresos = []
        costos = []

        for q in range(0, 500):  # Rango de cantidades
            unidades.append(q)
            ingresos.append(precio_unitario * q)
            costos.append(costos_fijos + costo_variable * q)

        # Generar la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(unidades, ingresos, label='Ingresos', color='blue')
        plt.plot(unidades, costos, label='Costos', color='orange')
        plt.axvline(x=costos_fijos / (precio_unitario - costo_variable), color='red', linestyle='--', label='Punto de Equilibrio')
        plt.xlabel('Unidades Vendidas', fontsize=12)
        plt.ylabel('Quetzales', fontsize=12)
        plt.title('Análisis de Punto de Equilibrio', fontsize=14)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x300")  # Ajusta el tamaño de la ventana si es necesario
    app = PuntoEquilibrioApp(root)
    root.mainloop()
