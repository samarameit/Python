# Importamos para poder obtener la fecha y hora:
from datetime import datetime
from datetime import date
import sys

# variables de fecha y hora:
fecha = datetime.now().strftime('%d-%m-%Y')
hora = datetime.now().strftime('%H:%M')

# Preguntar temperaturas y listarlas. Primero indicamos que se va a crear una lista llama temperaturas.
# Como no sabemos la cantidad que nos van a indicar, uso un while True y solo terminará de preguntar 
# cuando se pulse el numero 100. Esto se indica con el if, si pulsan el 100 se sale del bucle while.
# Si se introduce cualquier otro numero entero, este se añadira a la lista temperaturas.
temperaturas= []
while True:
    temp= int(input("Dime una temperatura tomada: "))
    if temp != 100:
        temperaturas.append(temp)
    if temp == 100:
        break;

# Informe principal. Uso funciones integradas de Python para obtener los datos requeridos.
print("Informe de temperaturas del Parque Natural Doñana:")
print("Fecha:",fecha )
print("Hora:",hora)
print("Numero de muestras: %d" % len(temperaturas))
print("Temperaturas tomadas:",temperaturas)
print("Temperatura máxima:", max(temperaturas))
print("Temperatura minima:",min(temperaturas))
print("Temperatura media:", round(sum(temperaturas)/len(temperaturas),2))
# Creacion tupla
tupla=(fecha,hora,temperaturas)
print(str(tupla))
# Convierte la tupla en una lista para poder meterlo en un fichero .txt
lista = list(tupla)
# Abrimos el archivo donde queremos guardar la tupla. Con write le indicamos
# lo que tiene que escribir. Despues cerramos el archivo.
with open("temperaturas.txt", "w") as f:
    f.write('temperaturas = %s' % lista + '\n1')
    f.close()