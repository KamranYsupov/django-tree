from django.db import models

from django.db import models


class Menu(models.Model):
    name = models.CharField('Название меню', max_length=50, unique=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuPoint(models.Model):
    name = models.CharField('Название пункта меню', max_length=50, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
