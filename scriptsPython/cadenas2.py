#Importo las librerias necesarias, random para poder generar una cadena
#aleatoria, string para obtener los caracteres para la cadena,
#y los necesarios para la fecha y hora.
import random
import string
from datetime import datetime
from datetime import date

#VARIABLES: 
# Nueva variante de covid tiene la siguiente secuencia "ccucggcgggca"
# Cadena es una cadena aleatoria que creamos con random.choices.
# Elige 50 caracteres (k=17) aleatorios de la variable letras,
# puestas de 3 en 3 para facilitar que el resultado sea positivo.
covid="ccucggcgggca"
letras=(['ccu','cgg','gca'])
cadena= "".join(random.choices(letras,k=17))
fecha = datetime.now().strftime('%d-%m-%Y')
hora = datetime.now().strftime('%H:%M')

#Preguntamos cual es el codigo numerico del paciente
codigo= input("Introduce codigo de paciente: ")

#Se imprime en pantalla el siguiente informe con los datos:
print("----Informe de virus COVID----")
print("Fecha:",fecha)
print("Hora:",hora)
print("Codigo Paciente:",codigo)
print("----Resultado----")
if covid in cadena:
    print("Positivo: Si se encuentra restos de la variante COVID")
    resultado="Positivo"
else:
    print("Negativo: No se encuentran restos de la variante COVID")
    resultado="Negativo"

#Guardamos los resultados obtenidos en una tupla
tupla=(fecha,hora,codigo,resultado)
print(tupla)