__author__ = 'Eder Tassin'

import pickle
import os
import random
from Articulo import *
from Validacion import *


def cargarVectorOrdenado_Automatico(n):
    v = []
    for i in range(n):
        codigo = random.randint( 1, 9999)
        valor = random.randint(1, 100)
        titulo = 'Titulo' + str(valor)
        paginas = random.randint( 5, 1000)
        tipo = random.randint( 0, 9)
        idioma = random.randint( 0, 5)
        reg = Articulo(codigo, titulo, paginas, tipo, idioma)
        # Sin titulo repetido
        ban = add_in_order( v, reg)
        if ban == False:
            continue
    return v


def add_in_order( v, reg):
    n = len(v)
    izq, der = 0, n-1
    pos = n
    while izq <= der:

        c = (izq + der) // 2
        if v[c].titulo == reg.titulo:
           return False

        elif reg.titulo < v[c].titulo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
        v[pos:pos] = [reg]  # CUIDADO !!!
        return True


def add_in_order_ConRepetidos( v, reg):
    n = len(v)
    izq, der = 0, n-1
    # ban = True
    pos = n
    while izq <= der:
        c = (izq + der) // 2
        if v[c].titulo == reg.titulo:
           pos = c
           break
        elif reg.titulo < v[c].titulo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def mostrarVector(vec):
    n = len(vec)
    for i in range(n):
        to_string(vec[i])


def buscarPorTitulo(vec, tit):
    n = len(vec)
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].titulo == tit:
           return vec[c]
        elif tit < vec[c].titulo:
            der = c - 1
        else:
            izq = c + 1

    return None


def buscarPorCodigo(vec, cod):

    for i in range(len(vec)):
        if vec[i].codigo == cod:
            return vec[i]
    return None


def generarMatrizConteo(vec):
    mat = [[0] * 6 for filas in range(10)]
    for i in range(len(vec)):
        fil = vec[i].tipo
        col = vec[i].idioma
        mat[fil][col] += 1
    return mat


def mostrarMatrizConteo(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                print('Tipo ', i, ' Idioma ', j, ' : ', mat[i][j], ' articulos')


def generarArchivo(FD, vec, x, y):

    m = open(FD, 'wb')
    for i in range(len(vec)):
        if vec[i].paginas > x and vec[i].paginas < y:
            pickle.dump(vec[i], m)
    m.close()


def mostrarArchivo(FD):

    if not os.path.exists(FD):
        print(' Archivo inexistente ... ')
        return
    t = os.path.getsize(FD)
    m = open(FD, 'rb')
    while m.tell() < t:
        reg = pickle.load(m)
        to_string(reg)
    m.close()


def generarMatrizDesdeArchivo(FD):

    if not os.path.exists(FD):
        print(' Archivo inexistente ... ')
        return

    mat = [ [0] * 6 for filas in range(10) ]
    t = os.path.getsize(FD)

    m = open(FD, 'rb')

    while m.tell() < t:
        reg = pickle.load(m)
        fil = reg.tipo
        col =  reg.idioma
        mat[fil][col] += reg.paginas

    m.close()
    return mat


def mostrarMatrizAcumulacion(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                print('Tipo ', i, ' Idioma ', j, ' : ', mat[i][j], ' paginas')


def calcularPromedio(vec):
    acum = 0
    for i in range(len(vec)):
        acum += vec[i].paginas
    return acum / len(vec)

def puntoExtra(vec, tip):
    ban = False
    promedio = calcularPromedio(vec)

    for i in range(len(vec)):
        if vec[i].tipo == tip and vec[i].paginas > promedio:
            print('Código: ', vec[i].codigo, ' - ', 'Título: ', vec[i].titulo)
            ban = True
    if ban == False:
        print('No hay artículos que cumplan con esas condiciones ...')


def main():
    FD = 'articulos.dat'
    vec= []
    op = 0
    while op != 9:
        print('\nEditorial XXX\n')
        print(' 1. Cargar el vector ordenado por título')
        print(' 2. Mostrar el vector')
        print(' 3. Buscar en el vector por título de artículo')
        print(' 4. Buscar en el vector por código de artículo')
        print(' 5. Cantidad total de páginas por tipo de articulo e idioma')
        print(' 6. Generar el archivo articulos.dat')
        print(' 7. Mostrar archivo articulos.dat')
        print(' 8. Generar matriz de acumulacion desde el archivo')
        print(' 9. SALIR ')
        op = int(input('\033[33m \t\tIngrese número de la opción elegida: \033[0m'))
        print()

        if op == 1:
            n = validarMayorQue(0, 'Ingrese cantidad de articulos: ')
            vec = cargarVectorOrdenado_Automatico(n)

        elif op == 2:
            if len(vec) != 0:
                mostrarVector(vec)
            else:
                print('Aún no se cargaron datos ...')

        elif op == 3:
            if len(vec) != 0:
                tit = input('Ingrese titulo a buscar: ')
                reg = buscarPorTitulo(vec, tit)
                if reg == None:
                    print('Titulo inexistente ... ')
                else:
                    to_string(reg)
            else:
                print('Aún no se cargaron datos ...')

        elif op == 4:
            if len(vec) != 0:
                cod = input('Ingrese codigo a buscar: ')
                reg = buscarPorCodigo(vec, cod)
                if reg == None:
                    print('Código inexistente ... ')
                else:
                    to_string(reg)
            else:
                print('Aún no se cargaron datos ...')

        elif op == 5:
            mat = generarMatrizConteo(vec)
            mostrarMatrizConteo(mat)

        elif op == 6:
            if len(vec) != 0:
                x = int(input('Ingrese cantidad de páginas desde: '))
                y = int(input('Ingrese cantidad de páginas hasta: '))
                if x > y:
                    # los ordeno para que siempre x sea menor o igual a y
                    x, y = y, x
                generarArchivo(FD, vec, x, y)
            else:
                print('Aún no se cargaron datos ...')

        elif op == 7:
            mostrarArchivo(FD)

        elif op == 8:
            mat = generarMatrizDesdeArchivo(FD)
            mostrarMatrizAcumulacion(mat)

        elif op == 9:
            print('FIN DEL PROGRAMA')
        print()


if __name__ == '__main__':
    main()