# Proyecto de Gestión de Datos Orientado a Objetos

## Descripción

Este proyecto está diseñado para modelar y gestionar la información relacionada con continentes, países, empresas y representantes utilizando un enfoque orientado a objetos en Python. La solución aborda la necesidad de organizar y visualizar datos en una estructura jerárquica y modular.

## Problemas que Resuelve

1. **Organización Estructural de Datos:**
   - **Problema:** La gestión de datos sobre continentes, países, empresas y representantes puede volverse desorganizada y difícil de manejar si no se estructura adecuadamente.
   - **Solución:** Utiliza clases y herencia para crear una jerarquía clara y modular, donde cada clase representa una entidad específica y se encarga de sus propios datos y comportamientos.

2. **Reutilización de Código:**
   - **Problema:** Sin un enfoque modular, el código puede contener redundancias, lo que hace más difícil el mantenimiento y la ampliación del sistema.
   - **Solución:** Implementa la herencia en las clases para reutilizar atributos y métodos comunes. Las clases específicas heredan de clases más generales, reduciendo la duplicación de código.

3. **Visualización de Datos:**
   - **Problema:** La presentación de datos de manera clara y concisa es fundamental para la comprensión y análisis.
   - **Solución:** Incluye un método `mostrar_datos()` en la clase `Representante` para presentar la información de forma organizada y legible, mostrando los datos del representante junto con la información de la empresa, país y continente.

4. **Entrada de Datos Dinámica:**
   - **Problema:** Ingresar datos manualmente en el código puede ser tedioso y propenso a errores.
   - **Solución:** Proporciona una función `crear_representante()` que permite al usuario ingresar los datos de manera interactiva, creando instancias de la clase `Representante` y almacenándolas en una lista para su posterior visualización.

## Clases Principales

### Continente
- Representa un continente con atributos para código y nombre.
  
### País
- Hereda de `Continente` y añade atributos específicos para el país.

### Empresa
- Hereda de `País` y añade atributos específicos para la empresa.

### Representante
- Hereda de `Empresa` y añade atributos específicos para el representante.

## Función `crear_representante()`

Esta función permite al usuario ingresar datos para crear instancias de la clase `Representante`. Los datos se almacenan en una lista y se muestran utilizando el método `mostrar_datos()`.

## Ejecución del Programa

Para ejecutar el programa y crear representantes, llama a la función `crear_representante()`:

```python
crear_representante()