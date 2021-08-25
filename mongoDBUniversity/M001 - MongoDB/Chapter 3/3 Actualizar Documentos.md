# Actualizar Documentos

Las cosas cambian y a menudo se necesita actualizar la data almacenada en una base de datos. Por esta razón se analizan las formas que se tienen para realizar cambios en los documentos de una base de datos de MongoDB.

## Actualizar docs. con el Explorador de Datos de Atlas

![Editar documento](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 3\3.1.jpg)

![Agregar elemento](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 3\3.2.jpg)

![Confirmar los cambios al documento](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 3\3.4.jpg)

## Actualizar docs. con la Mongo Shell

Cuando se actualizan los documentos de una base de datos es importante poder seleccionar aquellos que desean ser modificados. Mediante la terminal se puede actualizar un único documento o varios a la vez. Ambos comandos comparten en gran medida su estructura. Reciben dos argumentos, el primero indica la condición que debe cumplir el documento que se actualizará y el segundo, la instrucción que indica qué modificación debe realizarse.

**Un documento a la vez**

```shell
db.<nombre colección>.updateOne( {<"field">:<"value"}, {<"operador de actualización">: {<"field">:<"value"} })
```

**Varios documentos a la vez**

```shell
db.<nombre colección>.updateMany( {<"field">:<"value"}, {<"operador de actualización">: {<"field">:<"value"} })
```

# Operadores de Actualización

Los siguiente modificadores están disponibles para usar en operaciones de actualización; por ejemplo, en [`db.collection.update()`](https://docs.mongodb.com/manual/reference/method/db.collection.update/#mongodb-method-db.collection.update) y [`db.collection.findAndModify()`](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#mongodb-method-db.collection.findAndModify).

Las operaciones deben escribirse en un documento de la forma:

```
{
   <operator1>: { <field1>: <value1>, ... },
   <operator2>: { <field2>: <value2>, ... },
   ...
}
```

### Campos

| Name                                                         | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`$currentDate`](https://docs.mongodb.com/manual/reference/operator/update/currentDate/#mongodb-update-up.-currentDate) | Establece el valor de un campo a la fecha actual, ya sea como una Date o una Timestamp. |
| [`$inc`](https://docs.mongodb.com/manual/reference/operator/update/inc/#mongodb-update-up.-inc) | Incrementa el valor del campo por la cantidad especificada.  |
| [`$min`](https://docs.mongodb.com/manual/reference/operator/update/min/#mongodb-update-up.-min) | Sólo actualiza el campo si el valor especificado es menor que su valor actual. |
| [`$max`](https://docs.mongodb.com/manual/reference/operator/update/max/#mongodb-update-up.-max) | Sólo actualiza el campo si el valor especificado es mayor que su valor actual. |
| [`$mul`](https://docs.mongodb.com/manual/reference/operator/update/mul/#mongodb-update-up.-mul) | Multiplica el valor del campo por la cantidad especificada.  |
| [`$rename`](https://docs.mongodb.com/manual/reference/operator/update/rename/#mongodb-update-up.-rename) | Renombra el campo.                                           |
| [`$set`](https://docs.mongodb.com/manual/reference/operator/update/set/#mongodb-update-up.-set) | Establece el valor del campo especificado.                   |
| [`$setOnInsert`](https://docs.mongodb.com/manual/reference/operator/update/setOnInsert/#mongodb-update-up.-setOnInsert) | Establece el valor de un campo si la actualización realizada resulta en la inserción de un documento. No tiene efecto en una actualización que modifica un documento existente. |
| [`$unset`](https://docs.mongodb.com/manual/reference/operator/update/unset/#mongodb-update-up.-unset) | Remueve el campo especificado del documento.                 |

### Array

#### Operators

| Name                                                         | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`$`](https://docs.mongodb.com/manual/reference/operator/update/positional/#mongodb-update-up.-) | Acts as a placeholder to update the first element that matches the query condition. |
| [`$[\]`](https://docs.mongodb.com/manual/reference/operator/update/positional-all/#mongodb-update-up.---) | Acts as a placeholder to update all elements in an array for the documents that match the query condition. |
| [`$[\]`](https://docs.mongodb.com/manual/reference/operator/update/positional-filtered/#mongodb-update-up.---identifier--) | Acts as a placeholder to update all elements that match the `arrayFilters` condition for the documents that match the query condition. |
| [`$addToSet`](https://docs.mongodb.com/manual/reference/operator/update/addToSet/#mongodb-update-up.-addToSet) | Adds elements to an array only if they do not already exist in the set. |
| [`$pop`](https://docs.mongodb.com/manual/reference/operator/update/pop/#mongodb-update-up.-pop) | Removes the first or last item of an array.                  |
| [`$pull`](https://docs.mongodb.com/manual/reference/operator/update/pull/#mongodb-update-up.-pull) | Removes all array elements that match a specified query.     |
| [`$push`](https://docs.mongodb.com/manual/reference/operator/update/push/#mongodb-update-up.-push) | Agrega un elemento a un array.                               |
| [`$pullAll`](https://docs.mongodb.com/manual/reference/operator/update/pullAll/#mongodb-update-up.-pullAll) | Removes all matching values from an array.                   |

#### Modifiers

| Name                                                         | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`$each`](https://docs.mongodb.com/manual/reference/operator/update/each/#mongodb-update-up.-each) | Modifies the [`$push`](https://docs.mongodb.com/manual/reference/operator/update/push/#mongodb-update-up.-push) and [`$addToSet`](https://docs.mongodb.com/manual/reference/operator/update/addToSet/#mongodb-update-up.-addToSet) operators to append multiple items for array updates. |
| [`$position`](https://docs.mongodb.com/manual/reference/operator/update/position/#mongodb-update-up.-position) | Modifies the [`$push`](https://docs.mongodb.com/manual/reference/operator/update/push/#mongodb-update-up.-push) operator to specify the position in the array to add elements. |
| [`$slice`](https://docs.mongodb.com/manual/reference/operator/update/slice/#mongodb-update-up.-slice) | Modifies the [`$push`](https://docs.mongodb.com/manual/reference/operator/update/push/#mongodb-update-up.-push) operator to limit the size of updated arrays. |
| [`$sort`](https://docs.mongodb.com/manual/reference/operator/update/sort/#mongodb-update-up.-sort) | Modifies the [`$push`](https://docs.mongodb.com/manual/reference/operator/update/push/#mongodb-update-up.-push) operator to reorder documents stored in an array. |

### Bitwise

| Name                                                         | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`$bit`](https://docs.mongodb.com/manual/reference/operator/update/bit/#mongodb-update-up.-bit) | Performs bitwise `AND`, `OR`, and `XOR` updates of integer values. |
