class Historial():
    def __init__(self, niño):
        self.idHistorial = niño.getId()
        self.hemoglobina = []
        self.nivelRiesgo = ""

    def registraHemoglobina(self, hemoglobina):
        if (hemoglobina > 0):
            self.hemoglobina.append(hemoglobina)
            self.getNivelRiesgo()
        else:
            print("""[ERROR]
    Por favor, llenar correctamente los campos""")

    def getNivelRiesgo(self):
        actual = self.hemoglobina[-1]
        if (actual < 7.0):
            self.nivelRiesgo = "Severo"
            self.tratamiento = "Sulfato ferroso"
        elif (actual < 10.0):
            self.nivelRiesgo = "Moderado"
            self.tratamiento = "Micronutrientes en polvo"
        elif (actual < 11.0):
            self.nivelRiesgo = "Leve"
            self.tratamiento = "Hierro polimaltosado"
        else:
            self.nivelRiesgo = "No presenta"
            self.tratamiento = "No requiere"
        return self.nivelRiesgo

    def getHemoglobina(self):
        return self.hemoglobina

    def getTratamiento(self):
        return self.tratamiento