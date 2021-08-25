# Insertar Documentos en una colección

Como una base da datos de MongoDB, se compone de colecciones, las cuales a su vez lo hacen de documentos, los cuales tienen pares "campo":"valor". Al crear un documento, automáticamente se genera un campo:"_id" y se le asigna un valor del tipo ObjectId. Sin embargo, uno puede seleccionar el valor y el tipo de dicho campo, con la salvedad de que **debe ser único en la colección**

## Inserciones con la GUI de MongoDB Atlas

Para insertar un documento a una base de datos alojada en MongoDB Atlas, se puede hacer de dos formas. Una es, mediante la GUI de la misma aplicación y la otra es mediante una terminal de comandos. En esta ocasión se explicará la primera.

1. Primero se debe acceder a las colecciones.

   ![Admin de colecciones](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 3\1.1.jpg)

2. Luego hay que acceder a la colección en la que se quiere ingresar el documento.

   ![Acceder a una colección](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 3\1.2.jpg)

3. Finalmente con el botón de "Insertar Documento", se accede a un panel que permite crear el nuevo documento.

   ![Acceder a la creación de Documentos](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 3\1.3.jpg)

   ![Creación de Documentos](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 3\1.4.jpg)

## Inserciones mediante la shell

Existe más de una terminal con la que se puede establecer una conexión, hacer peticiones y cambios en una base de datos de MongoDB. Las más usadas son *mongo* y *mongosh*. Por otro lado, existen dos formas de insertar documentos mediante la terminal, estos son: eliminando una colección y volviendo a crearla con los cambios hechos o insertando sólo los cambios.

### Importar colecciones

Se pueden utilizar los comandos `mongoimport` y `mongorestore` abordados en el Chapter 2. Es muy importante agregar el parámetro --drop para que no existan errores debido a id repetidos.

### Insertar sólo los documentos nuevos

1. Primero debes obtener la conexión con el Cluster de Atlas.

2. Navegar a la base de datos que necesitamos.

3. Insertar el documento a la base de datos
   
    ```shell
    db.<nombre colección>.insert( {<"field":"value">,...} )
    ```
    

## Insertar Múltiples Documentos

Para insertar múltiples documentos deben ingresarse dentro de un array.

```shell
db.<nombre colección>.insert( [ {"field":"value"},{...},... ] )
```

## Consideraciones

1. Pueden existir documentos idénticos dentro de una colección siempre y cuando su _id sea distinto. Sin embargo esto puede generar problemas: inconsistencia en la información y mal uso del espacio en disco son algunos de ellos.
2. MongoDB tiene una funcionalidad que  valida el esquema de los documentos. Lo que te ayuda a prevenir la inserción de archivos mal estructurados. Al usar esta funcionalidad se está optando por hacer uno uso semi relacional con la base de datos, lo que le quita flexibilidad al sistema.

