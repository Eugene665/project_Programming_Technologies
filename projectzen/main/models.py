from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField('Название проекта', max_length=100)
    description = models.TextField('Описание проекта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
