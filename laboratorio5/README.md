# info de la materia: ST0263 Tópicos especiales en telemática
#
# Estudiante(s): Laura Marin Velez, lmarinv2@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co
#
#
# Laboratorio 5
#
## Par de claves

Inicialmente debemos tener creado un par de claves, para esto accedemos a EC2, par de claves, allí le asignaremos un nombre a nuestra clave, esocogemos RSA y .pem, finalmente creamos el par de claves y esta se descargara automaticamente

## Creacion del bucket

Accedemos a amazon s3 y le damos en crear bucket.

De acuerdo a los requisitos de Hadoop, los nombres del bucket y de las carpetas que utilice en Amazon EMR tienen las siguientes restricciones: deben contener solo letras en minúsculas, números, puntos y guiones y no pueden terminar en números 

## Creacion del cluster EMR

Accedemos a amazon EMR y damos clic en crear cluster

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

[1](evidencia/1.png)

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

# Conexion HUE

Accedemos  EMR, historial de aplicaciones copiamos el link de hue y lo abrimos en el navegador, nos pedira crear una cuenta y creamos un usuario hadoop con la contraseña que queramos 

Una vez adentro acedemos a files damos clic en New-directory, accedemos a este directorio y damos clic en upload y agregamos los archivos que deseamos

#

Por ultimo si accedemos de nuevo a EMR via ssh y listamos los archivos veremos la nueva carpeta que creamos via HUE

