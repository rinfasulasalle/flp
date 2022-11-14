import matplotlib.pyplot as plt

# -------------------------------------------------
def txt_a_lista(opc):
    if opc == 0:
        txt = 'resultados\_resultadosPythonBubble.txt'
    elif opc == 1:
        txt = 'resultados\_resultadosPythonMerge.txt'
    # falta agregar elif de lsitas cpp y go
    else:
        print("Opc no valida:",opc)
        return None
    lista_flotante = []
    archivo = open(txt, "r")
    lista_lineas_str = archivo.readlines()
    archivo.close()
    for i in lista_lineas_str:
        lista_flotante.append(float(i))
    return lista_flotante
def generarGrafico(lista, lista2):
    #lista          tamanios
    #lista2         tiempos_acum
    x = lista
    fx = [lista2[0],lista2[3],lista2[6],lista2[9],lista2[12]]   
    gx = [lista2[1],lista2[4],lista2[7],lista2[10],lista2[13]]  
    hx = [lista2[2],lista2[5],lista2[8],lista2[11],lista2[14]]
    
    plt.plot(x, fx)
    plt.plot(x, gx)
    plt.plot(x, hx)

    plt.plot(x, fx, label = "python")
    plt.plot(x, gx, label = "c++")
    plt.plot(x, hx, label = "go")
    plt.legend(loc = "upper left")

    plt.xlabel("Tamanios", )
    plt.ylabel("Tiempo en microsegundos (ms)")

    plt.savefig('diagrama.png')
    plt.show()
# -------------------------------------------------
def main():
    matrizTiempos = []
    max = 2
    for i in range(max):
        matrizTiempos.append(txt_a_lista(i))
    print(matrizTiempos)

# -------------------------------------------------
main()