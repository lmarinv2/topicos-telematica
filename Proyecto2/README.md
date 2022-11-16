# st0263-2266 Topicos especiales en telemática
## Estudiante: Laura Marin Velez - lmarinv2@eafit.edu.co
## Profesor: Edwin Nelson Montoya Múnera - emontoya@eafit.edu.co
#
# Proyecto 2
# 1. breve descripción de la actividad

Despliegue de MOODLE escalable, utilizando los recursos de AWS, para la base de datos RDS y para el sistema de archivos EFS. Tambien usaremos el balanceador de cargas.

#
# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

Amazon EC2 Auto Scaling es un servicio completamente administrado diseñado para lanzar o terminar instancias de Amazon EC2 automáticamente con el objetivo de garantizar el número correcto de instancias de Amazon EC2 disponibles para administrar la carga de su aplicación. Amazon EC2 Auto Scaling ayuda a conservar el nivel de disponibilidad de las aplicaciones mediante la administración de flotas de instancias EC2, lo que detecta y reemplaza instancias defectuosas, y mediante el escalado de la capacidad de Amazon EC2 automáticamente en función de las condiciones definidas. Puede usar Amazon EC2 Auto Scaling para incrementar automáticamente la cantidad de instancias EC2 de Amazon durante los picos de demanda, a fin de mantener el nivel de rendimiento y reducir la capacidad durante los periodos de menor demanda para minimizar los costos.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# EFS 

Amazon EFS es un servicio de almacenamiento de archivos para utilizar con computación de Amazon (EC2, contenedores, sin servidor) y servidores locales.

## Configuracion

- Entramos a EFS de amazon 

- Damos click en crear un sistema de archivos y lo creamos 

Imagen: [EFS](evidencias/efs-1.png)

# RDS 

Amazon Relational Database Service (Amazon RDS) es un servicio web que facilita la configuración, la operación y la escala de una base de datos relacional en Nube de AWS.

## Configuracion

- Entramos a rds de amazon 

- Damos click en crear base de datos con las siguientes configuracions

    - En en metodo seleccionamos creacion estandar

    - Para opciones del motor seleccionamos mariabd
        [rds-1](evidencias/rds-1.png)

    - En la configuracion le asignaremos un nombre a nuestra base de datos y alli mismo configuraremos un nombre se usuario y la contraseña para acceder a la base de datos
    [rds-2](evidencias/rds-2.png)

    - En conectividad seleccionamos que no se conecte a un recurso informatico 
    [rds-3](evidencias/rds-3.png)
    [rds-4](evidencias/rds-4.png)
    
    - En los grupos de seguridad selccionamos el que creamos para el rds
    [rds-5](evidencias/rds-5.png)

    - Por ultimo damos click en configuracion adicional para crear una base de datos incial 
    [rds-6](evidencias/rds-6.png)

# Instancia de moodle

Creamos una instancia de EC2, al crearla tendremos un opcion llamada configuraciones de red, alli vamos a asignar una direccion subnet.
[mood-1](evidencias/mood-1.png)

En el siguiente paso tendremos sistemas de archivos, seleccionamos EFS y seleccionamos el sistema de archivo que hemos creado anteriormente 
[mood-2](evidencias/mood-2.png)

Para probar el nsf en el moodle, vamos al nfs y seleccionamos el archivo, damos clic en conectar y nos saldra un comando, este comado lo probaremos en nuestra instancia 

[mood-3](evidencias/mood-2.png)

## conectar con la base de datos 

Seleccionamos la instancia, damos clic en acciones, redes, conectar a un base de datos rds.
[mood-4 ](evidencias/mood-4.png)

En esta configuracion  seleccionamos instancia.
[mood-5 ](evidencias/mood-5.png)
[mood-6 ](evidencias/mood-6.png)

Adicionalmente creamos la carpeta donde ira el docker de moodle y editamos los campos de database name y database user

    version: '2'
    services:
      moodle:
        image: docker.io/bitnami/moodle:4
        ports:
          - '80:8080'
        environment:
          - MOODLE_DATABASE_HOST=database-1.cz7jy9ihsp0i.us-east-1.rds.amazonaws.com
          - MOODLE_DATABASE_PORT_NUMBER=3306
          - MOODLE_DATABASE_USER=admin
          - MOODLE_DATABASE_NAME=moodle2
          # ALLOW_EMPTY_PASSWORD is recommended only for development.
          - ALLOW_EMPTY_PASSWORD=yes
        volumes:
          - 'moodle_data:/bitnami/moodle'
          - 'moodledata_data:/bitnami/moodledata'
    volumes:
      moodle_data:
        driver: local
      moodledata_data:
        driver: local



# AUTOSCALING

## crear una ami para autoscaling 

En el menú de Actions, click en Image > Create Image y configure los siguientes parámetros:

- Image name: Web Moodle  AMI

- Image description: AMI for Web Server

- Click en Create Image. Observará un mensaje de confirmación que muestra el AMI ID para la nueva AMI.

