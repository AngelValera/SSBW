
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mi_sitio_web.settings')

import django
django.setup()

from visitas_granada.models import Visita, Comentario


def populate():
	Visita1 = add_Visita(nombre='Catedral', 
						 descripcion='Catedral de Granada', likes=0)
	add_comentario(visita=Visita1, texto="Una catedral muy bonita")
	add_comentario(visita=Visita1, texto="No me parece para tanto")
	add_comentario(visita=Visita1, texto="La catedral más bonita que e visto")

	Visita2 = add_Visita(nombre='Alhambra', 
						 descripcion='Alhambra de Granada', likes=0)
	add_comentario(visita=Visita2, texto="Es preciosa.")
	add_comentario(visita=Visita2, texto="Solo he visto parte de ella y me parece una pasada.")

	Visita3 = add_Visita(nombre='Parque de las Ciencias',
	                     descripcion='Parque de las Ciencias de Granada', likes=0)
	add_comentario(visita=Visita3, texto="Es muy interesante.")
	add_comentario(visita=Visita3, texto="El biodomo es lo mejor")
	add_comentario(visita=Visita3, texto="La exposición que hicieron de rapaces estuvo muy interesante.")

	Visita4 = add_Visita(nombre='Hammam Al Ándalus, un baño en la historia',
	                     descripcion='Relájate a los pies de la Alhambra en estos baños árabes construidos sobre las ruinas de un antiguo Hammam del siglo XVI', likes=0)
	add_comentario(visita=Visita4, texto="Todo genial. Muy relajante y el personal muy atento.")
	add_comentario(visita=Visita4, texto="Una experiencia inolvidable! Hasta el mínimo detalle.")
	add_comentario(visita=Visita4, texto="Un buen lugar para desconectar al lado del Paseo de los Tristes. Las instalaciones están muy bien, además, tuvimos suerte que a pesar de ser fin de semana, no estaba masificado. Recomendable elegir la opción del masaje, para salir más relajado. Una sugerencia para mejorar el servicio, podría ser que fuera obligatorio el uso de chancletas para acceder a las piscinas.")
	add_comentario(visita=Visita4, texto="No me ha gustado hací amucha calor")
	# Print out what we have added to the user.
	for v in Visita.objects.all():
		for c in Comentario.objects.filter(visita=v):
			print ("- {0} - {1}".format(str(v), str(c)))


def add_comentario(visita, texto):
    comentario = Comentario.objects.get_or_create(visita=visita)[0]
    comentario.texto = texto
    comentario.save()
    return comentario

def add_Visita(nombre, descripcion, likes):
	visita = Visita.objects.get_or_create(nombre=nombre)[0]
	visita.descripcion = descripcion
	visita.likes = likes
	visita.save()
	return visita

# Start execution here!
if __name__ == "__main__":
	print("Starting App population script...")
	populate()
