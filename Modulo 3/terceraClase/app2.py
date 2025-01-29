
class  Reserva:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
    
reservas = [
    Reserva('Juan', None),
    Reserva('Pedro', '2021-01-02'),
    Reserva('Maria', '2021-01-03')
]

for reserva in reservas:
    if not reserva.fecha:
        print(f'Cliente: {reserva.cliente} no tiene fecha de reserva')
