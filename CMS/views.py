from django.shortcuts import render
from django.views.decorators.http import require_GET

from CMS.models import Family


@require_GET
def index(request):
    return render(request, 'index.html', locals())


@require_GET
def index2(request):
    return render(request, 'index2.html', locals())


@require_GET
def family_display(request):
    familys = Family.objects.all()
    theader = Family.get_threader()
    return render(request, 'family_display.html', locals())
