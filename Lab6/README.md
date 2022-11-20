# info de la materia: ST0263 Tópicos especiales en telemática
#
# Estudiante(s): Laura Marin Velez, lmarinv2@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co
#
#
# Laboratorio 6
#
## CONEXION A EMR

Inicialmente dedemos tener creado nuestro EMR.

Nos conectamos via ssh a este 

[EMR-shh](evidencias/emr-1.png)

## Wordcount en Apache Spark EN AWS EMR 6.3.1

De los laboratorios anteriores ya debemos tener creado el bucket de s3 con todos los archivos 

## De forma interactiva via 'pyspark' (en el nodo master de EMR)

    $ pyspark
    >>> files_rdd = sc.textFile("hdfs:///datasets/gutenberg-small/*.txt")
    >>> files_rdd = sc.textFile("s3://st0263datasets/gutenberg-small/*.txt")
    >>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    >>> wc = wc_unsort.sortBy(lambda a: -a[1])
    >>> for tupla in wc.take(10):
    >>>     print(tupla)
    >>> wc.saveAsTextFile("hdfs:///tmp/wcout1")

* asi salva wc un archivo por rdd.
* si quiere que se consolide en un solo archivo de salida:

        $ pyspark
        >>> ...
        >>> ...
        >>> wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout2")


[pyspark via ssh-1](evidencias/emr-2.png)

[pyspark via ssh-2](evidencias/emr-3.png)

## Desde Zeppelin Nodebook:

Accedemos a Zeppelin

- Creamos un nuevo notebook
- pegamos el codigo de python y lo corremos

[zeppelin-1](evidencias/emr-4.png)

[zeppelin-2](evidencias/emr-5.png)


## Jupyter Notebooks en EMR

Primero debemos crear un notebook para abrilo con jupyter

![image](https://user-images.githubusercontent.com/53051440/202915545-66ac8ed0-c084-4cc3-878c-64ae22b0041f.png)

Abrimos el notebook y ejecutamos los siguientes comandos

![image](https://user-images.githubusercontent.com/53051440/202915619-4f250ce2-df71-40a2-bdfd-635177f71a52.png)

![image](https://user-images.githubusercontent.com/53051440/202915630-668cd1fb-783e-4014-ab4b-3e4a38fe769b.png)

![image](https://user-images.githubusercontent.com/53051440/202915635-f1bacf5d-db69-4558-a968-34ad5a626774.png)

![image](https://user-images.githubusercontent.com/53051440/202915642-45fb8960-2805-4c89-bd59-a6ee5db202ad.png)

![image](https://user-images.githubusercontent.com/53051440/202915647-f8063a03-db25-4b38-a5b3-6682aad445a4.png)

![image](https://user-images.githubusercontent.com/53051440/202915656-e154b8e4-02b1-4207-83e2-a33a0bd07cee.png)

![image](https://user-images.githubusercontent.com/53051440/202915668-ab033ec9-7885-42c7-8798-ec289a0c09c2.png)

## HIVE y SparkSQL, GESTIÓN DE DATOS VIA SQL:

- Crear la tabla HDI en EMR/S3/Hue/Hive:

![image](https://user-images.githubusercontent.com/53051440/202915769-2a9e2787-1ca5-4abe-8537-d4013c5fd2e2.png)

- hacer consultas y cálculos sobre la tabla HDI:

![image](https://user-images.githubusercontent.com/53051440/202915842-e460e7a3-9c7f-4f66-8299-d2f60fdffdb0.png)

![image](https://user-images.githubusercontent.com/53051440/202915846-fbbfc3b0-e8e4-4aec-978f-3687ea1e89fc.png)

![image](https://user-images.githubusercontent.com/53051440/202915850-9a0cb793-be25-42ae-9875-027f7fa3fcf0.png)

- WORDCOUNT EN HIVE:

![image](https://user-images.githubusercontent.com/53051440/202915862-b39d670c-7f53-46d1-970b-37d7e7f722c0.png)

![image](https://user-images.githubusercontent.com/53051440/202915868-3f5bd9a6-b939-4d34-83e4-cf00d8c199f1.png)

![image](https://user-images.githubusercontent.com/53051440/202915880-f2c2d1cc-1956-44a9-b527-b892dda805ad.png)


## RETO

![image](https://user-images.githubusercontent.com/53051440/202915914-77d67b65-fc1c-4d6e-bec7-53d916fa7a72.png)

![image](https://user-images.githubusercontent.com/53051440/202915919-ff7e0e01-cb4f-4228-993a-bfcb857e3e30.png)

![image](https://user-images.githubusercontent.com/53051440/202915927-974e1911-c581-4910-9356-2c56d86fbe4c.png)

![image](https://user-images.githubusercontent.com/53051440/202915936-5a742347-f5be-4fa5-9fd2-c4dc63ee0e57.png)

![image](https://user-images.githubusercontent.com/53051440/202915944-8f798f52-ce39-4e3c-b652-a2212cd43632.png)


## resultados 

![image](https://user-images.githubusercontent.com/53051440/202916059-36dba016-755c-4758-a336-a5c193fc8a38.png)







