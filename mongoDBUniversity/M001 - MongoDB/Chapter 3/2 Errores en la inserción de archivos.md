# Errores en la inserción de archivos



| Error                               | Descripción                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| Llave repetida                      | Cuando en la inserción del documento, la llave que lo identifica ya existe en la colección. MongoDB arrojará un error y no realizará dicha acción. Esto puede deberse a que estás reescribiendo un documento que existe en la base da datos. Si aún así, decides insertar el documento puedes eliminar el _id del string de inserción. Así, mongo le asignará un id único por defecto. |
| Inserción algunos documentos        | Si el error de llave repetida se da en alguna de las inserciones de un array de inserciones, entonces por defecto ninguna de las inserciones siguientes se realizará. Se puede cambiar dicho comportamiento y hacer que todas las inserciones se ejecuten, menos las con llaves duplicadas, agregando la instrucción ordered:false al string. `db.<nombre colección>.insert( [{},{},...],{"ordered":false} )` |
| Inserción a la colección incorrecta | Si en el comando de inserción se escribe mal el nombre de la colección en la cuál se desean insertar los documentos, entonces MongoDB creará una colección con el nombre indicado e ingresará los datos. Este es un error común que se soluciona eliminando la colección errada y reinsertando los datos en la colección correcta. |

