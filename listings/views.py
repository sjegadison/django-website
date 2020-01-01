from django.shortcuts import render
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger

# from .models import Listing , objects
from .models import Listing

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
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
