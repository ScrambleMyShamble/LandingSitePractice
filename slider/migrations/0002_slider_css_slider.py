# Generated by Django 4.0.2 on 2022-02-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='css_slider',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS-класс'),
        ),
    ]
