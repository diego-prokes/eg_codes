# Búsquedas Complejas

Los operadores de consulta y comparación pueden utilizarse para crear búsquedas más complejas.

```shell
db.<nombre colección>.find({ <"campo">:{<"operador de consulta">:<"valor">}, ... })
```

En las búsquedas normales, se ocupa como operador $eq como operador por defecto.

## Operadores de comparación

Para la comparación de diferentes valores de tipo BSON, véase el [orden de comparación BSON especificado](https://docs.mongodb.com/manual/reference/bson-type-comparison-order/#std-label-bson-types-comparison-order).

| Nombre                                                       | Descripción                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`$eq`](https://docs.mongodb.com/manual/reference/operator/query/eq/#mongodb-query-op.-eq) | Compara valores que son **iguales** a un valor especificado. |
| [`$gt`](https://docs.mongodb.com/manual/reference/operator/query/gt/#mongodb-query-op.-gt) | Coincide con los valores que son **mayores** que un valor especificado. |
| [`$gte`](https://docs.mongodb.com/manual/reference/operator/query/gte/#mongodb-query-op.-gte) | Coincide con los valores que son **mayores o iguales** a un valor especificado. |
| [`$in`](https://docs.mongodb.com/manual/reference/operator/query/in/#mongodb-query-op.-in) | Coincide con **cualquiera** de los **valores especificados** **en un arreglo.** |
| [`$lt`](https://docs.mongodb.com/manual/reference/operator/query/lt/#mongodb-query-op.-lt) | Coincide con los valores que **son menores** que un valor especificado. |
| [`$lte`](https://docs.mongodb.com/manual/reference/operator/query/lte/#mongodb-query-op.-lte) | Coincide con los valores que son **menores o iguales** a un valor especificado. |
| [`$ne`](https://docs.mongodb.com/manual/reference/operator/query/ne/#mongodb-query-op.-ne) | Coincide con todos los valores que **no son iguales** a un valor especificado. |
| [`$nin`](https://docs.mongodb.com/manual/reference/operator/query/nin/#mongodb-query-op.-nin) | Coincide con **ninguno** de los **valores especificados** **en un arreglo.** |

## Operadores de consulta lógica

| Nombre                                                       | Descripción                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`$and`](https://docs.mongodb.com/manual/reference/operator/query/and/#mongodb-query-op.-and) | Une las cláusulas de la consulta con un AND lógico y devuelve todos los documentos que coinciden con las condiciones de ambas cláusulas. El operador AND se usa cuando la consulta une varias expresiones que especifican el mismo operador ( **ej. and [ {or [ {},{} ]},{or [ {},{} ]} ]** ) |
| [`$not`](https://docs.mongodb.com/manual/reference/operator/query/not/#mongodb-query-op.-not) | Invierte el efecto de una expresión de consulta y devuelve los documentos que no coinciden con la expresión de consulta. |
| [`$nor`](https://docs.mongodb.com/manual/reference/operator/query/nor/#mongodb-query-op.-nor) | Une las cláusulas de la consulta con un NOR lógico y devuelve todos los documentos que no coinciden con ambas cláusulas. |
| [`$or`](https://docs.mongodb.com/manual/reference/operator/query/or/#mongodb-query-op.-or) | Une las cláusulas de la consulta con un OR lógico y devuelve todos los documentos que coinciden con las condiciones de cualquiera de las dos cláusulas. |

### Estructura

#### and, or, nor

```shell
db.<nombre colección>.find({ "$and": [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] })
```

```shell
db.<nombre colección>.find({ "$or": [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] })
```

```shell
db.<nombre colección>.find({ "$nor": [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] })
```

#### not

```shell
db.<nombre colección>.find({ field: { $not: { <operator-expression> } } })
```

## $expr

Habrán veces en las cuáles se deseen realizar búsquedas comparando el valor de dos o más campos distintos de un mismo documento. Por ejemplo, en una colección que almacena a los integrantes de una familia, podría querer buscarse cuántos de ellos son primos y hermanos a la vez (drama).

Para realizar dicha búsqueda se debe utilizar un operador nuevo: $expr. $expr se puede combinar con todos los operadores de comparación. ($eq, $lt, $lte,$gt y $gte). La sintaxis que se utiliza es la siguiente:

```shell
db.<nombre colección>.find({"$expr": { "<op>": ["$campo1","$campo2"]} )
```

vale la pena destacar que: `$campo1` y `$campo2`, toman el valor de dichos campos.

## Operadores de array

| Nombre                                                       | Descripción                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`$all`](https://docs.mongodb.com/manual/reference/operator/query/all/#mongodb-query-op.-all) | Coincide con matrices que contienen todos los elementos especificados en la consulta. |
| [`$elemMatch`](https://docs.mongodb.com/manual/reference/operator/query/elemMatch/#mongodb-query-op.-elemMatch) | Selecciona los documentos si el elemento del campo de la matriz coincide con todas las condiciones especificadas en  [`$elemMatch`](https://docs.mongodb.com/manual/reference/operator/query/elemMatch/#mongodb-query-op.-elemMatch). |
| [`$size`](https://docs.mongodb.com/manual/reference/operator/query/size/#mongodb-query-op.-size) | Selecciona los documentos si el campo de la matriz tiene el tamaño especificado. |

