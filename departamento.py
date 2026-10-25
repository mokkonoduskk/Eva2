#**Departamento**
#- id int
#- nombre string
#- gerente asociado int
class Departamento :
 

    def __init__(self, id:int, nombre:str, gerente_asociado:int,):
        self.id = id
        self.nombre = nombre
        self.gerente_asociado = gerente_asociado

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
    def gerente_asociado(self)-> int:
        return self._gerente_asociado

    @gerente_asociado.setter
    def gerente_asociado(self,gerente_asociado:int)-> None:
        self._gerente_asociado = gerente_asociado

   

    def __str__(self)-> str:
        return f"Información de departamento:\nID: {self.id}\nNombre: {self.nombre}\nGerente: {self.gerente_asociado}"

    def __repr__(self)-> str:
        return f"departamento(id='{self.id}', nombre='{self.nombre}','gerente'{self.gerente_asociado})"
