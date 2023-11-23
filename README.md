Documentación Técnica
Tecnologías Utilizadas
Lenguaje de Programación: Python 3.x
Base de Datos: SQLite 3
Biblioteca para conexión con SQLite: sqlite3 (incluida en el estándar de Python)
Arquitectura
La aplicación consta de un script principal (main.py) que referencia funciones definidas en el mismo script.
Las funciones separadas permiten mantener un código organizado para cada operación de CRUD.
El script se conecta a una base de datos SQLite existente llamada "northwind.db". Se requiere que dicha base esté disponible en el mismo directorio del script.
Las consultas y operaciones con la BD se realizan a través de la biblioteca sqlite3 que viene integrada en Python.
Funciones Principales
menu(): Muestra las opciones disponibles en la aplicación
listar_categorias(): Consulta y listado de registros
agregar_categoria(): Insertar nuevos registros
modificar_categoria(): Actualización de registros existentes
eliminar_categoria(): Eliminación o borrado de registros
Documentación Funcional
Descripción General
La aplicación permite gestionar las categorías de productos contenidos en la base de datos de ejemplo Northwind.

Las operaciones disponibles en el menú principal son:

Listar categorías: consulta y muestra todos los registros de la tabla Categories
Agregar categoría: inserta un nuevo registro solicitando los datos al usuario
Modificar categoría: actualiza los campos CategoryName y Description de un registro existente
Eliminar categoría: elimina un registro por su Id
Salir: termina la ejecución de la aplicación
Adicionalmente maneja excepciones y mensajes para los errores y operaciones.

Forma de uso
Ejecutar el script main.py
Seguir las opciones e indicaciones que muestra el menú
Para las operaciones CRUD se solicitan y/o muestran los datos según corresponda
Posibles mejoras
Validación más robusta en campos de entrada
Opciones adicionales para consultas y filtros
Interfaz gráfica de usuario
Operaciones sobre otras tablas de la base de datos
