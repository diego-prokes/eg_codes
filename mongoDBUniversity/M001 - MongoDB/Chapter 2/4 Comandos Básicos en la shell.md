# Comandos Básicos en la shell

**Conectarse a un Cluster de Atlas**

```shell
mongo "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/admin"
```

```shell
mongosh "mongodb+srv://sandbox.cew6n.mongodb.net/admin" --username m001-student
```

```shell
mongosh "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.cgfls.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
```

```shell
quit()
```


**Mostrar las bases de datos en el cluster**

```shell
show dbs
```

**Acceder a una base de datos**

```shell
use <nombre bd>
```

**Mostrar las colecciones de una base de datos**

```shell
show collections
```

**Buscar documentos en una colección**

```shell
db.<nombre colección>.find({"field":"value"})
```

Este comando muestra, por defecto, 20 documentos. Si quieren visualizarse los siguientes 20 documentos encontrados. se debe utilizar el comando `it`. Dicho comando nos permite iterar sobre el "cursor", un puntero al resultado de la búsqueda.

**Buscar un único documento en una colección**

```shell
db.<nombre colección>.findOne()
```

**Buscar el número de documentos de una colección que cumplen una condición**

```shell
db.<nombre colección>.find({"field":"value",...}).count()
```

**Mostrar los documentos en el cursor de forma más legible**

```shell
db.<nombre colección>.find({"field":"value"}).pretty()
```

