# Sistemas Software Basados en Web

Repositorio para la asignatura de Sistemas Software Basados en Web para el máster de ingeniería informática de la UGR

  

### Django, React y Despliegue con Nginx 

Se ha desarrollado una aplicación sobre posiboles visitas a realizar en Granada usando tanto Django de backend como de frontend y también dispone de un api. De forma se puede usar Django en el backend y también React para el frontend de otra versión de la aplicación.  

También se ha incluido Nginx para el servicio de los directorios static y media.  

## Para iniciar la aplicación  

1.  `docker-compose build`

1.  `docker-compose run app_django python ./django_app/manage.py migrate`

1.  `docker-compose run app_django python ./django_app/manage.py collectstatic`

1.  `docker-compose run app_django python ./django_app/manage.py createsuperuser `

Es importante que el nombre que se haya dado al superusuario sea **"admin"** para que el script populate funcione correctamente

1.  `docker-compose up run app_django python ./django_app/populate.py`

Si tenemos un bot de telegram y queremos que la aplicación de django nos envíe las notificaciones a este bot, debemos crear un fichero en el directorio /django_app llamado **".env"** de la siguiente manera:

    TOKEN= {Nuestro token del bot de telegram}
    ID= {nuestro id de telegram}

Para instalar la aplicación de React debemos ejecutar el siguiente comando:

1.  `docker-compose up run app_react npm install`

1. `docker-compose up `
  
## Para acceder a las aplicaciones:

-  [http://localhost](http://localhost) para la aplicación con Django
	 -  [http://localhost/api_visitas/](http://localhost/api_visitas/) para la API Django
-  [http://localhost:3000](http://localhost:3000) para la aplicación con React