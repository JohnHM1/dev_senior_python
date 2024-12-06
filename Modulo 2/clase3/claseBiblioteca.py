class Libro:

    def __init__(self, headline, autor):
        self.headline = headline
        self.autor = autor

    def descripition(self):
        return f"Libro: {self.headline} Autor: {self.autor}"

    def __str__(self):
        return f"Libro: {self.headline} Autor: {self.autor}"

class LibroDigital(Libro):

    def __init__(self, headline, autor, formatt):
        super().__init__(headline, autor)
        self.formatt = formatt
        

    def description(self):#Polimorfismo largo y duro
        return f"Libro: {self.headline} Autor: {self.autor} Formato {self.formatt}"

    def __str__(self):#Polimorfismo largo y duro
        return f"Libro: {self.headline} Autor: {self.autor} Formato {self.formatt}"
    
libro1 = Libro("La peste","Albert Camu")
LibroDigital1 = LibroDigital("Conde de montecristo","Alejandro dumas", "Digital")

print(libro1.descripition())
print(LibroDigital1.__str__())




