import pandas as pd
import matplotlib.pyplot as plt

def leer_data(hoja = 'Notas'):
    dfNotas = pd.read_excel('NotasAlumnos.xlsx', sheet_name=hoja, index_col=0)
    print(f"{len(dfNotas.index)} fila(s) recuperada(s)")
    return dfNotas

def guardar_data(dfNotas: pd.DataFrame):
    dfNotas.to_excel('NotasAlumnos.xlsx', sheet_name='Notas', index=True)
    print(f"{len(dfNotas.index)} fila(s) recuperada(s)")

def menu():
    while(True):
        print()
        print("1.- Registrar notas de alumno")
        print("2.- Listar Calificaciones")
        print("3.- Mostrar Estadísticas")
        print("4.- Salir")

        seleccion = int(input("Seleccione una opción: "))

        match(seleccion):
            case 1:
                registrar_notas()   
            case 2:
                listar_notas()
            case 3:
                menu_estadisticas()
            case 4:
                return
            case _:
                continue

def menu_estadisticas():
    while(True):
        print()
        print("1.- Barras")
        print("2.- Barras apiladas")
        print("3.- Líneas")
        print("4.- Histograma")
        print("5.- Dispersion")
        print("6.- Líneas con filtro")
        print("7.- Dispersion comparativa")
        print("8.- Lineas agrupadas")
        print("9.- Regresar al menu principal")

        seleccion = int(input("Seleccione una opción: "))

        match(seleccion):
            case 1:
                barras()
            case 2:
                barras_apiladas()
            case 3:
                lineas()
            case 4:
                histograma()
            case 5:
                dispersion()
            case 6:
                lineas_filtro()
            case 7:
                dispersion_comparativa()
            case 8:
                lineas_agrupadas()
            case 9:
                return
            case _:
                continue

def registrar_notas():
    dfNotas = leer_data()
    codigo = input("Código: ")

    # Validando que el ID no se encuentre registrado
    if codigo in dfNotas.index:
        print("El ID ya se encuentra registrado.")
        return

    nombre = input("Nombre: ")
    parcial = int(input("Parcial: "))
    final = int(input("Final: "))
    nota_final = (parcial+final)/2
    condicion = 'Aprobado' if nota_final > 12.5 else 'Desaprobado'
    dfNotas.loc[codigo] = {'Nombre':nombre, 
                           'Parcial':parcial, 
                           'Final':final, 
                           'NotaFinal':nota_final, 
                           'Condicion':condicion}
    
    print(dfNotas.loc[codigo])

    guardar_data(dfNotas)

def listar_notas():
    dfNotas = leer_data()
    print(dfNotas)

# 1. Gráficos de barras 
def barras():
    dfNotas = leer_data()

    # Crear el gráfico
    plt.bar(dfNotas.index, dfNotas['NotaFinal'])

    # Personalizar el gráfico
    plt.xlabel('ALumnos')
    plt.ylabel('Nota Final')
    plt.title('Nota Final x Alumno')

    # Mostrar el gráfico
    plt.show()
    
# 2. Gráficos de barras apiladas 
def barras_apiladas():
    dfNotas = leer_data()

    plt.figure(figsize=(10, 6)) 
    plt.bar(dfNotas['Nombre'], dfNotas['Parcial'], label='Parcial') 
    plt.bar(dfNotas['Nombre'], dfNotas['Final'], bottom=dfNotas['Parcial'], label='Final') 
    plt.title('Notas Parciales y Finales Apiladas') 
    plt.xlabel('Nombre') 
    plt.ylabel('Notas') 
    plt.xticks(rotation=45) 
    plt.legend()
    plt.show()

# 3. Líneas
def lineas():
    dfNotas = leer_data()

    plt.figure(figsize=(10, 6))
    plt.plot(dfNotas['Nombre'], dfNotas['Parcial'], marker='o', label='Parcial')
    plt.plot(dfNotas['Nombre'], dfNotas['Final'], marker='o', label='Final')
    plt.title('Notas Parciales y Finales de los Estudiantes')
    plt.xlabel('Nombre')
    plt.ylabel('Notas')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()


# 4. Histograma
def histograma():
    dfNotas = leer_data()

    plt.figure(figsize=(10, 6))
    plt.hist(dfNotas['NotaFinal'], bins=5, alpha=0.7)
    plt.title('Distribución de Notas Finales')
    plt.xlabel('Nota Final')
    plt.ylabel('Frecuencia')
    plt.show()

# 5. Gráfico de Dispersión (Scatter Plot)
def dispersion():
    dfNotas = leer_data()

    plt.figure(figsize=(10, 6))
    #plt.scatter(dfNotas['Parcial'], dfNotas['Final'])
    plt.scatter(dfNotas['Parcial'], dfNotas['Final'], c=dfNotas['NotaFinal'], cmap='viridis', s=100)
    plt.title('Notas Parciales vs Notas Finales')
    plt.xlabel('Parcial')
    plt.ylabel('Final')
    plt.colorbar(label='Nota Final')
    plt.show()

# 6. Gráfico de líneas de notas finales por curso alumno 
def lineas_filtro():
    dfNotas = leer_data('NotasCursos')

    dfCurso1 = dfNotas[dfNotas['Curso']=='CC200']
    dfCurso2 = dfNotas[dfNotas['Curso']=='CC201']

    # Crear el gráfico
    plt.plot(dfCurso1.index, dfCurso1['NotaFinal'], marker='o', label='CC200')
    plt.plot(dfCurso2.index, dfCurso2['NotaFinal'], marker='*', label='CC201')

    # Personalizar el gráfico
    plt.xlabel('Códigos')
    plt.ylabel('Nota Final')
    plt.title('Nota Final x Curso y Alumno')
    plt.xticks(rotation=45)
    plt.legend()

    # Mostrar el gráfico
    plt.show()

# 7. Gráfico de dispersión de notas parciales vs finales por curso 
def dispersion_comparativa():
    dfNotas = leer_data('NotasCursos')

    plt.figure(figsize=(10, 6)) 
    for curso in dfNotas['Curso'].unique(): 
        subset = dfNotas[dfNotas['Curso'] == curso] 
        plt.scatter(subset['Parcial'], subset['Final'], label=curso) 
    
    plt.title('Notas Parciales vs Notas Finales por Curso') 
    plt.xlabel('Nota Parcial') 
    plt.ylabel('Nota Final') 
    plt.legend(title='Curso')
    plt.show()

# 8. Promedio de notas parciales y finales por condición de aprobación 
def lineas_agrupadas():
    dfNotas = leer_data('NotasCursos')

    dfPromCondicion = dfNotas.groupby('Condicion')[['Parcial', 'Final']].mean() 
    plt.figure(figsize=(10, 6)) 
    dfPromCondicion.plot(kind='bar') 
    plt.title('Promedio de Notas Parciales y Finales por Condición de Aprobación') 
    plt.xlabel('Condición') 
    plt.ylabel('Nota Promedio') 
    plt.legend(title='Tipo de Nota') 
    plt.show()


if __name__ == "__main__":
    menu()