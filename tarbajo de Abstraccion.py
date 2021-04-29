class computadora:
    def __init__(self, teclado, mouse, pantalla, cpu, programas, person):
        self.teclado = teclado
        self.mouse = mou    
        self.pantalla = pantalla
        self.cpu = cpu
        self.programas = programas
        self.persona = persona

    def comandos(self, Epersona):
        return f"Escribir en el {Epersona.person}, luego hacer click con {self.mouse}"
    def Hclick(self, Hmouse):
        return f"Mover el mouse {Hmouse.person}, para acceder a cualquier programna{self.programas}"
tecaldo = computadora("escribir")
mouse = computadora("click")
cpu = computadora("prender, apagar")
pantalla = computadora("imagenes")
programas = computadora("ejecutar")
persona = computadora("aldhair")