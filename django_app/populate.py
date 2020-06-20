
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mi_sitio_web.settings')

import django
django.setup()

from django.contrib.auth.models import User
from visitas_granada.models import Visita, Comentario


def populate():	
	Visita1 = add_Visita(nombre='Catedral', 
                      descripcion='La santa iglesia catedral metropolitana de la encarnación de granada es un templo católico de la ciudad española de granada, sede de la archidiócesis de la ciudad.', likes=1)
	add_comentario(visita=Visita1, texto="Una catedral muy bonita")
	add_comentario(visita=Visita1, texto="No me parece para tanto")
	add_comentario(visita=Visita1, texto="La catedral más bonita que he visto")
	add_comentario(visita=Visita1, texto="No me gusyan mucho las iglesias pero esta es especialmente bonita!!!")

	Visita2 = add_Visita(nombre='Alhambra', 
                      descripcion='Descubre las maravillas del monumento más visitado de españa con este tour guiado en español por los palacios nazaríes de la alhambra y los jardines de el generalife.', likes=13)
	add_comentario(visita=Visita2, texto="Es preciosa.")
	add_comentario(visita=Visita2, texto="Solo he visto parte de ella y me parece una pasada.")

	Visita3 = add_Visita(nombre='Parque de las Ciencias',
	                     descripcion='El parque de las ciencias de andalucía-granada es el primer museo interactivo de ciencia de andalucía.', likes=2)
	add_comentario(visita=Visita3, texto="Es muy interesante.")
	add_comentario(visita=Visita3, texto="El biodomo es lo mejor")
	add_comentario(visita=Visita3, texto="La exposición que hicieron de rapaces estuvo muy interesante.")
	add_comentario(visita=Visita3, texto="Me encanta ir con mi familia y amigos siempre que puedo hay muchas cosas increíbles!")

	Visita4 = add_Visita(nombre='Hammam Al Ándalus',
	                     descripcion='Relájate a los pies de la alhambra en estos baños árabes construidos sobre las ruinas de un antiguo hammam del siglo xvi', likes=3)
	add_comentario(visita=Visita4, texto="Todo genial. Muy relajante y el personal muy atento.")
	add_comentario(visita=Visita4, texto="Una experiencia inolvidable! Hasta el mínimo detalle.")
	add_comentario(visita=Visita4, texto="Un buen lugar para desconectar al lado del Paseo de los Tristes. Las instalaciones están muy bien, además, tuvimos suerte que a pesar de ser fin de semana, no estaba masificado. Recomendable elegir la opción del masaje, para salir más relajado. Una sugerencia para mejorar el servicio, podría ser que fuera obligatorio el uso de chancletas para acceder a las piscinas.")
	add_comentario(visita=Visita4, texto="No me ha gustado hacía mucha calor")

	Visita5 = add_Visita(nombre='Pradollano Sierra Nevada',
	                     descripcion='Esquía por las pistas que te ofrece sierra nevada y disfruta de los restaurantes locales.', likes=2)
	add_comentario(visita=Visita5, texto="El pueblo es super bonito y tiene muchas cafeterias y zonas de ocio, además la gente es muy amable!!!Volvería sin dudarlo!!")

	Visita6 = add_Visita(nombre='Pico del Veleta',
	                     descripcion='Disfruta de este magnifico paseo por la sierra granadina mientras aprendes sobre la fauna y la flora que te rodean.', likes=1)
	add_comentario(visita=Visita6, texto="Las vistas son increibles!!!! me encantaría volver otra vez :)")

	# Print out what we have added to the user.
	for v in Visita.objects.all():
		for c in Comentario.objects.filter(visita=v):
			print ("- {0} - {1}".format(str(v), str(c)))


def add_comentario(visita, texto):
    comentario = Comentario.objects.get_or_create(
    	visita=visita, texto=texto)[0]
    comentario.texto = texto
    comentario.save()
    return comentario

def add_Visita(nombre, descripcion, likes ):	
	user = User.objects.get(username="admin")	
	visita = Visita.objects.get_or_create(nombre=nombre, owner=user)[0]
	visita.descripcion = descripcion
	visita.likes = likes	
	visita.save()
	return visita

# Start execution here!
if __name__ == "__main__":
	print("Starting App population script...")		
	populate()
