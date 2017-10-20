def FDyV(n,div):
    if(len(n) < div):
        m = 1
        for i in range(len(n)):
            m = m * int(n[i])
        return m
    else:
        divisiones = Dividir(n,div)
        factorial = 1
        for j in range(div):
            factorial = factorial * FDyV(divisiones[j],div)
        return factorial

def Dividir(n,div):
    k = 0
    divisiones = createArray(div)
    if(len(n)%div == 0):
        for i in range(div):
            temp = []
            for j in range(int(len(n)/div)):
                temp.append(n[k])
                k = k + 1
            divisiones[i] = temp
    else:
        for i in range(div-1):
            temp = []
            for j in range(int(len(n)/div)):
                temp.append(n[k])
                k = k + 1
            divisiones[i] = temp
        divisiones[div-1] = n[k:]
    return divisiones

def createArray(size):
    arrayAux = []
    for i in range(size):
        arrayAux.append('')
    return arrayAux

def main():
    arreglo = []
    num = int(input("Ingresa el numero\n"))
    div = int(input("Ingresa numero de divisiones que deseas\n"))
    for i in range(num):
        arreglo.append(str(i+1))
    resultado = FDyV(arreglo,div)
    print (str(num) + "! = " + str(resultado))
    input("")

main()
