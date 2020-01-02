from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,bedroom_choices, state_choices


def index(request):
    listings_data = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings_data,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    return render(request,'pages/index.html', context)
    # return HttpResponse('<h1>Hello World</h1>')

def about(request):
    realtors_data = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    print(realtors_data)

    for data in realtors_data:
        data.phone_formatted = '(' + data.phone[:3] + ') ' + data.phone[3:6] + '-' + data.phone[6:]

    context = {
        'realtors': realtors_data,
        'mvp_realtors': mvp_realtors
    }

    return render(request,'pages/about.html', context)

