# MongoDB

## Configuración de Atlas
Para la realización del curso se configuró en MongoDB Atlas los siguiente: 

| Configuración | Nombre              |
| ------------- | ------------------- |
| Proyecto      | M001                |
| Cluster       | Sandbox             |
| usuario       | m001-student        |
| contrasenia   | m001-mongodb-basics |

#### Resumen

Primero se accedió a MongoDB Atlas y se creó un proyecto con el nombre de M001. Luego, se creó un nuevo Cluster (la opción gratuita) y se le dio el nombre de "SandBox". El resto de sus configuraciones se dejaron por defecto. Ya con el cluster creado se accedió  al apartado de conexión. Se permitió que cualquier IP establezca conexión y se creó un usuario para administrarla.

## Poblar la BD

Para poblar la base de datos se presionaron los tres puntos (...) y se cargo un dataset de prueba. Dicho proceso tarda algunos minutos.

## Establecer la conexión

Para establecer la conexión se volvió a entrar al apartado de conexión. Se seleccionó la opción de Connect with the MongoDb Shell. Luego se apretó el botón 'I have the MongoDB Shell installed' y se seleccionó la última versión de la shell (4.4). Finalmente se ejecutó el comando entregado por la interfaz:

```shell
mongo "mongodb+srv://sandbox.cew6n.mongodb.net/myFirstDatabase" --username m001-student
```

![conexión](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 1\connectionByShell.jpg)