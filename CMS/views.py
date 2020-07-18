from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from CMS.models import Family


@require_GET
def index(request):
    return render(request, 'index.html', locals())


@require_GET
def index2(request):
    return render(request, 'index2.html', locals())


@require_GET
def family_display(request):
    families = Family.objects.all()
    theader = Family.get_threader()
    return render(request, 'family_display.html', locals())


@require_http_methods(['POST', 'GET'])
def family_create(request):
    if request.method == 'GET':
        return render(request, 'family_create.html', locals())
    else:
        address = request.POST.get('address', None)
        illegal_situation = request.POST.get('illegal_situation', None)
        commercial_housing_situation = request.POST.get('commercial_housing_situation', None)
        rental_status = request.POST.get('rental_status', None)
        object_class = request.POST.get('object_class', None)
        vehicle_condition = request.POST.get('vehicle_condition', None)

        family = Family.objects.create()
        family.address = address
        family.illegal_situation = illegal_situation
        family.commercial_housing_situation = commercial_housing_situation
        family.rental_status = rental_status
        family.object_class = object_class
        family.vehicle_condition = vehicle_condition
        family.save()

        families = Family.objects.all()
        theader = Family.get_threader()
        return render(request, 'family_display.html', locals())
