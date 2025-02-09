
import tkinter as tk

def convertir():
    try:    
        grados = float(entry.get())
        resultado = grados * 9/5 + 32
        label_resultado.config(text=f"{resultado}°F")
    except:
        label_resultado.config(text="Ingrese un valor valido")
    finally:
        entry.delete(0, tk.END)
        
root = tk.Tk()
root.title("Conversor de Temperatura")
root.geometry("500x150")


entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

label_resultado = tk.Label(root, text="Ingrese los grados Celsius", fg="blue")
label_resultado.pack(padx=10, pady=10)


button = tk.Button(root, text="Convertir", command=convertir)
button.pack(padx=10, pady=10)



if __name__ == "__main__":
    root.mainloop()
