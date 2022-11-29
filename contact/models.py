from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactList(models.Model):
    manager = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    nome = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=50,blank=True,unique=True)
    telefone = models.CharField(max_length=10,blank=False,unique=True)
    genero = models.CharField(max_length=6,default='select',choices=(('select','Selecionar'),('homem','Homem'),('mulher','Mulher')),blank=False)
    imagem = models.ImageField(upload_to='images',blank=True)
    categoria = models.CharField(max_length=15,blank=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
