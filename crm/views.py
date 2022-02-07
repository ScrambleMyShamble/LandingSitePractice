from django.shortcuts import render
from slider.models import Slider
from priceAPP.models import PriceCard, PriceTable


def first_page(request):
    slider_list = Slider.objects.all()
    price_card_1 = PriceCard.objects.get(pk=1)
    price_card_2 = PriceCard.objects.get(pk=2)
    price_card_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    dict_objects = {'slider_list': slider_list,
                    'price_table': price_table,
                    'price_card_1': price_card_1,
                    'price_card_2': price_card_2,
                    'price_card_3': price_card_3}
    return render(request, './index.html', dict_objects)
