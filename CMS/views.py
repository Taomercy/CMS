from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    return render(request, 'index.html', locals())


@require_GET
def index2(request):
    return render(request, 'index2.html', locals())

