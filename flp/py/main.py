import random
from time import time

from bubble import bubbleSort
from merge import mergeSort
# ------------------------------------------------------ 
def generarArr(tam):
    lista = []
    for i in range(0,tam):
        lista.append(random.randrange(1,tam))
    return lista
def contarTiempo(lista,funcion):
    # lista     lista_entrada
    # funcion   algopritmo de ordenamiento a usar
    inicio = time()
    funcion(lista)
    tiempo_ = time() - inicio
    return tiempo_
def guardarLista(lista,opc):
    if opc == 0:
        txt = 'resultados\_resultadosPythonBubble.txt'
    elif opc == 1:
        txt = 'resultados\_resultadosPythonMerge.txt'
    else:
        print("Opc no valida:",opc)
        return None
    archivo = open(txt,'w')
    for i in range(len(lista)):
        #print(lista[i])
        texto = str(lista[i]) + "\n"
        archivo.write(texto)
    archivo.close()
# ---------------------------------------------------------
def promedioResultados(matrizResultados,indice):
    total = 0
    for i in range(len(matrizResultados)):
        #print("interacion", i)
        for j in range(len(matrizResultados[i])):
            #print("j:", j)
            #print("t[", i, "][", j, "]:", matrizResultados[i][j])
            j = j + 1
        total = total + matrizResultados[i][indice]
        #print("total en interacion", i, ": ", total)
        #print("-------------------------")
    promedio = total / len(matrizResultados)
    #print("tamanio:",len(matrizResultados))
    return promedio
# --------------------------------------------------------- 
def main():
    tamanios = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000]
    #tamanios = [1000,1500,2000,2500,3000,3500,4000,6000]
    #tamanios = [10,15,20,20,30,35]
    total_b = []
    total_m = []
    promedio_b = []
    promedio_m = []
    numEjecuciones = 5

    inicio = time()
    for iterador in range(numEjecuciones):
        lista_arrays = []    # lista de listas generadas
        lista_tiempo_b = []
        lista_tiempo_m = []
        # Creo arrays en base a los tamanios y cada lista la agrego en lista_arrays
        for i in tamanios:
            lista_arrays.append(generarArr(i))
        #print(lista_arrays)
        # Para cada elemento de  lista_arrays le cuento el tiempo que demora y lo agrego en lista_tiempo_b o lista_tiempo_m
        for j in lista_arrays:
            lista_tiempo_b.append(contarTiempo(j,bubbleSort))
            lista_tiempo_m.append(contarTiempo(j,mergeSort))
        #print("lista_tiempo_b:",lista_tiempo_b)
        #print("lista_tiempo_m:",lista_tiempo_m)
        total_b.append(lista_tiempo_b)
        total_m.append(lista_tiempo_m)
    #-------------------
    for x in range(len(tamanios)):
        promedio_b.append(promedioResultados(total_b,x))
        promedio_m.append(promedioResultados(total_m,x))
    #print("promedio_b:",promedio_b)
    #print("promedio_m:",promedio_m)
    guardarLista(promedio_b,0)
    guardarLista(promedio_m,1)

    tiempo = time() - inicio
    print("---------------------------------------------")
    print("Tiempo total python de",tiempo,"segundos.") 
#---------------------------------------------------------- 
main()

