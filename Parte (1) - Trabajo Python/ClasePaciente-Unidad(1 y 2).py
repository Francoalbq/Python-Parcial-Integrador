import datetime

class Paciente:
    def __init__(self, codigo_paciente):
        self.codigo_paciente = codigo_paciente
        self.datos_medicos = []
    
    def agregar_datos(self, nombre, edad, historial, medicacion):
        listado = [nombre, edad, historial, medicacion]
        self.datos_medicos.append(listado)
        
    def eliminar_datos(self, dato_eliminar):
        encontrado = False
        for i in self.datos_medicos:
            if i[0] == dato_eliminar:
                self.datos_medicos.remove(i)
                encontrado = True
                break
        if encontrado:
            print(f"Se eliminó correctamente el dato: {dato_eliminar}")
        else:
            print("No se encontró el dato a eliminar.")
    
    def info(self):
        return f'ID es: {self.codigo_paciente}\n{self.datos_medicos}'
    
    def busqueda_recursiva(self, medicamento, index=0):
        # caso base
        if index >= len(self.datos_medicos):
            return f"Medicamento '{medicamento}' no encontrado."
        
        if self.datos_medicos[index][3] == medicamento:
            return f"El Medicamento '{medicamento}' encontrado en el historial clínico del paciente."
        
        # llamada recursiva, incrementando el índice
        return self.busqueda_recursiva(medicamento, index + 1)


el_paciente = Paciente(182)
el_paciente.agregar_datos('Juan Raúl', '23/03/1966', 'Neumonia', 'Geniol 10mg')
el_paciente.agregar_datos('Ana Pérez', '12/05/1980', 'Asma', 'Ventolin 100mg')

print(el_paciente.info())

print(el_paciente.busqueda_recursiva('Geniol 10mg'))
print(el_paciente.busqueda_recursiva('Aspirina'))

# calcula y muestra el tiempo de ejecución del codigo
print()
inicio = datetime.datetime.now()
fin = datetime.datetime.now()
tiempo_ejecucion = fin - inicio
print(f"\nTiempo de ejecución: {tiempo_ejecucion}")