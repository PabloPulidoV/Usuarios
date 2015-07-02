from django.db import models

class Usuarios(models.Model):
	nombre = models.CharField(max_length = 40)
	codigo = models.CharField(max_length = 40)
	edad =  models.CharField(max_length = 40)
	contrasena  = models.CharField(max_length = 40)
	correo = models.CharField(max_length = 40)
	paginaweb = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre