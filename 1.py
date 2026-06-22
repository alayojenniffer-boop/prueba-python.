estudiante=[]
def validar_nombre(nombre):
    return nombre.strip()!=" "
def validar_edad(edad):
    return edad > 0
def validar_nota(nota):
    return nota >= 0
def mostrar_menu():
    print("\n====Menú principal====")
    print("1.Agregar estudiante")
    print("2.Buscar estudiante")
    print("3.Eliminar estudiante")
    print("4.Actualizar estados")
    print("5.Mostrar estudiantes")
    print("6.Salir")
    print("=========================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opcion: "))
            if 1 <= opcion <= 6:
             return opcion
        
            else:
              print("Debe ingresar una opcion entre 1 y 6")
            
        except ValueError:
            print("Debe ingresar un numero valido")
def agregar_estudiante(lista_estudiantes):
    nombre =input("Ingrese nombre del estudiante: ")
    if not validar_nombre(nombre):
        print("Error: nombre invalido")
        return
    try:
        busqueda=input("Ingrese nombre del estudiante que busca: ")
    except ValueError:
        print("Estudiante no encontrado")
        return
    if not validar_nombre(nombre):
        print("Error: no registrado")
        return
    try:
        edad =int(input("Ingrese la edad del estudiante: "))
    except ValueError:
        print("La edad tiene que ser un numero entero")
        return
    if not validar_edad(edad):
        print("La edad debe ser positiva")
        return
    
    try:
        nota=float(input("Ingrese la nota del estudiante: "))
    except ValueError:
        print("Error: La nota debe ser un numero entero")
        return
    if not validar_nota(nota):
        print("Error: La nota no puede ser negativa")
        return
    estudiante= {
        "nombre" : nombre,
        "nota" : nota,
        "edad" : edad,
        "estado" :False
    }
    lista_estudiantes.appened(estudiante)
    print("Estudiante agregado correctamente")
def buscar_estudiante(lista_estudiante,nombre_buscar):
    for posicion in range(len(lista_estudiante)):
        if lista_estudiante[posicion]["nombre"]== nombre_buscar:
            return posicion
        return -1
def eliminar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    posicion= buscar_estudiante(lista_estudiantes,nombre)
    if posicion!= -1:
        lista_estudiantes.pop(posicion)
        print("Estudiante eliminado correctamente")
    else:
        print(f"El estudiante'{nombre}' no se encuentra registrado")
def actualizar_estudiante(lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante ["cantidad"] >0:
            estudiante["Encontrado"]= True
        else:
            estudiante["Encontrado"]= False
    print("Actualizacion ejecutada correctamente")
def mostrar_estudiantes(lista_estudiantes):
    if len(lista_estudiantes)==0:
        print("No existen estudiantes registrados")
        return
    print("\n==Lista de estudiantes==")
    for estudiante in lista_estudiantes:
        estado="Encontrado"
        if not estudiante["Encontrado"]:
            estado= "No encontrado"
        print(f"\n Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota: {estudiante[nota]}")
        print(f"Estado: {estado['estado']}")
        print("*"*40)
while True:
    mostrar_menu()
    opcion= leer_opcion()
    if opcion==1:
        agregar_estudiante
    elif opcion==2:
        nombre=input("Ingrese nombre del estudiante a buscar: ")
        posicion= buscar_estudiante(estudiante, nombre)
        if posicion!=-1:
         estudiante=estudiante[posicion]
         print("\n Estudiante encontrado")
         print(f"Posicion:{posicion}")
         print(f"Nombre:{estudiante['nombre']}")
         print(f"Nota: {estudiante['nota']}")
         print(f"Estado: {estudiante['aprobado']}")
        else:
         print("Estudiante no encontrado")
    elif opcion ==3:
        eliminar_estudiante(estudiante)
    elif opcion==4:
     actualizar_estudiante(estudiante)
    elif opcion==5:
      mostrar_estudiantes(estudiante)
    elif opcion==6:
     print("Gracias por usar el sistema .Vuelve pronto")
     break
