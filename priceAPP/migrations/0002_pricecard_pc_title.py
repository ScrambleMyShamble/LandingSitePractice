# Generated by Django 4.0.2 on 2022-02-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricecard',
            name='pc_title',
            field=models.CharField(default='-', max_length=50, verbose_name='Имя'),
        ),
    ]