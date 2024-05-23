def suma(a,b):
    """suma de dos numeros

    Args:
        a (float): primero numero
        b (float): segundo numero

    Returns:
        float: suma a + b
    """
    return a + b

def resta(a,b):
    """resta de dos numeros

    Args:
        a (float): primer numero
        b (float): segundo numero

    Returns:
        _float: resta a - b
    """
    return a - b

def division (a,b):
    """division de dos numeros

    Args:
        a (float): primer numero
        b (float): segundo numero

    Returns:
        float: division de a / b y muestra un error si se ingresa un cero
    """

    if b == 0:
        return "Error no se puede dividir por cero"
    return a / b

def multiplicacion (a,b):
    """multiplicacion de dos numeros

    Args:
        a (float): primer numero
        b (float): segundo numero

    Returns:
        float: multiplicacion de a * b
    """

    return a * b

def factorial(numero):
    """factorial de un solo numero

    Args:
        numero (int): numero para calcular factorial

    Returns:
        int: factorial de numero sino devuelve mensaje de error si es negativo
    """

    if numero < 0:
        return "No se puede devolver un factorial dde un numero negativo"
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1 , numero + 1):
            resultado *= 1
        return resultado
