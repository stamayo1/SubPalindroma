
def SubPalindroma(cadena):
    
    cadena = cadena.upper()
    ori = cadena.replace(' ', '') 
    inver = ori[::-1] #Invertir la cadena original
    
    filas = len(ori) + 1 #Aumento la longitud cadena en +1, para asi llenar la martrix
    columnas = filas 
    
    # Matrix donde mapeo las soluciones
    Bmax = [[0] * columnas for i in range(filas)]
    
    for j in range(0,filas):  # LLENADO DE LA MATRIX: de izquierda a derecha y de arriba hacia abajo
        for i in range(0, columnas):
            
            if (i == 0 or j == 0):
                 Bmax[j][i] = 0
                 
            elif (inver[j - 1] == ori[i - 1]):
                 Bmax[j][i] = Bmax[j - 1][i - 1] + 1  #Tomo el valor en la posicion diagonal y le sumo 1
                    
            elif(Bmax[j - 1][i] > Bmax[j][i - 1]):  # Tomo el que mayor valor tenga
                 Bmax[j][i] = Bmax[j - 1][i] 
            else: 
                 Bmax[j][i] = Bmax[j][i - 1]
            
            
    j, i = filas-1, columnas-1
    count = Bmax[j][i] # En la ultima posicion de la matrix, esta almacenada la longitud de la subcadena
    respuesta=''  
    
    while (count > 0):  # Solucion Button-Up
        
        if (inver[j-1] == ori[i-1]):
            respuesta += ori[i-1]  #Concateno la letra que hace parte de la palabra
            #Se reduce la cantidad de letras dentro de la subcadena, al igual que los indices 
            #sobre los que se busca la respuesta
            i -= 1
            j -= 1
            count -= 1
        elif(Bmax[j - 1][i] > Bmax[j][i-1]):
            j -= 1  # Reduzco la cantidad de filas sobre las que hare la busqueda            
        else:
            i -= 1    # Reduzco la cantidad de columnas sobre las que hare la busqueda
    
    return  respuesta
 
""" if __name__ == "__main__":
    string = "qwer1235321fr" 
    print(SubPalindroma(string))  """

