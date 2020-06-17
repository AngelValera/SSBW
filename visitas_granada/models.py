# -*- coding: utf-8 -*-
from django.db import models

from sorl.thumbnail import ImageField

# Create your models here.
class Visita(models.Model):	
	nombre      = models.CharField(max_length=155, unique=True)
	descripcion = models.CharField(max_length=1000)
	likes       = models.IntegerField(default=0)	
	foto = ImageField(upload_to='fotos', blank=True)
	
	def save(self, *args, **kwargs):    		
		super(Visita, self).save(*args, **kwargs)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nombre

class Comentario(models.Model):
	visita      = models.ForeignKey(Visita, on_delete=models.CASCADE)
	texto       = models.CharField(max_length=500)
	
	def save(self, *args, **kwargs):    		
		super(Comentario, self).save(*args, **kwargs)


	def __str__(self):	  #For Python 2, use __str__ on Python 3
		return self.texto
