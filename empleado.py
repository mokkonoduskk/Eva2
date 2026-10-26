#Empleado
#- id empleado int
#- nombre string
#- edad int
#- direccion string
#- telefono int
#- correo string
#- inicio contrato date
#- salario float
from datetime import date

class Empleado:

    def __init__(self, id_empleado:int, nombre:str, edad:int, direccion:str, telefono:int, correo:str, inicio_contrato:date, salario:float):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.inicio_contrato = inicio_contrato
        self.salario = salario

    @property
    def id_empleado(self)-> int:
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self,id_empleado:int)-> None:
        self._id_empleado = id_empleado

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)-> None:
        self._nombre = nombre

    @property
    def edad(self)-> int:
        return self._edad

    @edad.setter
    def edad(self,edad:int)-> None:
        self._edad = edad

    @property
    def direccion(self)-> str: 
        return self._direccion

    @direccion.setter
    def direccion(self,direccion:str)-> None:
        self._direccion = direccion

    @property
    def telefono(self)-> int:
        return self._telefono

    @telefono.setter
    def telefono(self,telefono:int)-> None:
        self._telefono = telefono

    @property
    def correo(self)-> str:
        return self._correo

    @correo.setter
    def correo(self,correo:str)-> None:
        self._correo = correo

    @property
    def inicio_contrato(self)-> date:
        return self._inicio_contrato

    @inicio_contrato.setter
    def inicio_contrato(self,inicio_contrato:date)-> None:
        self._inicio_contrato = inicio_contrato

    @property
    def salario(self)-> float:
        return self._salario

    @salario.setter
    def salario(self,salario:float)-> None:
        self._salario = salario

    def __str__(self)-> str:
            return f"Información de empleado:\nID: {self.id_empleado}\nNombre: {self.nombre}\nEdad: {self.edad}\nDireccion: {self.direccion}\nTelefono: {self.telefono}\nCorreo: {self.correo}\nInicio Contrato: {self.inicio_contrato}\nSalario: {self.salario}"

    def __repr__(self)-> str:
            return f"empleado(id='{self.id_empleado}', nombre='{self.nombre}', edad={self.edad}, direccion='{self.direccion}', telefono={self.telefono}, correo='{self.correo}', inicio_contrato='{self.inicio_contrato}', salario={self.salario})"