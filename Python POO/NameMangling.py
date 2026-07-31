"""para recordar un poco anteriormente aprendi lo que es _ lo cual es una convención para indicar que el atributo está destinado para uso interno de la clase y no deberia ser accedido directamente desde fuera de esta y por otro lado el doble __ activa en name mangling que es una tecnica que cambia el nombre del atributo o metodo para hacerle mas dificil de acceder desde fuera lo cual añade una capa de protección adicinal"""

"""el objetivo principal de estas convenciones es proteger el estado interno del objeto y mantener la integridad de los datos, evitando conflictos de nombres en clases derivadas y promoviendo un diseño más limpio y mantenible"""

class ejemplo:
    def __init__(self,valor):
        self._valor = valor # atributo privado por convención

class ejemplo2:
    def __init__(self,valor):
        self.__valor = valor # atributo privado con name mangling

"""esto no significa que no se pueda acceder a estos atributos desde fuera de la clase, pero si es una buena práctica respetar estas convenciones para mantener la integridad del objeto y evitar conflictos de nombres en clases derivadas"""

"""como acceder igualmente"""

objeto = ejemplo(10)
print(objeto._valor)  # Acceso permitido, pero no recomendado

objeto2 = ejemplo2(20)
print(objeto2._ejemplo2__valor)  # Acceso permitido, pero no recomendado

"""como verás al integrar name mangling este cambia como se hace referencia realmente al atributo y pasa a ser _NombreDeLaClase__NombreDelAtributo, lo cual hace que sea más difícil de acceder desde fuera de la clase y ayuda a evitar conflictos de nombres en clases derivadas"""

"""si intentas llamar al atributo con __valor directamente desde fuera de la clase, obtendrás un error de atributo, ya que el nombre ha sido modificado internamente por el name mangling"""

"""ejemplo"""

#print(objeto2.__valor)  # Esto generará un error de atributo

"""y si intentas asignar un valor a __valor desde fuera de la clase, en realidad estarás creando un nuevo atributo en el objeto, y no modificando el atributo original que está protegido por name mangling"""

objeto2.__valor = 30  # Esto no modifica el atributo original, sino que crea un nuevo atributo en el objeto

print(objeto2.__valor)  # Esto imprimirá 30, pero no es el atributo original protegido por name mangling

print(objeto2._ejemplo2__valor)  # Esto imprimirá 20, que es el valor original del atributo protegido por name mangling