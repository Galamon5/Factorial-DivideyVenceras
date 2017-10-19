def FDyV(n):
    if(len(n) < div):
        m = 1
        for i in range(len(n)):
            m = m * int(n[i])#--------------
        return m
    else:
        divisiones = Dividir(n)
        factorial = 1
        for j in range(div):
            factorial = factorial * FDyV(divisiones[i])
        return factorial

def Dividir(n):
    k = 0
    divisiones = createArray(div)
    if(len(n)%div == 0):
        for i in range(div):
            temp = ""
            for j in range((len(n)/div)):
                temp = temp + n[k++]#String.valueOf(n.charAt(k++))----------------
            divisiones[i] = temp
        divisiones[div-1] = n[k:]
    return divisiones

def createArray(size):
    arrayAux = []
    i = 0
    for i in range(size):
        arrayAux.append(random.randint(0,size))
    return arrayAux

def main():
    arreglo = []
    num = int(input("Ingresa el numero\n"))
    div = int(input("Ingresa numero de divisiones que deseas\n"))
    for i in range(num):
        arreglo.append(i)
    resultado = FDyV(arreglo)
    print (num+"! = "resultado)
