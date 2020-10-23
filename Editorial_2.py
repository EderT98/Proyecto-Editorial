__author__ = 'Eder Tassin'

import os
import pickle
from Articulo import *


def mostrarArchivo(FD):
    if not os.path.exists(FD):
        print('Archivo inexistente ...')
        return
    t = os.path.getsize(FD)
    if t == 0:
        print('Archivo sin datos ...')
    else:
        m = open(FD, 'rb')
        while m.tell() < t:
            reg = pickle.load(m)
            to_string(reg)
        m.close()


def main():
    FD = 'articulos.dat'
    op = 0
    while op != 2:
        print('\nEditorial - Programa 2')
        print(' 1. Mostrar el contenido del archivo articulos.dat')
        print(' 2. Salir')
        op = int(input('\033[33m \t\tIngrese número de la opción elegida: \033[0m'))
        print()

        if op == 1:
            mostrarArchivo(FD)

        elif op == 2:
            print('FIN DEL PROGRAMA')


if __name__ == '__main__':
    main()