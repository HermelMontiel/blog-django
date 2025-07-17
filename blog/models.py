from django.db import models

# Create your models here.

class Post (models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Comentario (models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.post.titulo}"


# Tipos de campos adicionales

#CharField = Texto corto con limitantes de caracteres
#TextField = Texto Largo
