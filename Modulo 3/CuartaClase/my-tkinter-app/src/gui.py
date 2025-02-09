from tkinter import Frame, Label, Button, Entry, StringVar, messagebox

class AppGUI:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.pack()

        self.clientes = []
        self.mascotas = []
        self.citas = []

        self.label = Label(self.frame, text="Ingrese el ID de la mascota:")
        self.label.pack()

        self.mascota_id = StringVar()
        self.entry = Entry(self.frame, textvariable=self.mascota_id)
        self.entry.pack()

        self.submit_button = Button(self.frame, text="Consultar Historial", command=self.consultar_historial)
        self.submit_button.pack()

        self.quit_button = Button(self.frame, text="Salir", command=master.quit)
        self.quit_button.pack()

    def registrar_cliente(self):
        self.clear_frame()
        Label(self.frame, text="Registrar Cliente").pack()
        Label(self.frame, text="Nombre:").pack()
        self.cliente_nombre = StringVar()
        Entry(self.frame, textvariable=self.cliente_nombre).pack()
        Label(self.frame, text="ID:").pack()
        self.cliente_id = StringVar()
        Entry(self.frame, textvariable=self.cliente_id).pack()
        Button(self.frame, text="Guardar", command=self.guardar_cliente).pack()

    def guardar_cliente(self):
        nombre = self.cliente_nombre.get()
        cliente_id = self.cliente_id.get()
        self.clientes.append({'id': cliente_id, 'nombre': nombre})
        messagebox.showinfo("Información", f"Cliente {nombre} registrado con ID {cliente_id}")

    def registrar_mascota(self):
        self.clear_frame()
        Label(self.frame, text="Registrar Mascota").pack()
        Label(self.frame, text="Nombre:").pack()
        self.mascota_nombre = StringVar()
        Entry(self.frame, textvariable=self.mascota_nombre).pack()
        Label(self.frame, text="ID:").pack()
        self.mascota_id = StringVar()
        Entry(self.frame, textvariable=self.mascota_id).pack()
        Button(self.frame, text="Guardar", command=self.guardar_mascota).pack()

    def guardar_mascota(self):
        nombre = self.mascota_nombre.get()
        mascota_id = self.mascota_id.get()
        self.mascotas.append({'id': mascota_id, 'nombre': nombre})
        messagebox.showinfo("Información", f"Mascota {nombre} registrada con ID {mascota_id}")

    def programar_cita(self):
        self.clear_frame()
        Label(self.frame, text="Programar Cita").pack()
        Label(self.frame, text="ID de la Mascota:").pack()
        self.cita_mascota_id = StringVar()
        Entry(self.frame, textvariable=self.cita_mascota_id).pack()
        Label(self.frame, text="Fecha y Hora:").pack()
        self.cita_fecha_hora = StringVar()
        Entry(self.frame, textvariable=self.cita_fecha_hora).pack()
        Button(self.frame, text="Guardar", command=self.guardar_cita).pack()

    def guardar_cita(self):
        mascota_id = self.cita_mascota_id.get()
        fecha_hora = self.cita_fecha_hora.get()
        self.citas.append({'mascota_id': mascota_id, 'fecha_hora': fecha_hora})
        messagebox.showinfo("Información", f"Cita programada para la mascota con ID {mascota_id} en {fecha_hora}")

    def consultar_historial(self):
        try:
            mascota_id = self.mascota_id.get()
            historial = [cita for cita in self.citas if cita['mascota_id'] == mascota_id]
            if historial:
                historial_texto = "\n".join([f"Fecha y Hora: {cita['fecha_hora']}" for cita in historial])
                messagebox.showinfo("Historial", f"Historial de la mascota con ID {mascota_id}:\n{historial_texto}")
            else:
                messagebox.showerror("Error", "Mascota no encontrada o sin historial.")
        except ValueError:
            messagebox.showerror("Error", "ID de mascota no válido.")

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()