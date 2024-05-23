def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def division (a,b):

    if b == 0:
        return "Error no se puede dividir por cero"
    return a / b

def multiplicacion (a,b):

    return a * b

def factorial(numero):

    if numero < 0:
        return "No se puede devolver un factorial dde un numero negativo"
    elif numero == 0:
        return 1
    else:
        resultado = 1

        for i in range(1 , numero + 1):
            resultado *= 1
        return resultado
