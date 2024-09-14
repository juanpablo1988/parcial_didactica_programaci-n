# Clase Continente
class Continente:
    def __init__(self, codigo_continente, nombre_continente):
        self.codigo_continente = codigo_continente
        self.nombre_continente = nombre_continente

# Clase País, que hereda de Continente
class Pais(Continente):
    def __init__(self, codigo_continente, nombre_continente, codigo_pais, nombre_pais):
        super().__init__(codigo_continente, nombre_continente)
        self.codigo_pais = codigo_pais
        self.nombre_pais = nombre_pais

# Clase Empresa, que hereda de País
class Empresa(Pais):
    def __init__(self, codigo_continente, nombre_continente, codigo_pais, nombre_pais, codigo_empresa, nombre_empresa, telefono_empresa):
        super().__init__(codigo_continente, nombre_continente, codigo_pais, nombre_pais)
        self.codigo_empresa = codigo_empresa
        self.nombre_empresa = nombre_empresa
        self.telefono_empresa = telefono_empresa

# Clase Estado, que hereda de País
class Estado(Pais):
    def __init__(self, codigo_continente, nombre_continente, codigo_pais, nombre_pais, codigo_estado, nombre_estado, descripcion):
        super().__init__(codigo_continente, nombre_continente, codigo_pais, nombre_pais)
        self.codigo_estado = codigo_estado
        self.nombre_estado = nombre_estado
        self.descripcion = descripcion

# Clase Ciudad, que hereda de Estado
class Ciudad(Estado):
    def __init__(self, codigo_continente, nombre_continente, codigo_pais, nombre_pais, codigo_estado, nombre_estado, descripcion, codigo_ciudad, nombre_ciudad):
        super().__init__(codigo_continente, nombre_continente, codigo_pais, nombre_pais, codigo_estado, nombre_estado, descripcion)
        self.codigo_ciudad = codigo_ciudad
        self.nombre_ciudad = nombre_ciudad

# Clase Representante
class Representante(Empresa):
    def __init__(self, codigo_continente, nombre_continente, codigo_pais, nombre_pais, codigo_empresa, nombre_empresa, telefono_empresa, codigo_representante, nombre_representante):
        super().__init__(codigo_continente, nombre_continente, codigo_pais, nombre_pais, codigo_empresa, nombre_empresa, telefono_empresa)
        self.codigo_representante = codigo_representante
        self.nombre_representante = nombre_representante

    def mostrar_datos(self):
        print(f"Continente: {self.nombre_continente}, País: {self.nombre_pais}")
        print(f"Empresa: {self.nombre_empresa}, Teléfono: {self.telefono_empresa}")
        print(f"Representante: {self.nombre_representante}, Código: {self.codigo_representante}")

# Función para crear y mostrar representantes
def crear_representante():
    representantes = []
    
    for _ in range(2):  # ingreso de dos registros
        codigo_continente = input("Código del continente: \n")
        nombre_continente = input("Nombre del continente: \n")
        codigo_pais = input("Código del país: \n")
        nombre_pais = input("Nombre del país: \n")
        codigo_empresa = input("Código de la empresa: \n")
        nombre_empresa = input("Nombre de la empresa: \n")
        telefono_empresa = input("Teléfono de la empresa:\n ")
        codigo_representante = input("Código del representante: \n")
        nombre_representante = input("Nombre del representante: \n")

        representante = Representante(codigo_continente , nombre_continente, codigo_pais, nombre_pais, 
                                      codigo_empresa, nombre_empresa, telefono_empresa, 
                                      codigo_representante, nombre_representante)
        representantes.append(representante)
    
    # Mostrar los datos de los representantes
    for representante in representantes:
        representante.mostrar_datos()

# Ejecutar la función
crear_representante()
