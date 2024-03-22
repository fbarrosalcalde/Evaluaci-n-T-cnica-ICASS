# Links utilizados: 
# - https://www.geeksforgeeks.org/inheritance-in-python/
# - https://www.geeksforgeeks.org/abstract-classes-in-python/

from abc import ABC, abstractmethod
import random

class Hormiga(ABC):  # Clase abstracta base para representar una hormiga
    ultimo_id = 0

    def __init__(self, nombre, tipo, edad, id_colonia):
        self.id = Hormiga.ultimo_id
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.estado = True  # Estado predeterminado como vivo
        self.id_colonia = id_colonia
        Hormiga.ultimo_id += 1  # Incrementa el ID para la próxima instancia

    @abstractmethod
    def comunicarse(self):
        """Método abstracto para que la hormiga se comunique con otras hormigas mediante feromonas."""
        pass

    def imprimir_info(self):
        estado = "viva" if self.estado else "muerta"  # Determina el estado de la hormiga
        print(f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo}, Edad: {self.edad}, ID Colonia: {self.id_colonia}, Estado: {estado}")


class Reina(Hormiga):
    def __init__(self, nombre, edad, id_colonia):
        super().__init__(nombre, "Reina", edad, id_colonia)
        self.huevos_diarios = random.randint(20, 50)  # Número aleatorio de huevos diarios

    def poner_huevos(self):
        pass  # Lógica para poner huevos

    def comunicarse(self):
        pass  # Lógica para que la Reina se comunique


class Princesa(Hormiga):
    def __init__(self, nombre, edad, id_colonia):
        super().__init__(nombre, "Princesa", edad, id_colonia)

    def iniciar_vuelo_nupcial(self):
        pass  # Lógica para iniciar el vuelo nupcial

    def comunicarse(self):
        pass  # Lógica para que la Princesa se comunique


class Principe(Hormiga):
    def __init__(self, nombre, edad, id_colonia):
        super().__init__(nombre, "Príncipe", edad, id_colonia)

    def fecundar_princesa(self):
        pass  # Lógica para fecundar a la princesa

    def comunicarse(self):
        pass  # Lógica para que el Príncipe se comunique


class Nodriza(Hormiga):
    def __init__(self, nombre, edad, id_colonia):
        super().__init__(nombre, "Nodriza", edad, id_colonia)

    def cuidar_huevos(self):
        pass  # Lógica para cuidar los huevos

    def comunicarse(self):
        pass  # Lógica para que la Nodriza se comunique


class Obrera(Hormiga):
    def __init__(self, nombre, edad, id_colonia):
        super().__init__(nombre, "Obrera", edad, id_colonia)

    def buscar_alimento(self):
        pass  # Lógica para buscar alimento

    def proveer_alimento(self):
        pass  # Lógica para proveer alimento

    def comunicarse(self):
        pass  # Lógica para que la Obrera se comunique


class Soldado(Hormiga):
    def __init__(self, nombre, edad, id_colonia):
        super().__init__(nombre, "Soldado", edad, id_colonia)

    def defender_hormiguero(self):
        pass  # Lógica para defender el hormiguero

    def atacar_otro_hormiguero(self):
        pass  # Lógica para atacar otro hormiguero

    def comunicarse(self):
        pass  # Lógica para que la hormiga Soldado se comunique


class Sepulturera(Hormiga):
    def __init__(self, nombre, edad, id_colonia):
        super().__init__(nombre, "Sepulturera", edad, id_colonia)

    def recoger_cadaveres(self):
        pass  # Lógica para recoger cadáveres

    def comunicarse(self):
        pass  # Lógica para que la Sepulturera se comunique


def crear_hormigas():
    """Crea instancias de diferentes tipos de hormigas."""
    hormigas = [
        Reina("Isabel", 5, 0),
        Princesa("Elena", 3, 0),
        Principe("Carlos", 2, 0),
        Nodriza("María", 4, 0),
        Obrera("Sofía", 1, 0),
        Soldado("Juan", 2, 0),
        Sepulturera("Ana", 3, 0)
    ]
    return hormigas


def imprimir_info_hormigas(hormigas):
    """Imprime la información de las hormigas."""
    for hormiga in hormigas:
        hormiga.imprimir_info()


if __name__ == "__main__":
    hormigas = crear_hormigas()  # Crea instancias de hormigas
    imprimir_info_hormigas(hormigas)  # Imprime la información de las hormigas
