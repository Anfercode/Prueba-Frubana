# Prueba Frubana 🍎 🍋 🍊.
Este repo tiene la finalidad de realizar la solución de la prueba técnica de frubana. 

# Dependencias.

- **Python 3.7.4** 🐍
- **Manejo de terminal Linux** 💻

## Problema 1.

<<<<<<< HEAD
****
=======
** **
>>>>>>> 25c28cdb912aef356a21077bdaddc3415e4a7e49

La mediana de los números M se define como el número del medio después de ordenarlos en orden si M es
Impar. O es el promedio de los dos números del medio si M es par. Empiezas con un vacío
Lista de números Luego, puede agregar números a la lista o eliminar los números existentes. Después
Cada operación de agregar o quitar, genera la mediana.

**Ejemplo:**

Para un conjunto de M = 5 números 9, 2, 8, 4, 1, la mediana es el tercer número en el conjunto ordenado 1, 2,
4, 8, 9, que es 4. Del mismo modo, para un conjunto de M = 4 números, 5, 2, 10, 4, la mediana es el
promedio del segundo y tercer elemento en el conjunto ordenado 2, 4, 5, 10, que es (4 + 5) / 2 = 4.5.

**Input:**

La primera línea es un número entero, N, que indica el número de operaciones.
Cada uno de los próximos N las líneas son a x o r x:

1. a x indica que x se agrega al conjunto
2. r x indica que x es eliminado del conjunto.

**Output:**

Para cada operación: si la operación es agregar, genera la mediana después de agregar x en una sola línea.
Si la operación es eliminar y el número x no está en la lista, la salida ¡Incorrecto! En una sola línea. Si
la operación es eliminar y el número x está en la lista, muestra la mediana después de eliminar x en
Una sola línea. (Si el resultado es un entero, NO envíe el punto decimal. Y si el resultado es un
número real, NO muestre ceros finales).

**Nota:** Si su mediana es 3.0, imprima solo 3. Y si su mediana es 3.50, imprima solo 3.5. Cuando
necesita imprimir la mediana y la lista está vacía, imprima Wrong

**Restricciones:**
1. 0 < N <= 10**5

Para cada a x o r x, x siempre será un entero con signo (que se ajustará en 32 bits).

<<<<<<< HEAD
**Sample Input:**

7

r1

a1

a2

a1

r1

r2

=======
Sample Input:

7
r1
a1
a2
a1
r1
r2
>>>>>>> 25c28cdb912aef356a21077bdaddc3415e4a7e49
r1

**Sample Output:**

Wrong!

1

1,5

1

1,5

1

Wrong!

**Nota:** Como es evidente desde la última línea de la entrada, si después de la operación de eliminación
la lista se convierte vacío, tienes que imprimir Wrong!

## Problema 2.

<<<<<<< HEAD
****
=======
** **
>>>>>>> 25c28cdb912aef356a21077bdaddc3415e4a7e49

Se le da un árbol sin raíz de n nodos numerados del 1 al n. cada nodo tiene un color C sub i sea d(i,j) el número de colores diferentes en la ruta entre el nodo i y el nodo j. por
cada nodo i , calcular el valor de la sumatoria de d(i,j)

Tu tarea es imprimir el valor de sumatoria de d(i,j) para cada nodo 1 ≤ i ≤ n.

**Restricciones:**

1 ≤ nodes ≤ 10**5

1 ≤ colour_nodes ≤ 10**5

**Sample Input:**

5

1 2 3 2 3

1 2

2 3

2 4

1 5

**Sample Output:**

10

9

11

9

12

# Preguntas. ❓ ❓ ❓ 

**1- ¿Cuáles serían las cualidades para un código limpio?**

Para mí las cualidades para un código limpio sería un código con 
nombres de variables y funciones mnemotécnica y bastante descriptivas, y que lleve principios SOLID, esto para que el código sea reutilizable o modular, mantenible y testeable.

**2- ¿Cuáles serían los estándares según tú para un buen proyecto?**

En mi opinión no puede haber un buen proyecto sin algo de desorden o caos pero para mí un proyecto que use buenas prácticas como el manejo de patrones de diseño y principios SOLID seria el proyecto sería un proyecto más manejable y más amigable para trabajar

**3- ¿Qué patrones conoce y utiliza?**

Los patrones que conozco son el singleton, el factory y el command, pero el que mas suelo utilizar es el singleton

# Estadisticas 📈

En esta seccion encontraras el tiempo invertido en horas para realizar la prueba y el tiempo por archivo, [click aqui va ver con detalle](https://wakatime.com/@Anfercode/projects/xtwfglflac?start=2019-08-13&end=2019-08-19), la herramienta utilizada para estas metricas se llama [Wakatime](https://wakatime.com).
****

Hecho con ❤️ por Andres Campero 😃