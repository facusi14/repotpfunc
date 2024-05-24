import funcionesBiblioteca

def mostrar_menu(a, b):
    print(f"""
    menú:
    1-- ingresar primer operando (a={a})
    2-- ingresar segundo operando (b={b})
    3-- calcular operaciones
    4-- informar resultados
    5-- salir
    """)

def validar_numero(mensaje, tipo):
    while True:
        entrada = input(mensaje)
        try:
            valor = tipo(entrada)
            return valor
        except ValueError:
            print("ingrese un valor valido ")

def calcular_todas_las_operaciones(a, b):
    a_entero = int(a)
    b_entero = int(b)
    return [
        funcionesBiblioteca.suma(a, b),
        funcionesBiblioteca.resta(a, b),
        funcionesBiblioteca.division(a, b),
        funcionesBiblioteca.multiplicacion(a, b),
        funcionesBiblioteca.factorial(a_entero),
        funcionesBiblioteca.factorial(b_entero),
    ]

def informar_resultados(resultados):
    print("Resultados:")
    print(f"a) El resultado de a+b es: {resultados[0]}")
    print(f"b) El resultado de a-b es: {resultados[1]}")
    print(f"c) El resultado de a/b es: {resultados[2]}")
    print(f"d) El resultado de a*b es: {resultados[3]}")
    print(f"e) El factorial de a es: {resultados[4]} y el factorial de b es: {resultados[5]}")

def iniciar():
    a = None
    b = None

    while True:
        mostrar_menu(a, b)

        opcion = validar_numero(" seleccione una opcion: ", int)

        if opcion == 1:
            a = validar_numero(" ingrese el primer operando : ", float)
        elif opcion == 2:
            b = validar_numero("ingrese el segundo operando  : ", float )
        elif opcion == 3:
            if a == None or b == None:
                print("tiene que ingresar ambos numeros")
            else:
                resultados = calcular_todas_las_operaciones(a, b)
                print("operaciones hechas")
        elif opcion == 4 :
            if a == None or b == None:
                print("tiene que ingresar ambos numeros primero ")
            else:
                informar_resultados(resultados)
        elif opcion == 5:
            print("terminado")
            break
        else:
            print("erro tiene que ingresar un numero del 1 al 5")

if __name__ == "__main__":
    iniciar()
