# Pipeline de agregación¶

El marco de agregación de MongoDB se basa en el concepto de tuberías de procesamiento de datos. Los documentos entran en una tubería de varias etapas que transforma los documentos en un resultado agregado. Por ejemplo

```shell
db.orders.aggregate([
   { $match: { estado: "A" } },
   { $group: { _id: "$cust_id", total: { $sum: "$amount" } } }
])
```

Primera etapa: La etapa *$match* filtra los documentos por el campo de estado y pasa a la siguiente etapa aquellos documentos que tienen estado igual a "A".

Segunda etapa: La etapa *$group* agrupa los documentos por el campo *cust_id* para calcular la suma del importe de cada *cust_id* único.

Las etapas más básicas del pipeline proporcionan filtros que operan como consultas y transformaciones de documentos que modifican la forma del documento de salida.

Otras operaciones de canalización proporcionan herramientas para agrupar y ordenar los documentos por uno o varios campos específicos, así como herramientas para agregar el contenido de las matrices, incluidas las matrices de documentos. Además, las etapas del pipeline pueden utilizar operadores para tareas como el cálculo de la media o la concatenación de una cadena.

El pipeline proporciona una eficiente agregación de datos utilizando operaciones nativas dentro de MongoDB, y es el método preferido para la agregación de datos en MongoDB.

**Ejemplo:**

Para completar este ejercicio, conéctese a su clúster Atlas utilizando el espacio IDE en el navegador al final de este capítulo. ¿Qué tipos de habitaciones están presentes en la colección sample_airbnb.listingsAndReviews?

![](.\1.1.jpg)