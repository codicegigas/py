from abc import ABC, abstractmethod

class ClaseBase(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"