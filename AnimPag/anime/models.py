from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, verbose_name='username')
    password = models.CharField(max_length=100, null=True, verbose_name='password')
    foto = models.ImageField(upload_to='static/foto_perfil/', null=True, verbose_name='foto')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    
    def __str__(self):
        fila = "Username: " + str(self.username)
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()

class Comentario(models.Model):
    comentarios = models.CharField(max_length=100, verbose_name='comentarios')
    enviado = models.DateTimeField(auto_now_add=True, verbose_name='enviado')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='usuario')
    
    def __str__(self):
        fila = "usuario: " + str(self.usuario) + " | " + "comentarios: " + str(self.comentarios)
