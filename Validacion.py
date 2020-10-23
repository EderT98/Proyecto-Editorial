__author__ = 'Eder Tassin'


def validarMayorQue(limite, mensaje):
    valor = int(input(mensaje))
    while valor <= limite:
        print('ERROR...')
        valor = int(input(mensaje))
    return valor


def validarIntervalo(inferior, superior, mensaje):
    valor = int(input(mensaje))
    while valor < inferior or valor > superior:
        print('ERROR...')
        valor = int(input(mensaje))
    return valor