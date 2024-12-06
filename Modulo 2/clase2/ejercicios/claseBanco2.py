class bankAccount:

    def __init__(self, headline, balance, password):
        self.headline = headline
        self._balance = balance
        self.__password = password
    
    def deposite(self, depositeTo):
        self._balance += depositeTo
        return f"Deposito exitoso. Saldo actual {self._balance}"

    def retire(self, montToRetire):
        if montToRetire > self._balance:
            return "Fondos insuficientes."
        else:
            self._balance -= montToRetire
            return f"Retiro exitoso. Saldo actual {self._balance}"

    def passwordModify(self, newPassword):
        self.__password = newPassword
        return f"Clave modificada de forma exitosa. La clave es {self.__password}"
