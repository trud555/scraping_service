from django.db import models

from scraping.utils import cyr_to_lat


class City(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название города', unique = True)
    slug = models.CharField(max_length = 50, blank = True, verbose_name = 'Слаг города', unique = True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = cyr_to_lat(str(self.name))
            super().save(*args, **kwargs)

class Language(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Язык програмирования', unique = True)
    slug = models.CharField(max_length = 50, blank = True, verbose_name = 'Слаг языка програмирования', unique = True)

    class Meta:
        verbose_name = 'Язык програмирования'
        verbose_name_plural = 'Языки програмирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = cyr_to_lat(str(self.name))
            super().save(*args,**kwargs)

class Vacancy(models.Model):
    url = models.URLField(unique = True, verbose_name = 'Ссылка')
    title = models.CharField(max_length = 250, verbose_name = 'Заголовок')
    company = models.CharField(max_length = 250, verbose_name = 'Компания')
    description = models.TextField(verbose_name ='Описание')
    city = models.ForeignKey('City', on_delete = models.CASCADE, verbose_name = 'Город')
    language = models.ForeignKey('Language', on_delete = models.CASCADE, verbose_name = 'Язык програмирования')
    datestamp = models.DateField(auto_now_add = True, verbose_name = 'Дата')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title