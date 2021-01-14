import time
numero = int(input("Bienvenido introduzca la cantidad de numeros naturales a sumarse: "))
def sumador(num):
    suma = 0
    for x in range(num+1):
        suma = suma + x
    print("El resultado es:", suma)
    return suma
start = time.time()
sumador(numero)
end = time.time()
print("Tiempo consumido: {} seg".format(end-start))