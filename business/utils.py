from .models import Business
from django.db.models import Q


def searchBusiness(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    address = Business.objects.filter(address__icontains=search_query)

    business = Business.objects.distinct().filter(
        Q(business_name__icontains=search_query) |
        Q(address__in=address)
    )
    return business, search_query