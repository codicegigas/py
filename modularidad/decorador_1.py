#Los decoradores son una forma de envolver funciones para añadir funcionalidades sin modificar su código original.
#Se usan mucho en frameworks web y VALIDAR DATOS


def mi_decorador(funcion):
    def nueva_funcion():
        print("Antes de la función")
        funcion()
        print("Despues de la función")
    return nueva_funcion

@mi_decorador
def saludar():
    print("Hola!")

saludar()

