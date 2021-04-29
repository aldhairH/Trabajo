class Persona:
    def __init__(self, nombre, apellido, edad, deporte, color, telefono):
        self.nombre = nombre   
        self.apellido = apellido
        self.edad = edad
        self.deporte = deporte
        self.color = color
        self.telefono = telefono
    def saluda(self, otra_persona):
        return f"Hola, cual es  tu nombre {otra_persona.nombre}, mi nombre es {self.nombre}"
    def Papellido(slef, Aotra_persona):
        return f"Y tu apellido {Aotra_persona.apellido}, mi apellido es {self.apellido}" 
    def Pedad(self, Eotra_persona):
        return f"cual es tu edad {Eotra_persona.edad}, mi edad es {self.edad}"
    