from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from CMS.models import Family, Person, HandleAffairsRecord


@require_GET
def index(request):
    return render(request, 'index.html', locals())


@require_GET
def index2(request):
    return render(request, 'index2.html', locals())


@require_GET
def family_display(request):
    families = Family.objects.all()
    family_thead = Family.get_thread()
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
        family_thead = Family.get_thread()
        return render(request, 'family_display.html', locals())


@require_http_methods(['POST', 'GET'])
def family_details(request):
    if request.method == 'GET':
        return render(request, 'family_details.html', locals())
    else:
        address = request.POST.get('address', None)
        family = Family.objects.get(address=address)
        people_thead = Person.get_thread()
        family_member = Person.objects.filter(family__address=address)
        affairs = HandleAffairsRecord.objects.filter(person__family__address=address)
        affairs_thead = HandleAffairsRecord.get_thread()
        return render(request, 'family_details.html', locals())


@require_http_methods(['POST', 'GET'])
def family_member_create(request):
    if request.method == 'GET':
        address = request.GET.get('address', None)
        family = Family.objects.get(address=address)
        return render(request, 'family_member_create.html', locals())
    else:
        address = request.POST.get('address', None)

        appellation = request.POST.get('appellation', None)
        name = request.POST.get('name', None)
        domicile = request.POST.get('domicile', None)
        work_units = request.POST.get('work_units', None)
        id_number = request.POST.get('id_number', None)
        income = request.POST.get('income', None)
        social_security = request.POST.get('social_security', None)
        political_landscape = request.POST.get('political_landscape', None)
        health = request.POST.get('health', None)
        phone_number = request.POST.get('phone_number', None)

        person = Person.objects.create(family=Family.objects.get(address=address))
        person.appellation = appellation
        person.name = name
        person.domicile = domicile
        person.work_units = work_units
        person.id_number = id_number
        person.income = income
        person.social_security = social_security
        person.political_landscape = political_landscape
        person.health = health
        person.phone_number = phone_number
        person.save()

        family = Family.objects.get(address=address)
        people_thead = Person.get_thread()
        family_member = Person.objects.filter(family__address=address)
        affairs = HandleAffairsRecord.objects.filter(person__family__address=address)
        affairs_thead = HandleAffairsRecord.get_thread()
        return render(request, 'family_details.html', locals())


@require_GET
def person_display(request):
    people = Person.objects.all()
    people_simple_thead = Person.get_simple_thead()
    return render(request, 'person_display.html', locals())


@require_http_methods(['POST', 'GET'])
def affair_create(request):
    if request.method == 'GET':
        address = request.GET.get('address', None)
        family_member = Person.objects.filter(family__address=address)
        return render(request, 'affair_create.html', locals())
    else:
        person = request.POST.get('person', None)
        event = request.POST.get('event', None)
        agent = request.POST.get('agent', None)

        print("person:", person)
        print("event:", event)
        print("agent:", agent)
        affair = HandleAffairsRecord.objects.create(
            person=Person.objects.get(name=person),
            event=event,
            agent=agent
        )
        affair.save()

        address = Person.objects.get(name=person).family
        family = Family.objects.get(address=address)
        people_thead = Person.get_thread()
        family_member = Person.objects.filter(family__address=address)
        affairs = HandleAffairsRecord.objects.filter(person__family__address=address)
        affairs_thead = HandleAffairsRecord.get_thread()
        return render(request, 'family_details.html', locals())


@require_GET
def affairs_display(request):
    affairs = HandleAffairsRecord.objects.all()
    affairs_thead = HandleAffairsRecord.get_thread()
    return render(request, 'affairs_display.html', locals())
