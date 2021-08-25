# Proyecciones en Búsquedas

Cuando se realizan búsquedas en colecciones que contienen documentos muy grandes, la visualización de los resultados suele ser difícil. Para solucionar este problema se crearon las proyecciones. Estas permiten mostrar en pantalla sólo los campos requeridos de cada documento en el *cursor*.

Hasta ahora, cuando se realiza una búsqueda solamente se incluye en el comando de búsqueda la parte que establece las condiciones que se deben cumplir para que un documento se agregue al *cursor*. La segundo parte de este comando corresponderá al filtro que establece qué campos de dichos documentos deben incluirse. La sintaxis es la siguiente:

```shell
db.<nombre colección>.find({<condiciones>},{<campo>:<binario>,...}).pretty()
```

Si la sección `<binario>` si se utiliza un 1, se mostrará dicho campo, si se utiliza un 0, no lo hará. Así se puede hacer ya sea una lista de inclusión o una lista de exclusión de campos.

## $elemMatch

Si bien elemMatch suele utilizarse más en la parte de la consulta que en la parte de la proyección vale la pena agregarlo en este apartado.

### en la parte de consulta

El operador [`$elemMatch`](https://docs.mongodb.com/manual/reference/operator/query/elemMatch/#mongodb-query-op.-elemMatch) coincide con aquellos documentos que contienen un campo del tipo arreglo, el cual contiene al menos un elemento que coincide con todos los criterios de búsqueda especificados. Se suele utilizar cuando se tiene un arreglo de documentos, de los cuales, se quiere que uno de sus campos cumpla con cierta condición.

```shell
db.<nombre colección>.find({ <campo>: { $elemMatch: { <consulta1>, <consulta2>, ... } } })
```

**Ejemplo:**

En este caso se buscan todos los documentos de la colección *grades*, los cuáles en su campo del tipo arreglo *scores* contengan un documentos que almacene un *score* del tipo *extra credit*.

![](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 4\4.1.jpg)

### en la parte de proyección

Proyecta sólo los elementos del array con al menos un elemento que coincida con los criterios especificados.

**Ejemplo:**

Como se puede ver en este caso, se muestran todos los documentos, pero sólo aquellos documentos que presentan un *score* mayor a 85 y el *_id* de cada uno, el cuál se muestra por defecto.

![elemMatch en proyección](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 4\4.2.jpg)

