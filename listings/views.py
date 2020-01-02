from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger

# from .models import Listing , objects
from .models import Listing
from listings.choices import price_choices,bedroom_choices, state_choices

def index(request):
    listings_data = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings_data, 6) # Show 'n' Listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing_data = get_object_or_404(Listing,pk=listing_id)

    context = {
        'listing': listing_data
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_data = Listing.objects.order_by('-list_date')
    
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_data = queryset_data.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_data = queryset_data.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_data = queryset_data.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_data = queryset_data.filter(bedrooms__lte=bedrooms) 

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_data = queryset_data.filter(price__lte=price) 

    context = {
        'listings': queryset_data,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'values':  request.GET
    }
    return render(request, 'listings/search.html', context)
