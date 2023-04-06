from django.db import models

# Create your models here.
class User(models.Model):
      nombre = models.CharField(max_length=50)
      numero = models.IntegerField(max_length=100)
      
      def __str__(self):
          return self.nombre
      
    
class Registros(models.Model):
      nombre = models.CharField(max_length=50)
      
      def __str__(self):
          return self.nombre



class Amigos(models.Model):
      models.ForeignKey(User, on_delete=models.CASCADE)
      amigos = models.CharField( max_length=50)