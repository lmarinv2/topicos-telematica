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


En crear cluster accedemos a opciones avanzadas y tendremos varios pasos
* Paso 1: usaremos emr-5.26.0 y activaremos 
    - Hadoop 2.8.5 
    - hive 2.3.5 
    - spark 2.4.3 
    - sqoop 1.4.7 
    - oozie 5.1.0. 

    tambien seleccionamos usar metadatos en la tabla de hive y spark

* Paso 2: dejamos los valores por defecto y para el tipo de instancia cambiamos las 3 a m4.xlarge y cambiamos el volumen a 20 GiB

* Paso 3: le asignamos el nombre al cluster

* Paso 4: asignamos el par de claves que creamos anteriormente y dejamos los demas valores por defecto 

Debemos habilitar los puertos de las aplicaciones que vamos a usar, para esto accedemos a EMR, bloquear acceso público y agregamos los puertos
22
8088
18080
50070
8888

Luego accedemos al cluster, damos clic en resumen y abrimos los grupos de seguridad para principal y habilitamos los mismoa puertos que habilitamos anteriormente

Imagen: [4](evidencias/4.png) - [5](evidencias/5.png) - [6](evidencias/6.png) - [7](evidencias/7.png) - [8](evidencias/8.png) - [9](evidencias/9.png)

## Conexion SSH a EMR

En instancias ec2 se habran creato 3 maquinas, nos conectaremos en la master

```
ssh -i "lab5.pem" hadoop@ec2-54-158-177-169.compute-1.amazonaws.com
```
Una vez conectada ejecutamos los siguiente comandos para obtener los datasets

```
sudo yum install git
git clone https://github.com/st0263eafit/st0263-2022-2.git
```
Para verificar que si obtuvimos todos los recursos accedemos a la carpeta y listamos el contenido

```
cd st0263-2022-2/bigdata/datasets/
ls
```
Ahora crearemos una carpeta dentro del hadoop file system y copiamos los datos allí

```
hdfs dfs -mkdir /user/hadoop/datasets
hdfs dfs -copyFromLocal * /user/hadoop/datasets
```

Cuando el cluster se termine estos archivos serán eliminados automaticamente para conservarlos serán guardadas en el bucket s3 que creamos anteriormente

```
hadoop distcp /user/hadoop/datasets/* s3a://"Nombre de su Bucket"/datasets
```

Imagen: [10](evidencias/10.png) - [11](evidencias/11.png) - [12](evidencias/12.png) - [13](evidencias/13.png) - [14](evidencias/14.png)

# Conexion HUE

Accedemos  EMR, historial de aplicaciones copiamos el link de hue y lo abrimos en el navegador, nos pedira crear una cuenta y creamos un usuario hadoop con la contraseña que queramos 

Una vez adentro acedemos a files damos clic en New-directory, accedemos a este directorio y damos clic en upload y agregamos los archivos que deseamos
Imagen: [15](evidencias/15.png) - [16](evidencias/16.png)


#

Por ultimo si accedemos de nuevo a EMR via ssh y listamos los archivos veremos la nueva carpeta que creamos via HUE

Imagen: [17](evidencias/17.png)

# Ejercicios básicos de MapReduce con MRJOB en python

Para este punto vamos a usar la carpeta Datasets, y los codigos de python.
Al ejecutar cada uno obtenemos lo siguiente 

p1_1.py El salario promedio por Sector Económico (SE)

p1_2.py El salario promedio por Empleado

p1_3.py Número de SE por Empleado que ha tenido a lo largo de la estadística

p2_1.py Por acción, dia-menor-valor, día-mayor-valor

p2_2.py Listado de acciones que siempre han subido o se mantienen estables.

p2_3.py  DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.

p3_1.py Número de películas vista por un usuario, valor promedio de calificación

p3_2.py Día en que más películas se han visto

p3_3.py Día en que menos películas se han visto

p3_4.py Número de usuarios que ven una misma película y el rating promedio

p3_5.py Día en que peor evaluación en promedio han dado los usuarios

p3_6.py Día en que mejor evaluación han dado los usuarios

p3_7.py La mejor y peor película evaluada por genero

