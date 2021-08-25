# Eliminar Documentos

Cuando uno elimina un documento de una colección, este ya no puede recuperarse. Por ende, es muy importante que estas acciones se realicen con sumo cuidado.

## Eliminar una Base de Datos

```
use <nombre base datos>
db.dropDatabase()
```

## Eliminar una colección

Ya sea porque se creó una colección sin querer o por cualquier otro motivo, habrán veces en las que la mejor opción será eliminar toda una colección. En estos casos se puede emplear el siguiente comando en la terminal (se debe contar con los permisos necesarios):

```shell
use <nombre base datos>
db.<nombre colección>.drop()
```

## Eliminar varios documentos

En muchos casos se querrán eliminar todos los documentos que cumplan con una condición de una colección.

```shell
db.<nombre colección>.deleteMany({<"campo">:<"valor">})
```

## Eliminar un sólo documento

Cuando se da la instrucción para borrar un único documento, MongoDB buscará el primer archivo que cumpla la condición especificada y lo eliminará. Esto puede provocar que se elimine un archivo distinto del que se pretendía. Para evitarlo, se recomiendo que dicha búsqueda se haga sobre el _id.

```shell
db.<nombre colección>.deleteMany({<"campo">:<"valor">})
```
