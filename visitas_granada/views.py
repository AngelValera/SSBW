# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from visitas_granada.models import Visita, Comentario
from django.template import loader

# Leave the rest of the views (detail, results, vote) unchanged
def index(request):
    lista_visitas = Visita.objects.order_by('-nombre')[:5]

    template = loader.get_template('visitas_granada/index.html')
    context = {
        'lista_visitas': lista_visitas,       
    }

    return HttpResponse(template.render(context, request) )


def listado(request):
    lista_visitas = Visita.objects.order_by('-nombre')[:5]

    template = loader.get_template('visitas_granada/listado.html')
    context = {
        'lista_visitas': lista_visitas,
    }

    return HttpResponse(template.render(context, request))




# Leave the rest of the views (detail, results, vote) unchanged
