#Importamos la librería
from datetime import datetime, date, timedelta, time

#Abrimos el archivo subido en lectura
fechas1 = open('Fechas1.txt','r')
texto1 = fechas1.read()
fechas1.close()

#Abrimos el documento a crear en escritura
Fechita1 = open('fechita1.txt', 'w')
Fechita1.write(texto1)

#Creamos una lsta con el contenido de nuestro archivo
fechas1 = open('Fechas1.txt','r')
lista1 = fechas1.readlines()
fechas1.close()
print(lista1)

#Identificamos los elementos del documento
fecha1 = (lista1[0].rstrip())
fecha2 = (lista1[1].rstrip())

#Definimos date1
date1 = datetime.strptime(fecha1,'%d/%m/%Y %H:%M:%S')
Fechita1.write(str(date1))
print(date1)

#Sumamos horas a date1
sumar19hours = (date1 + timedelta(hours=19))
Fechita1.write(str(sumar19hours))
print(sumar19hours)

#Comparamos dos fechas
comparacion1 = fecha1 > fecha2
Fechita1.write("¿la fecha 2 es mayor que la fecha 3?: ")
Fechita1.write(str(comparacion1))
print(comparacion1)

#Definimos una tercera fecha
date3 = datetime.strptime(fecha1,'%d/%m/%Y %H:%M:%S')
Fechita1.write(str(date3))
print(date3)

#Restamos dos fechas
resta = date3-date1
Fechita1.write(str(resta))
print(resta)

#Definimos la fecha 4
date4 = datetime.strptime(fecha2,'%d/%m/%Y %H:%M:%S')
Fechita1.write(str(date4))
print(date4)

#Restamos 5 horas a la fecha 4
restar5hours = (date4 - timedelta(hours=5))
Fechita1.write(str(restar5hours))
print(restar5hours)

#Cerramos  archivo
Fechita1.close()

#Abrimos nuestro archivo con las segundas fechas
fechas2 = open('Fechas2.txt','r')
texto2 = fechas2.read()
fechas2.close()

#Abrimos el archivo con segundas fchas a crear
Fechita2 = open('fechita2.txt', 'w')
Fechita2.write(texto2)

#Abrimos de nuevo el archivo en modo lectura y definimos la lista 2
fechas2 = open('Fechas2.txt','r')
lista2 = fechas2.readlines()
fechas2.close() 
print((lista2))

#Identificamos los elementos de nuestra lista
dia1 = (lista2[0].rstrip())
dia2 = (lista2[1].rstrip())
dia1_hour = int(dia1[12:14])
print(dia1_hour)
dia1_min = int(dia1[15:17])
print(dia1_min)
dia1_sec = int(dia1[18:20])
print(dia1_sec)
dia2_hour = int(dia2[12:14])
print(dia2_hour)
dia2_min = int(dia2[15:17])
print(dia2_min)
dia2_sec = int(dia2[18:20])
print(dia2_sec)
Fechita2.write("- time(): ")
fech1 = time(dia1_hour,dia1_min,dia1_sec)
Fechita2.write(str(fech1))
print(fech1)

#Realizamos la operacion con otro tipo de formato
formato2 = ( "{:%H y %M del día}".format(fech1))
Fechita2.write(str(formato2))
Fechita2.write("- time(), .hour(), .minute(), .second(): ")
fech2 = time(dia2_hour,dia2_min,dia2_sec)
Fechita2.write(str(fech2))
Fechita2.write(str(fech2.hour))
Fechita2.write(str(fech2.minute))
Fechita2.write(str(fech2.second))
print(fech2)

#Comparamos dos fechas
comparacion = fech1 > fech2
Fechita2.write("¿la hora 1 es mayor que la hora 2?: ")
Fechita2.write(str(comparacion))
print(comparacion)
fech3 = time(dia1_hour,dia1_min,dia1_sec)
fech4 = time(dia2_hour,dia2_min,dia2_sec)
comparacionn = fech3 < fech4
Fechita2.write("¿la hora 1 es menor que la hora 2?: ")
Fechita2.write(str(comparacionn))
print(comparacionn)

#Cerramos el doumento
Fechita2.close()