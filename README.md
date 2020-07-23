# SubPalindroma
Código para encontrar la subcadena más larga que sea palindroma dentro de una secuencia de caracteres. 

### Explicación
REST API con template, que procesa una cadena de texto con el fin de encontrar la subcadena más larga que sea palindroma presente en ella.

Se implento programacion dinámica para llevar a cabo la solución de este problema de forma optima, donde se tenia que tener presente que, dado 
el caso en que la cadena sea demasiado grande, se tendrian que hacer muchas validaciones que aumentaría la complejidad computacional requerida, 
que se traduce en tiempo de espera para presentar el resultado. 

La complejidad que posee actualmente es de O(m*n). Calculos basados en conocimientos adquiridos en la materia Fundamentos de analisis y diseño de algoritmos

# Contruido con 🔧
### Back - end
*Python (3.7+), Flask (1.1.1+) 
### Front - end 🎨
*Templates (HTML)

# Intrucciones de ejecución 📋
* Si no se tiene instalo Flask:
```
pip install -r requeriments.txt
```
* Ejecutar servidor de forma local:

```
python app.py
```
* Ejecutar archivo de pruebas unitarias:

```
python test.py
```

## Autor ✒️

* **Sebastián Tamayo Lasso** - *Desarrollador* 
