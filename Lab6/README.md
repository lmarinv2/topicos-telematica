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


