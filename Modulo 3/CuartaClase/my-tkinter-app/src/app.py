from tkinter import Tk, Menu
from gui import AppGUI

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mascota Management App")
        self.root.geometry("400x300")
        
        self.gui = AppGUI(root)  # Initialize AppGUI before creating the menu
        self.create_menu()

    def create_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        client_menu = Menu(menu)
        menu.add_cascade(label="Clientes", menu=client_menu)
        client_menu.add_command(label="Registrar Cliente", command=self.gui.registrar_cliente)
        
        pet_menu = Menu(menu)
        menu.add_cascade(label="Mascotas", menu=pet_menu)
        pet_menu.add_command(label="Registrar Mascota", command=self.gui.registrar_mascota)
        
        appointment_menu = Menu(menu)
        menu.add_cascade(label="Citas", menu=appointment_menu)
        appointment_menu.add_command(label="Programar Cita", command=self.gui.programar_cita)
        
        history_menu = Menu(menu)
        menu.add_cascade(label="Historial", menu=history_menu)
        history_menu.add_command(label="Consultar Historial", command=self.gui.consultar_historial)
        
        menu.add_command(label="Salir", command=self.root.quit)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()