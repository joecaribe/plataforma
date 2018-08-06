from django.db import models
from login.models import CustomUser

# Create your models here.
class Course(models.Model):
	id = models.AutoField( primary_key = True)
	professor = models.ForeignKey( CustomUser, on_delete = models.CASCADE )
	name = models.CharField( max_length = 100 , default = "sem_nome")
	
	def __str__(self):
		return self.name