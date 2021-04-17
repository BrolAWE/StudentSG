from django.db import models
import cloudinary.models


# Create your models here.

class Participant(models.Model):
    """Модель участника"""
    last_name = models.CharField(max_length=100,
                                 verbose_name="Фамилия на русском")
    first_name = models.CharField(max_length=100,
                                  verbose_name="Имя на русском")
    second_name = models.CharField(max_length=100,
                                   verbose_name="Отчество", blank=True)


class Post(models.Model):
    """Модель новости"""
    code = models.CharField(max_length=3, help_text="Пример заполнения: <em>001</em>.",
                            verbose_name="Код новости", primary_key=True)
    image = cloudinary.models.CloudinaryField('картинка', blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Список новостей"

    def publish(self):
        self.published_date = timezone.now()
        self.save()
