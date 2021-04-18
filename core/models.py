from django.db import models
import cloudinary.models
from django.utils import timezone


# Create your models here.

class Participant(models.Model):
    """Модель участника"""
    last_name = models.CharField(max_length=100,
                                 verbose_name="Фамилия на русском")
    first_name = models.CharField(max_length=100,
                                  verbose_name="Имя на русском")
    second_name = models.CharField(max_length=100,
                                   verbose_name="Отчество", blank=True)
    email = models.EmailField(max_length=100,
                              verbose_name="Email", blank=True)
    phone = models.CharField(max_length=100,
                             verbose_name="Телефон", blank=True)
    city = models.CharField(max_length=100,
                            verbose_name="Город", blank=True)
    organization = models.CharField(max_length=100,
                                    verbose_name="Образовтательная организация", blank=True)
    nomination = models.CharField(max_length=100,
                                  verbose_name="Номинация", blank=True)
    file = models.CharField(max_length=100,
                            verbose_name="Файл", blank=True)
    brief = models.TextField(max_length=5000,
                             verbose_name="Текст письма", blank=True)
    site = models.CharField(max_length=100,
                            verbose_name="Ссылка на сайт", blank=True)
    video = models.CharField(max_length=100,
                             verbose_name="Ссылка на сайт", blank=True)


class Post(models.Model):
    """Модель новости"""
    code = models.CharField(max_length=3, help_text="Пример заполнения: <em>001</em>.",
                            verbose_name="Код новости", primary_key=True)
    image = cloudinary.models.CloudinaryField('картинка', blank=True, null=True)
    title = models.TextField(verbose_name="Заголовок новости", blank=True, null=True)
    body = models.TextField(verbose_name="Содержание новости", blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Список новостей"

    def publish(self):
        self.published_date = timezone.now()
        self.save()
