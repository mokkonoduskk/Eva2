###Persona
#- id int
#- nombre string
#- rut string
#- direccion string
#- telefono int
#- correo string
class Persona:

    

    def __init__(self, id:int, nombre:str, rut:str, direccion:str, telefono:int, correo:str):
        self.id = id
        self.nombre = nombre
        self.rut = rut
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    @property
    def id(self)-> int:
        return self._id

    @id.setter
    def id(self,id:int)-> None:
        self._id = id

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)-> None:
        self._nombre = nombre

    @property
    def rut(self)-> str:
        return self._rut

    @rut.setter
    def rut(self,rut:str)-> None:
        self._rut = rut

    @property
    def direccion(self)->str:
        return self._direccion

    @direccion.setter
    def direccion(self,direccion:str)-> None:
        self._direccion = direccion

    @property
    def telefono(self)->int:
        return self._telefono

    @telefono.setter
    def telefono(self,telefono:int)-> None:
        self._telefono = telefono
    
    @property
    def correo(self)->str:
        return self._correo

    @correo.setter
    def direccion(self,correo:str)-> None:
        self._correo = correo

    def __str__(self)-> str:
        return f"Información de persona:\nID: {self.id}\nNombre: {self.nombre}\nRut: {self.rut}\nDireccion: {self.direccion}\nTelefono: {self.telefono}\nCorreo: {self.correo}"

    def __repr__(self)-> str:
        return f"persona(id='{self.id}', nombre='{self.nombre}', rut={self.rut}, direccion='{self.direccion}'telefono='{self.telefono}correo='{self.correo})"
