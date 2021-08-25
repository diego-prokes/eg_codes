# Importar y exportar en MongoDB

> ***Para aplicar estos comandos debes imaginar que te encuentras siempre en el cluster.***
>

Cuando se trabaja con una base de datos de MongoDB, se debe tener muy en consideración que esta almacena la data en forma ficheros BSON. Esta formato, presenta importantes ventajas a la hora de ahorrar espacio en disco y de realizar búsquedas sobre la data, sin embargo es ilegible para el ser humano. No así JSON, que si bien es más lento y pesado, es comprensible a simple vista.

Con esto en mente, puedes sospechar que habrán veces en las que querrás importar data que estaba en formato BSON o JSON a tu BD y otras que querrás exportarlos en cualquiera de estos formatos. Para cada una de dichas acciones existe un comando. Lo que se representa en la tabla siguiente:
> ***Para aplicar estos comandos debes imaginar que te encuentras siempre en el cluster.***

| FUNCIÓN      | JSON        | BSON         |
| ------------ | ----------- | ------------ |
| **exportar** | mongoexport | mongodump    |
| **importar** | mongoimport | mongorestore |

## Exportar
> ***Para aplicar estos comandos debes imaginar que te encuentras siempre en el cluster.***

- Exportar la data en formato BSON:

  - ```bash
    mongodump --uri "<Atlas Cluster URI>"
    ```

  - ```bash
    mongodump --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies"
    ```

- Exportar la data en formato JSON

  - ```bash
    mongoexport --uri "<Atlas Cluster URI>"
    			--collection=<collection name>
    			--out=<filename>.json
    ```

  - ```bash
    mongoexport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies" --collection=sales --out=sales.json
    ```


## Importar
> ***Para aplicar estos comandos debes imaginar que te encuentras siempre en el cluster.***

- Importar la data que está en formato formato BSON:

  - ```bash
    mongorestore --uri "<Atlas Cluster URI>"
    			 --drop dump
    ```

  - ```bash
    mongorestore --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/<database name>"  --drop dump
    ```

    

- Importar la data que está en formato JSON

  - ```bash
    mongoimport --uri "<Atlas Cluster URI>"
    			--drop=<filename>.json
    ```

  - ```bash
    mongoimport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies" --drop=<filename>.json
    ```

