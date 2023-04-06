from django.db import models


# Create your models here.
class User(models.Model):
      nombre = models.CharField(max_length=50)
      numero = models.IntegerField(max_length=100)
      
      def __str__(self):
          return self.nombre
      
class Amigos(models.Model):
      a = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
      amigos = models.CharField( max_length=50)
      
      def __str__(self):
            return self.amigos


class TablaChats(models.Model):
      a = models.ForeignKey(Amigos, on_delete=models.CASCADE, default=False) 
      mensaje = models.CharField(max_length=100)
      
    
class Registros(models.Model):
      nombre = models.CharField(max_length=50)
      
      def __str__(self):
          return self.nombre
      