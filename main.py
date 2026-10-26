from empleado import Empleado
empleados:list[Empleado]=[
        Empleado(1,"Juan Perez",30,"Calle 1",123456789,"juan@empresa.com","2023-01-01",1000000),
        Empleado(2,"Maria Gonzalez",25,"Calle 2",987654321,"maria@empresa.com","2023-01-01",1000000)
    ]

def leer_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def menu():
    print("="*20)
    print("Menú EcoTech")
    print("="*20)
    print("1. - Agregar Empleado")
    print("2. - Editar Empleado")
    print("3. - Eliminar Empleado")
    print("4. - Buscar Empleado")
    print("5. - Mostrar Empleados")
    print("6. - Agregar Administrador")
    print("7. - Editar Administrador")
    print("0. - Salir")
    op=leer_numero("Ingrese una opción: ")
    print("="*20)
    return op

def agregar_empleado()-> None:
    id_empleado = leer_numero("Ingrese el ID del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    edad = leer_numero("Ingrese la edad del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    telefono = leer_numero("Ingrese el teléfono del empleado: ")
    correo = input("Ingrese el correo del empleado: ")
    inicio_contrato = input("Ingrese la fecha de inicio de contrato (YYYY-MM-DD): ")
    salario = float(input("Ingrese el salario del empleado: "))

    empleados.append(Empleado(id_empleado, nombre, edad, direccion, telefono, correo, inicio_contrato, salario))
    print("Empleado agregado exitosamente.")
    print(f"Total de empleados: {len(empleados)}")
