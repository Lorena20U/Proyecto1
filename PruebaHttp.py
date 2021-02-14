import os
import numpy as np
ruta_carpetas = '/Users/Pablo Velasquez/Downloads/blynk_server/Data_server/' 
nombres_carpetas = os.listdir(ruta_carpetas)
datos = []
def buscar_archivos(ruta): 
    archivos_texto = [] 
    archivos = os.listdir(ruta) 
    for archivo in archivos:
        if '.user' in archivo:
            archivos_texto.append(archivo) 
    return archivos_texto

for carpeta in nombres_carpetas:
    if '.user' in carpeta:
        ruta = ruta_carpetas
        archivos_texto = buscar_archivos(ruta)
        for texto in archivos_texto:
            with open(ruta + '/' + texto, 'r') as f:
                mensaje = f.read()
                guardar = mensaje.split(',', 2)
                guardar[0] = guardar[0].replace('{"name":', "")
                guardar[0] = guardar[0].replace('"', "")
                guardar[1] = guardar[1].replace('"email":', "")
                guardar[1] = guardar[1].replace('"', "")
                f.close()
                #datos.append(guardar[0])
                #datos.append(guardar[1])
                for i in range(0, 2):
                    datos[len(datos):] = [guardar[i]]
                #datos[len(datos):] = [guardar[0]]
                #datos[len(datos):] = [guardar[1]]
        break
d = open('/Users/Pablo Velasquez/Downloads/Python/Usuarios.txt', 'w')
x = 0
for escribir in datos:
    if x % 2 == 0:
        d.write(str(int(x-x*0.5)))
        d.write("\n")
        d.write('Nombre: ' + escribir)
        d.write("\n")
    if x % 2 == 1:
        d.write('Email: ' + escribir)
        d.write("\n")
    x = x+1
d.close()