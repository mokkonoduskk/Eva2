#**Proyecto**
#- id int
#- nombre string
#- descripcion string
#- fecha inicio date
class Proyecto:

    

    def __init__(self, id:int, nombre:str, descripcion:str, fecha_inicio:int):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
       

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
    def descripciom(self)-> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self,descripcion:str)-> None:
        self._descripcion = descripcion


    @property
    def fecha_inicio(self)->int:
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self,fecha_inicio:int)-> None:
        self._fecha_inicio = fecha_inicio
    

    def __str__(self)-> str:
        return f"Información de proyecto:\nID: {self.id}\nNombre: {self.nombre}\nDescripcion: {self.descripcion}\nFecha_inicio: {self.fecha_inicio}"

    def __repr__(self)-> str:
        return f"proyecto(id='{self.id}', nombre='{self.nombre}', descripcion='{self.descripcion}'fecha_inicio='{self.fecha_inicio})"
