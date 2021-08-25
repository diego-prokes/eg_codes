# Operadores de arreglos y sub-documentos

La sintaxis de una base de datos en MongoDB es muy flexible. Los campos de un documento pueden contener todo tipo de datos: enteros, fechas, booleanos, caracteres, cadenas de texto e incluso arreglos y documentos. Incluso se pueden crear arreglos de documentos, los que a su vez pueden contener arreglos de documentos. Las posibilidades son infinitas. Es por esto que MongoDB cuenta con herramientas que le permiten al operador de la base de datos acceder a dichos datos.

## Sub-Documentos

En la imagen siguiente se observa un ejemplo de un sub-documento asociado a los campos *start station location* y *end station location*.

![Colección que ejemplifica lo explicado, con sus campos *start station location* y *end station location*](.\5.1.jpg)

Para buscar la información ubicada dentro de uno de estos campos se debe usar la siguiente sintaxis de comando:

```shell
db.<nombre colección>.find({<"campo documento">.<"campo sub-documento">:<"valor">})
```

Un ejemplo de esto sería el siguiente comando:

```shell
db.trips.find({"start station location.type":"Point"})
```

Este permite encontrar todos los documentos de la colección *trips* que en su campo *start station location*, almacenan un documento, el cuál posee el valor *Point* asociado al campo *type*.

## Arreglo de documentos

Habrán otras veces en las cuales un campo se asocie a un array de documentos, como en la imagen siguiente.

![ejemplo de campo asociado a array de elementos](.\5.2.jpg)

Para realizar búsquedas sobre los elementos de este campo, la opción que se plantea para este caso es conocer la posición que guarda el documento sobre el que se desea realizar la búsqueda en el arreglo. Luego, mediante su posición se puede acceder a él de la siguiente forma.

```shell
db.<nombre colección>.find({<"campo">.<pos>.<"campo sub-documento": <"value"> })
```

ejemplo:

```shell
db.companies.find({ "relationships.0.person.last_name": "Zuckerberg" },{ "name": 1 }).pretty()
```

