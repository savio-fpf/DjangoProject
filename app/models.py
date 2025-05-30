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


class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} | {self.description}'


class Publisher(models.Model):
    livro = models.CharField(max_length=50)
    ano = models.IntegerField()
    description = models.TextField()
    id_autor = models.ForeignKey(Author, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.livro} | {self.ano} | {self.description} | {self.id_autor}'