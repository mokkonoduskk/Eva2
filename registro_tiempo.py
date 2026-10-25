#**Registro de tiempo**
#- id int
#- fecha date
#- horas trabajadas time
#- descripcion tareas string

class Registro_tiempo:

    

    def __init__(self, id:int, fecha:int, horas_trabajo:int, descripcion_tareas:int):
        self.id = id
        self.fecha = fecha
        self.horas_trabajo = horas_trabajo
        self.descripcion_tareas = descripcion_tareas
       

    @property
    def id(self)-> int:
        return self._id

    @id.setter
    def id(self,id:int)-> None:
        self._id = id

    @property
    def fecha(self)-> int:
        return self._fecha 

    @fecha.setter
    def fecha(self,fecha:int)-> None:
        self._fecha = fecha

    @property
    def horas_trabajo(self)-> int:
        return self._horas_trabajo

    @horas_trabajo.setter
    def horas_trabajo(self,horas_trabajo:int)-> None:
        self._horas_trabajo = horas_trabajo


    @property
    def descripcion_tareas(self)->int:
        return self._descripcion_tareas

    @descripcion_tareas.setter
    def descripcion_tareas(self,descripcion_tareas:int)-> None:
        self._descripcion_tareas = descripcion_tareas
    

    def __str__(self)-> str:
        return f"Información de registro_tiempo:\nID: {self.id}\nFecha: {self.fecha}\nHoras_trabajo: {self.horas_trabajo}\nDescripcion_tareas: {self.descripcion_tareas}"

    def __repr__(self)-> str:
        return f"registro_tiempo='{self.id}', fecha='{self.fecha}', horas_trabajo='{self.horas_trabajo}'descripcion_tareas='{self.descripcion_tareas})"
