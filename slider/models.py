from django.db import models


# Create your models here.

class Slider(models.Model):
    slider_img = models.ImageField(upload_to='slidering/')
    slider_title = models.CharField(max_length=200, verbose_name='Заголовок')
    slider_text = models.CharField(max_length=200, verbose_name='Текст')
    css_slider = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS-класс')

    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
