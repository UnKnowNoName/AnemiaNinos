class Niño():
    contadorNiños = 1

    def __init__(self, nombre, apellido, edad):
        self.idNiño = Niño.contadorNiños
        Niño.contadorNiños += 1
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        # columnaNombres.append(self.nombre)
        # columnaApellidos.append(self.apellido)
        # columnaEdades.append(self.edad)

    def getId(self):
        return self.idNiño

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setEdad(self, edad):
        self.edad = edad

    def mostrarNiño(self):
        return """Niño 0{} 
    Nombre\t\t\t: {}
    Apellido\t\t\t: {}
    Edad (Meses)\t\t: {}""".format(self.idNiño, self.nombre, self.apellido, self.edad)