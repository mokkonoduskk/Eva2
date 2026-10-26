#Administrador
#- id int
#- nivel acesso string
#- usuario string
#- contraseña string

class Administrador:

    def __init__(self, id:int, nivel_acceso:str, usuario:str, contrasena:str):
        self.id = id
        self.nivel_acceso = nivel_acceso
        self.usuario = usuario
        self.contrasena = contrasena

    @property
    def id(self)-> int:
        return self._id

    @id.setter
    def id(self,id:int)-> None:
        self._id = id

    @property
    def nivel_acceso(self)-> str:
        return self._nivel_acceso

    @nivel_acceso.setter
    def nivel_acceso(self,nivel_acceso:str)-> None:
        self._nivel_acceso = nivel_acceso

    @property
    def usuario(self)-> str:
        return self._usuario

    @usuario.setter
    def usuario(self,usuario:str)-> None:
        self._usuario = usuario

    @property
    def contrasena(self)-> str:
        return self._contrasena

    @contrasena.setter
    def contrasena(self,contrasena:str)-> None:
        self._contrasena = contrasena

    def __str__(self)-> str:
            return f"Información de administrador:\nID: {self.id}\nNivel de acceso: {self.nivel_acceso}\nUsuario: {self.usuario}\nContraseña: {self.contrasena}"

    def __repr__(self)-> str:
            return f"administrador(id='{self.id}', nivel_acceso='{self.nivel_acceso}', usuario='{self.usuario}', contrasena='{self.contrasena}')"