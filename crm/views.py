from django.shortcuts import render
from slider.models import Slider


def first_page(request):
    slider_list = Slider.objects.all()
    return render(request, './index.html', {'slider_list':slider_list})
