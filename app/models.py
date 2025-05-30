from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    categoria = models.CharField(max_length=32)

    def __str__(self):
        return self.categoria



class Author(model.Model):
    id = models.AutoField(primary_key=id)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return (f'{self.name} | {self.description}')
    
class Publisher(model.Model):
    livro = model.models.CharField(max_length=50)
    ano = models.DateField()
    description = models.TextField()
    id_autor = models.ForeignKey(Author.id)

    def __str__(self):
        return (f'{self.livro} | {self.ano} | {self.description} |  {self.id_autor}')