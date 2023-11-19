
# Por ahora, como prototipo, sólo se trabajará con la tabla Categories  
# El código se podría extender en el futuro para incluir más tablas

import sqlite3

def menu():
    print("1. Listar categorías (mostrar todas las categorías)")
    print("2. Agregar categoría (ingresar una nueva categoría)")  
    print("3. Modificar categoría (editar una categoría existente)")
    print("4. Eliminar categoría (borrar una categoría)")
    print("5. Salir (cerrar el programa)")

def listar_categorias():
    conn = sqlite3.connect('northwind.db')
    c = conn.cursor()
    try:
        c.execute("SELECT CategoryID, CategoryName, Description FROM Categories") 
        categorias = c.fetchall()
        print("Listado de Categorías:")
        for categoria in categorias:
            print(categoria[0], categoria[1], categoria[2])
    except sqlite3.Error as e:
        print("Error al listar las categorías:", e)
    finally:
        conn.close()

def agregar_categoria():
    conn = sqlite3.connect('northwind.db')
    c = conn.cursor()
    try:
        nombre = input("Ingrese el nombre de la nueva categoría: ")
        descripcion = input("Ingrese una descripción: ")
        c.execute("INSERT INTO Categories (CategoryName, Description) VALUES (?, ?)", (nombre, descripcion))
        conn.commit()
        print("Categoría agregada exitosamente!")
    except sqlite3.Error as e:
        print("Error al agregar la categoría:", e)
    finally:
        conn.close()

def modificar_categoria():
    conn = sqlite3.connect('northwind.db')
    c = conn.cursor()
    try:
        id = int(input("Ingrese el ID de la categoría a modificar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nueva_descripcion = input("Ingrese la nueva descripción: ")
        c.execute("UPDATE Categories SET CategoryName = ?, Description = ? WHERE CategoryID = ?", (nuevo_nombre, nueva_descripcion, id))
        conn.commit()
        print("Categoría modificada exitosamente!")
    except sqlite3.Error as e:
        print("Error al modificar la categoría:", e)
    finally:
        conn.close()  

def eliminar_categoria():
    conn = sqlite3.connect('northwind.db')
    c = conn.cursor()
    try:
        id = int(input("Ingrese el ID de la categoría a eliminar: "))
        c.execute("DELETE FROM Categories WHERE CategoryID = ?", (id,))
        conn.commit()
        print("Categoría eliminada exitosamente!")
    except sqlite3.Error as e:
        print("Error al eliminar la categoría:", e)
    finally:
        conn.close()

opcion = 0
while opcion != 5:
    menu()
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            listar_categorias()
        elif opcion == 2:
            agregar_categoria()
        elif opcion == 3:
            modificar_categoria()
        elif opcion == 4:
            eliminar_categoria()
        elif opcion == 5:
            print("Saliendo...") 
        else:
            print("Opción inválida")
    except ValueError:
        print("Por favor, ingrese un número válido.")
