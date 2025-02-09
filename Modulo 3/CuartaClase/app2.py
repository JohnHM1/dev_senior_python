from logging import root
import tkinter as tk
from tkinter import messagebox
import datetime
from dataclasses import dataclass
from tkinter import ttk

@dataclass
class Vehiculo:
    placa: str
    horaEntrada: datetime.datetime

    def calcularPrecio(self):
        horaSalida = datetime.datetime.now()
        tiempo = horaSalida - self.horaEntrada
        segundos = tiempo.total_seconds()
        horas = segundos / 3600
        return horas * 1000
    

@dataclass
class App:
    root: tk.Tk

    def __post_init__(self):
        self.root.title("App de estacionamiento")
        self.root.geometry("400x400")
        self.Vehiculos = []

        self.label = tk.Label(self.root, text="Placa")
        self.entry = tk.Entry(self.root)
        self.label.pack(pady=10)
        self.entry.pack(pady=10)

        self.guardar_button = tk.Button(self.root, text="Guardar", command=self.guardar)
        self.calcular_button = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.guardar_button.pack(pady=10)
        self.calcular_button.pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Placa", "Fecha de entrada"), show='headings')
        self.tree.heading("Placa", text="Placa")
        self.tree.heading("Fecha de entrada", text="Fecha de entrada")
        self.tree.pack(pady=10, fill='both', expand=True)

    def guardar(self):
        # Implementar la lógica para guardar los datos
        placa = self.entry.get()

        for v in self.Vehiculos:
            if v.placa == placa:
                messagebox.showerror("Upps", "La placa ya está registrada")
                return
            
        horaEntrada = datetime.datetime.now()
        vehiculo = Vehiculo(placa, horaEntrada)
        self.Vehiculos.append(vehiculo)
        self.tree.insert("", "end", values=(placa, horaEntrada))

        

    def calcular(self):
        # Implementar la lógica para calcular los datos
        placa = self.entry.get()
        for vehiculo in self.Vehiculos:
            if vehiculo.placa == placa:
                precio = vehiculo.calcularPrecio()
                messagebox.showinfo("Precio", f"El precio a pagar es: {precio}")

                for item in self.tree.get_children():
                    if self.tree.item(item, "values")[0] == placa:
                        self.tree.delete(item)
                        self.Vehiculos.remove(vehiculo)
                        messagebox.showinfo("Vehículo eliminado", f"El vehículo {placa} ha sido eliminado")
                        break
                return
        messagebox.showerror("Error", "No se encontró el vehículo")
        
        
            



if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()



