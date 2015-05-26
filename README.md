# pydiceware-es
Generador de passphrases basado en las ideas de diceware

# Uso

El programa `generapassphrase.py` genera una passphrase aleatoria a partr de las palabras contenidas en el archovo (binario) `diccionarios.obj`

Por defecto genera cinco palabras al azar con un total de 60 bits de entropia. Se le pueden pasar las siguientes opciones:

- `-b` permite elegir el total de bits de entropía (cuanto mayor sea, más segura es la passphrase, pero menos comunes serán las palabras y por lo tanto más difíciles de recordar). Por defecto es 60

- '-l`  establece el número de palabras en la passphrase. Un número más alto permite que las palabras sean más comunes para el mismo nivel de entropía. Por defecto es 5.

- una palabra cualquiera pasada como parámetro hace que se ignore la opción `-l`, y fuerza a que cada palabra empiece con la letra correspondiente. Es decir, si la palabra que pasamos es `google`, elegirá la passphrase de forma que la primera palabra empiece por `g`, la segunda por `o` y así sucescivamente.

## Ejemplos:

Para generar una passphrase de 6 letras con 70 bits de entropía

```
./generapassphrase.py -l 6 -b 70
```

Para generar una passphrase cuyas palabras empiecen por las letras `f,a,c,e,b,o,o,k` con 50 bits de entropía

```
./generapassphrase.py facebook -b 50
```


# Generar diciconarios

El programa `seleccionapapalabras.py` sirve para generar el archivo `diccionarios.obj` a partir de varios archivos de texto. Además, genera un archivo llamado `diceware.txt` para ser usado con el método diceware. En este archivo hay una lista de palabras para ser elegidas con cinco tiradas de dado. De este modo se pueden generar passphrases aleatorias sin necesidad de fiarse de un ordenador. Cada una de estas palabras aporta 12.9 bits de entropía.

Para usarlo, simplemente hay que colocar el archivo `seleccionapalabras.py` en un directorio donde haya uno o más archivos de texto (con la extensión `.txt`), y ejecutar

```
python seleccionapalabras.py
```

Automáticamente el programa recorrerá los archivos de texto, extrayendo las palabras y generando la base de datos que guardará en el archivo 'diccionarios.obj'. Al final, seleccionará las 7776 palabras más repetidas y con ellas generará el archivo `diceware.txt`

Los archivos aquí incluídos dueron generados con este método a partir de una colección de libros de dominio público.
