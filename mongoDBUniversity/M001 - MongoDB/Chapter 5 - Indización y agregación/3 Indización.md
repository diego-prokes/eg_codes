# Indización

Existen variadas maneras de optimizar las búsquedas que se le hacen a una base de datos de MongoDB. Una de las mejores, es, crear índices sobre el campo que se quiere optimizar. Los índices de una base de datos funcionan parecido a como funciona el de un libro. Le permite al sistema realizar búsquedas sin pasar por todos los documentos de una colección.

[Indexes — MongoDB Manual](https://docs.mongodb.com/manual/indexes/)

```shell
db.collection.createIndex( <key and index type specification>, <options> )
```

El siguiente ejemplo crea un índice descendente sobre el campo `name`:

```shell
db.collection.createIndex( { name: -1 } )
```

