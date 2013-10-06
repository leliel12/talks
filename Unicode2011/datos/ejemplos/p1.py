import yaml


class Direccion(object):
    
    def __init__(self, tipo, desc):
        self.tipo = tipo
        self.desc = desc
                

class Persona(object):
    
    def __init__(self, name, direcciones):
        self.name = name
        self.direcciones = direcciones

dir1 = Direccion("personal", "fake 123")
dir2 = Direccion("laboral", "real 456")

persona = Persona("Tito Puente", [dir1, dir2])

src = yaml.dump(persona, default_flow_style=True)

print src
