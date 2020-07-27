
def SubPalindroma(cadena):
    
    ori = cadena  #Cadena original con la que vamos a trabajar
    inver = ori[::-1] #Invertimos la cadena original para poder realizar la comparación
    
    #Vamos a utilizar una matriz en donde se almacenaran las soluciones posibles que se puedan tener
    #La atriz siempre sera cuadra, ya que se tendra el mismo numero de filas y de columnas
    filas = len(ori) + 1 
    columnas = filas    
    Bmax = [[0] * columnas for i in range(filas)] #Creacion de la matriz
    
    # LLENADO DE LA MATRIZ: de izquierda a derecha y de arriba hacia abajo, ya que 
    # se va a comparar el primer caracter de la cadena invertida con cada uno de los caracteres de la cadena original
    for j in range(0,filas):  
        for i in range(0, columnas):
            
            if (i == 0 or j == 0):
                #La primer fila y columna tendran valor 0, ya que con eso es que iniciamos a calcular los valores
                #que contendra la matriz
                 Bmax[j][i] = 0   
                 
            elif (inver[j - 1] == ori[i - 1]): 
                #Si los caracteres de la cadena original y la invertida son iguales en la misma posicion
                #entonces vamos a tomar el valor que tengo en diagonal  y le sumo 1, con esto indicamos que esa letra hace parte
                #de la subcadena palindroma
                 Bmax[j][i] = Bmax[j - 1][i - 1] + 1  
                    
            elif(Bmax[j - 1][i] > Bmax[j][i - 1]):  
                #Cuando los caracteres son diferentes, entonces lo que se hace es validar cual es la mejor opción
                #si, anexar una nueva letra o seguir con la que se estaba trabajando, y esto se hace mirando el tamaño almacnado en la matriz. 
                
                 Bmax[j][i] = Bmax[j - 1][i] 
            else: 
                 Bmax[j][i] = Bmax[j][i - 1]
            
            
    j, i = filas-1, columnas-1 
    #En la ultima posicion de la matrix luego de hacer su llenado, esta almacenada la longitud de la subcadena
    #con esto podemos saber un recorrido de la cadena original, para extraer la solución.
    count = Bmax[j][i] 
    respuesta=''  
    
    while (count > 0):  # Solucion Button-Up, recorremos de atras hacia adelante la cadena original y la invertida. 
        
        if (inver[j-1] == ori[i-1]):
            respuesta += ori[i-1]  #Concateno la letra que hace parte de la palabra
            # Reduzco el tamaño de la matriz sobre los que se seguira busca la respuesta
            i -= 1  
            j -= 1
            count -= 1   #La longitud de subcadena se reduce en 1, porque ya he concatenado una de las letras que hace parte
            
        elif(Bmax[j - 1][i] > Bmax[j][i-1]):
            #Como son diferentes los caracteres, se reduce la matriz ya sea en fila o columna, con base en que valor me ayudara a llegar a la solución
            #es decir el que tenga mayor tamaño
            
            j -= 1  # Reduzco la cantidad de filas sobre las que hare la busqueda            
        else:
            i -= 1    # Reduzco la cantidad de columnas sobre las que hare la busqueda
    
    return  respuesta
 


