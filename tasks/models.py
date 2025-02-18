from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    # Es un método especial de Python que define cómo se presenta un objeto de la clase 'Task' como cadena de texto
    def __str__(self):
        return self.title