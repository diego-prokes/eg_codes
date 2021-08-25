# Métodos sort() y limit()

Una vez que se ha realizado una búsqueda en un colección mediante el método de colección: *find()* el cursor almacena los resultados de dicha búsqueda. Sin embargo, a menudo no se quieren obtener todos los resultados de la misma. Por ejemplo, si se tiene una colección de viajeros, puede querer responderse la pregunta: ¿En qué año nació el ciclista más joven de la colección sample_training.trips?

Para conocer su respuesta, se puede recurrir a los métodos de cursor: sort() y find()

## sort()

Especifica el orden en que la consulta devuelve los documentos coincidentes. Debe aplicar sort() al cursor antes de recuperar cualquier documento de la base de datos.

El método sort() tiene el siguiente parámetro:

| Parámetro | Tipo      | Descripción                                             |
| :-------- | :-------- | :------------------------------------------------------ |
| `sort`    | documento | Un documento que define el orden del set de resultados. |

El parámetro `sort` contiene pares de campos y valores, de la siguiente forma

```
{ field: value }
```

##  limit()

El parámetro `limit` contiene un entero que determina el número de resultados que se mostrarán

## Desarrollo ejemplo

![](.\2.1.jpg)

De este ejemplo es importante recalcar que al realizar la búsqueda el campo de *birth year* se debe establecer que dicho valor no puede estar vacío, para que el orden se ejecute correctamente y la búsqueda muestre el resultado deseado.