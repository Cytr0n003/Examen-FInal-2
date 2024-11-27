
import pandas as pd
from inmobilaria.clases import Propietario

def cargar_propietarios():
    # Cargar desde el Excel
    dfPropietarios = pd.read_excel('Inmobiliaria.xlsx', sheet_name='Propietarios', index_col=0)
    print(f"Se cargaron {len(dfPropietarios.index)} fila(s)")
    return dfPropietarios

def guardar_propietarios(dfPropietarios):
    # Guardar en excel multihoja
    writer = pd.ExcelWriter('Inmobiliaria.xlsx', mode='a', if_sheet_exists='replace')
    dfPropietarios.to_excel(writer, sheet_name='Propietarios')
    writer.close()

def agregar_propietarios():
    # Cargar datos de propietarios
    dfPropietarios = cargar_propietarios()

    # Validar si el dataFrame ya fue cargadado desde el excel
    if dfPropietarios is None:
        print("No existen propietarios registrados. Por favor, cargue los datos.")
        return
    
    # Recibiendo los datos del propietario a registrar
    idProp = input("Ingrese el ID del nuevo propietario: ")
    nbProp = input("Ingrese el NOMBRE del nuevo propietario: ")

    # Validadno que el ID no se encuentre registrado
    if idProp in dfPropietarios.index:
        print("El ID ya se encuentra registrado.")
        return

    # Construir el objeto Propietario
    objProp = Propietario(idProp, nbProp)

    # Agregar el nuevo propietario al DataFrame
    dfPropietarios.loc[objProp.idPropietario] = {'Nombre':objProp.nombre}

    # Guardar datos en archivo
    guardar_propietarios(dfPropietarios)

    # Mostrar los últimos registros del dataFrame
    print(dfPropietarios.tail(10))

def actualizar_propietarios():
    # Cargar datos de propietarios
    dfPropietarios = cargar_propietarios()
    
    # Recibiendo los datos del propietario a registrar
    idProp = input("Ingrese el ID del propietario a actualizar: ")

    # Validadno que el ID no se encuentre registrado
    if not idProp in dfPropietarios.index:
        print("No existe Propietario con el ID indicado.")
        return
    
    print(f"Datos del propietario: \n{dfPropietarios.loc[idProp]}")
    nbProp = input("Ingrese el NOMBRE del propietario a actualizar: ")

    # Construir el objeto Propietario
    objProp = Propietario(idProp, nbProp)

    # Actualizar el nuevo propietario al DataFrame
    dfPropietarios.loc[objProp.idPropietario] = {'Nombre':objProp.nombre}

    # Guardar en excel multihoja
    guardar_propietarios(dfPropietarios)

    print(f"Datos del propietario: \n{dfPropietarios.loc[idProp]}")

def eliminar_propietarios():
    # Cargar datos de propietarios
    dfPropietarios = cargar_propietarios()
    
    # Recibiendo los datos del propietario a registrar
    idProp = input("Ingrese el ID del propietario a eliminar: ")

    # Validadno que el ID no se encuentre registrado
    if not idProp in dfPropietarios.index:
        print("No existe Propietario con el ID indicado.")
        return
    
    print(f"Datos del propietario: \n{dfPropietarios.loc[idProp]}")

    # Actualizar el nuevo propietario al DataFrame
    rpta = input(f"Confirma la eliminación del propietario con ID = '{idProp}' [S/N]: ").upper()
    if rpta == 'S':
        dfPropietarios.drop(idProp, inplace=True)

    # Guardar en excel multihoja
    guardar_propietarios(dfPropietarios)

    print("Propietario eliminado.")

def listar_propietarios():
    # Cargar datos de propietarios
    dfPropietarios = cargar_propietarios()
    
    # Listar los datos del datFrame de propietarios
    print(dfPropietarios)

def menu_propietarios():
    while(True):
        print("")
        print("1.- Agregar Propietarios")
        print("2.- Actualizar Propietarios")
        print("3.- Eliminar Propietarios")
        print("4.- Listar Propietarios")
        print("5.- Volver al menú principal")

        seleccion = int(input("Seleccione una opción: "))

        if 1 <= seleccion <= 4:
            match(seleccion):
                case 1:
                    agregar_propietarios()
                case 2:
                    actualizar_propietarios()
                case 3:
                    eliminar_propietarios()
                case 4:
                    listar_propietarios() 
        elif seleccion == 5:
            return
        else:
            continue


def menu_principal():
    while(True):
        print("")
        print("1.- Gestionar Propietarios")
        print("2.- Gestionar Vendedores")
        print("3.- Gestionar Tipos de Inmueble")
        print("4.- Gestionar Inmuebles")
        print("5.- Reportes")
        print("6.- Salir")

        seleccion = int(input("Seleccione una opción: "))

        if 1 <= seleccion <= 5:
            match(seleccion):
                case 1:
                    menu_propietarios()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass 
        elif seleccion == 6:
            return
        else:
            continue


if __name__ == "__main__":
    menu_principal()
