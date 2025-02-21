from typing import Set

def getUniqueClients(clients: Set[str], newClients: Set[str]) -> Set[str]:
    return clients.union(newClients)



def manageClients(clients: Set[str])-> None:

    #Add new clients
    clients.add("John Doe")
    print(f"New clients added: {clients}")

    #Remove clients
    clients.discard("Jane Doe")
    print(f"Client removed: {clients}")

    #Discard non-existent client
    clients.discard("Mary Smith")
    print(f"Client discard: {clients}") # la diferecia es que no arroja error si el elemento no existe en el set

    #Pop client
    client = clients.pop()
    print(f"Client popped: {client}")  # Devuelve el ultimo elemento y lo elimina del set

    #clear clients
    clients.clear()
    print(f"All clients cleared: {clients}")


def main():
    oldClients = {'Juan', 'Maria', 'Pedro'}
    newClients = {'Jane', 'Mariam', 'Ana'}
    uniqueClients = getUniqueClients(oldClients, newClients)
    print(f"Unique clients: {uniqueClients}")
    manageClients(uniqueClients)

if __name__ == "__main__":
    main()