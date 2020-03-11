from django.db import models

# Create your models here.
class Visita(models.Model):	
	nombre      = models.CharField(max_length=150, primary_key=True, unique=True)
	descripcion = models.CharField(max_length=1000)
	likes       = models.IntegerField(default=0)
	foto		= models.FileField(upload_to='fotos', blank=True)

class Comentario(models.Model):
	visita      = models.ForeignKey(Visita, on_delete=models.CASCADE)
	texto       = models.CharField(max_length=500)
