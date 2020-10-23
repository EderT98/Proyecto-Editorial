__author__ = 'Eder Tassin'


class Articulo:
    def __init__(self, codigo, titulo, paginas, tipo, idioma):
        self.codigo = codigo
        self.titulo = titulo
        self.paginas = paginas
        self.tipo = tipo
        self.idioma = idioma


def to_string(articulo):
    print('Código: ', articulo.codigo, end = ' | ')
    print('Título: ', articulo.titulo, end = ' | ')
    print('Cantidad de páginas: ', articulo.paginas, end = ' | ')
    print('Tipo: ', articulo.tipo, end = ' | ')
    print('Idioma: ', articulo.idioma)