#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_DAI.settings')

import django
django.setup()

from app.models import Bar, Tapa


def populate():
    bar1= add_bar('Plaza','España Orce Plaza Nueva nº 4')

    add_tapa(bar=bar1,nombre="Boquerones",descripcion="Boquerones fritos ricos ricos ")

    add_tapa(bar=bar1,nombre="Carne con tomate",descripcion="Rica carne con tomate frito")

    add_tapa(bar=bar1,nombre="Patatas bravas",descripcion="Patatas bravas muy ricas")

    add_tapa(bar=bar1,nombre="Jamón",descripcion="Jamón muy rico")
    #---------------------------------------------------------------------------------------------------------
    bar2= add_bar('Restaurante la Mimbrera','España Orce calle Chorreador nº 6')

    add_tapa(bar=bar2,nombre="Boquerones",descripcion="Boquerones fritos ricos ricos ")

    add_tapa(bar=bar2,nombre="Carne con tomate",descripcion="Rica carne con tomate frito")

    add_tapa(bar=bar2,nombre="Patatas bravas",descripcion="Patatas bravas muy ricas")

    add_tapa(bar=bar2,nombre="Jamón",descripcion="Jamón muy rico")
    #---------------------------------------------------------------------------------------------------------
    bar3= add_bar('Bar el Salero','España Orce Fernando villalobos nº 8')

    add_tapa(bar=bar3,nombre="Boquerones",descripcion="Boquerones fritos ricos ricos ")

    add_tapa(bar=bar3,nombre="Carne con tomate",descripcion="Rica carne con tomate frito")

    add_tapa(bar=bar3,nombre="Patatas bravas",descripcion="Patatas bravas muy ricas")

    add_tapa(bar=bar3,nombre="Jamón",descripcion="Jamón muy rico")
    #---------------------------------------------------------------------------------------------------------
    bar4= add_bar('La Bodeguilla','España Orce calle Angel nº 2 ')

    add_tapa(bar=bar4,nombre="Boquerones",descripcion="Boquerones fritos ricos ricos ")


    #---------------------------------------------------------------------------------------------------------
    bar5= add_bar('Bar Alcazaba','España Orce Fernando villalobos nº 32')

    add_tapa(bar=bar5,nombre="Boquerones",descripcion="Boquerones fritos ricos ricos ")

    add_tapa(bar=bar5,nombre="Carne con tomate",descripcion="Rica carne con tomate frito")


    #---------------------------------------------------------------------------------------------------------
    bar6= add_bar('hotel la Morata','España Orce Avenida los caños nº 1')

    add_tapa(bar=bar6,nombre="Boquerones",descripcion="Boquerones fritos ricos ricos ")

    add_tapa(bar=bar6,nombre="Carne con tomate",descripcion="Rica carne con tomate frito")





    #---------------------------------------------------------------------------------------------------------
    # Print out what we have added to the user.
    for b in Bar.objects.all():
        for t in Tapa.objects.filter(bar=b):
            print "- {0} - {1}".format(str(b), str(t))

def add_tapa(bar, nombre, descripcion, votos=0):
    tapa = Tapa.objects.get_or_create(bar=bar, nombre=nombre)[0]
    tapa.votos=votos
    tapa.descripcion=descripcion
    tapa.save()
    return tapa

def add_bar(nombre, direccion, visitas=0):
    bar = Bar.objects.get_or_create(nombre=nombre)[0]
    bar.direccion= direccion
    bar.visitas=visitas
    bar.save()
    return bar

# Start execution here!
if __name__ == '__main__':
    print "Starting App population script..."
    populate()