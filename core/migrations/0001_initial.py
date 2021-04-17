# Generated by Django 3.0.8 on 2021-04-17 19:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия на русском')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('second_name', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('code', models.CharField(help_text='Пример заполнения: <em>001</em>.', max_length=3, primary_key=True, serialize=False, verbose_name='Код новости')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='картинка')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Список новостей',
            },
        ),
    ]