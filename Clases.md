**Persona**
- id int
- nombre string
- rut string
- direccion string
- telefono int
- correo string

**Administrador**
- id int
- nivel acesso string
- usuario string
- contraseña string

**Empleado**
- id empleado int
- nombre string
- edad int
- direccion string
- telefono int
- correo string
- inicio contrato date
- salario float

**Departamento**
- id int
- nombre string
- gerente asociado int

**Proyecto**
- id int
- nombre string
- descripcion string
- fecha inicio date

**Registro de tiempo**
- id int
- fecha date
- horas trabajadas time
- descripcion tareas string