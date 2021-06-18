# HerramientasComputacionales
En este repositorio se encuentran las soluciones a los ejercicios visto a lo largo del curso de Herramientas Computacionales


### Ejercicio Evaluacion
Para calcular la nota final de un curso, se realizó un algoritmo el cual debió seguir la distribución siguiente:
- 2 parciales: cada uno del 25%
- taller: 20%
- proyecto: 30%

#### Los datos de entrada son: 
- Nota parcial 1
- Nota parcial 2
- Nota taller
- Nota proyecto

#### Los datos de salida son:
- Nota final del curso

##### ¿Cómo se calcula?
El algoritmo calcula la nota final del curso de la siguiente manera: 
Nota_final=Nota_parcial_1*25%+Nota_parcial_*25%+nota_taller*20%+nota_proyecto*30%

La implementación puede verse en el archivo: [evaluacion.py](evaluacion.py)


### Ejercicio Grados

Elaborar un algoritmo que realice la transformación de grados Celsius a Fahrenheit

#### Los datos de entrada son: 
- Grados celsius

#### Los datos de salida son:
- Grados Fahrenheit

##### ¿Cómo se calcula?
El algoritmo calcula los grados Fahrenheit de la siguiente manera:

grados_f=(32-grados_celsius)*(5/9)

La implementación puede verse en el archivo: [grados.py](grados.py)


### Ejercicio Moneda

Elaborar un algoritmo casa de cambio, que reciba una cantidad de dinero en pesos colombianos y
realice su equivalente en dolares, yenes y euros, tenga en cuenta que el cambio deberá realizarse a la
tasa representativa de cada moneda (actual) y que la casa de cambio, incluye un 2% de ganancia a ese
valor.

#### Los datos de entrada son: 
-Pesos colombianos

#### Los datos de salida son:

- Dolares
- Yenes
- Euros

##### ¿Cómo se calcula?
El algoritmo calcula los dolares, yenes y euros de la siguiente manera:
- dolares=pesos_col*0.00027
- yenes=pesos_col*0.029
- euros=pesos_col*0.00023

La implementación puede verse en el archivo: [moneda.py](moneda.py)

### Ejercicio triangulo

Para el problema numero 5 se desea crear un algoritmo para calcular el área de un triángulo cuya 
altura es de x y la base es de y.

#### Los datos de entrada son: 
- x=base
- y=altura

#### Los datos de salida son:
- Area del triangulo

##### ¿Cómo se calcula?
Se calcula en base a la fórmula para calcular el área de un triángulo la cual es BASExALTURA/2, 
es decir (X x Y)/2
Finalmente el algoritmo nos arroja el resultado del área con unidades de cm^2.
La implementación puede verse en el archivo: [triangulo.py](triangulo.py)

