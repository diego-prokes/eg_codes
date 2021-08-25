# Ejercicios de Búsquedas

![lab 2: Operadores Lógicos](C:\Users\dfpro\Desktop\M001 - MongoDB\Chapter 4\2.4.jpg)

```shell
db.companies.find({"$or":[ {"$or":[{"founded_year":2004,"category_code":"social"},{"founded_year":2004,"category_code":"web"}]}, {"$or": [{"founded_month":10,"category_code":"social"},{"founded_month":10,"category_code":"web"}]} ]}).count()
```