[lb-2 ](evidencias/lb-2.png)


## target group

En el menú de EC2, en la sección de Load Balancing, escoga Target Groups. Seleccione la opción de “Create target group”. 
[lb-3 ](evidencias/lb-3.png)


- Basic Configuration
Choose  a target type: Instances.
Target group name: TG-MyWebApp.
Protocol: HTTP:80
VPC: VPC-default
Protocol version: HTTP1

Click en Next.

         Registers Target

        Available instances:

        Review Target:


## Balanceador de cargas 

En el panel izquierdo, click Load Balancers.

- Click en Create Load Balancer. 
Como puede observar, se definen tres tipos diferentes de balanceadores de carga. 

- Haga click en Create en la sección de Application Load Balancer.

- En la sección de configuración básica, configure los siguientes parámetros:

        Name: ELB-MyWebApp
        Scheme: Seleccione internet-facing.
        IP address type: ipv4
        VPC: VPC-default.

[lb-4 ](evidencias/lb-4.png)


- Availability Zones: Seleccione la casilla de cada zona de disponibilidad.  Y seleccione la subred pública para ambas zonas. Recuerde que el balanceador de carga va desplegado en la subred pública.

[lb-5 ](evidencias/lb-5.png)

- En la sección de Configure Security Group, seleccione la opción de escoger un security group existente. 

[lb-6](evidencias/lb-6.png)

En la sección de Listeners, configure los siguientes parámetros:

        Load Balancer Protocol: http.
        Load Balancer Port: 80.
        Default action: seleccione el Target Group Creado: TG-MyWebApp
        En la sección de Availability Zones:
        VPC: VPC-default

[lb-7 ](evidencias/lb-7.png)


- En la sección de Configure Routing, se procede a configurar hacia donde enviar las peticiones que llegan al balanceador de cargas. Aquí vamos a crear un Target group que será usado por el servicio de autoscaling. 

        Name: TG-MyWebApp
        Click en Next: Register Targets.
        El servicio de autoscaling de manera automática registra las instancias como targets. Esto lo haremos posteriormente.
        Click en Next: Review. Verifique los parámetros configurados. 
        Click en Create.

[lb-9 ](evidencias/lb-9.png)

## launch template

En el home de la consola de administración, seleccione el servicio de EC2.

En el panel izquierdo, seleccione Launch Template.

- Click en Create launch template.
Proceda a configurar los siguientes aspectos:

        Launch configuration name: MyWebApp
        Template version description: Template for web moodle.
        Auto Scaling guidance: Active la casilla.

[lb-10](evidencias/lb-10.png)

- Launch template contents
Application and OS Images (Amazon Machine Image): En myAMIs, click en Owned by me, Web Moodle AMI

        Instance type: t2.micro
        Key pair (login)
        Vockey
Deje lo demás por defecto y de Click en “Create launch template”

[lb-11](evidencias/lb-11.png)
[lb-12](evidencias/lb-12.png)

##  grupo de autoscaling

Ahora se procederá a crear el grupo de Auto Scaling. Para esto:
Seleccione el launch configuration creado.
- Click en el menú Actions. Click en Create auto scaling group.

        Digite el nombre del auto scaling group:
        Name: MyWebApp-Auto Scaling Group
        Launch template: MyWebApp
Click en Next.

[lb-13](evidencias/lb-13.png)

- En la sección de Network configure los siguientes parámetros:

        Network: VPC-default.
        Subnet: Seleccione las dos subredes públicas (-1a y -1b) ubicadas en las dos zonas de disponibilidad.

[lb-14](evidencias/lb-15.png)

- En la sección de Configure advanced options:
Seleccione la casilla para: Attach to an existing load balancer.

        Escoja: Choose from your load balancer target groups
        Escoja el target group que se creó para la aplicación. TG-MyWebApp.
        Marque la casilla de Enable group metrics collection within CloudWatch. 

[lb-15](evidencias/lb-16.png)
Click en Next.

- En la sección de Configure Group Size 

        Desired capacity: 2
        Minimum capacity: 2
        Maximum capacity: 3

Esta configuración va a permitir escalar entre dos y tres máquinas.
En esta misma sección para scaling policies:
Seleccione target tracking scaling policy.
Scaling policy name: MyWebApp-ScalingPolicy
Metric type: Average CPU utilization.
Target Value: 60.
Click en “next”

[lb-16](evidencias/lb-16.png)
    
# otra información que considere relevante para esta actividad.

![image](https://user-images.githubusercontent.com/53051440/202277909-ade4312e-38a7-4f77-8e80-aff220262697.png)


# referencias:
### https://docs.aws.amazon.com/es_es/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.html
### https://aws.amazon.com/es/blogs/aws-spanish/despliegue-de-moodle-en-alta-disponibilidad-en-aws/
### https://docs.aws.amazon.com/efs/latest/ug/creating-using.html


#### versión README.md -> 1.0 (2022-agosto)
