# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from visitas_granada.models import Visita, Comentario
from django.template import loader
import os

# Leave the rest of the views (detail, results, vote) unchanged
def index(request):
    lista_visitas = Visita.objects.order_by('-nombre')[:5]
    num_comentarios = Comentario.objects.all().count()
    num_visitas = Visita.objects.all().count()
    template = loader.get_template('visitas_granada/index.html')
    context = {
        'lista_visitas': lista_visitas, 
        'num_comentarios': num_comentarios,
        'num_visitas' : num_visitas,
    }
    return HttpResponse(template.render(context, request) )


def detalle_visita(request, visita_id):
    lista_visitas = Visita.objects.order_by('-nombre')[:5]
    num_comentarios = Comentario.objects.all().count()
    num_visitas = Visita.objects.all().count()
    mi_visita = Visita.objects.get(id=visita_id)
    comentarios = Comentario.objects.filter(visita=mi_visita)    
    template = loader.get_template('visitas_granada/detalle_visita.html')
    context = {
        'lista_visitas': lista_visitas,
        'mi_visita': mi_visita, 
        'comentarios': comentarios,
        'num_comentarios': num_comentarios,
        'num_visitas': num_visitas,
    }
    return HttpResponse(template.render(context, request))



def listado(request):
    lista_visitas = Visita.objects.order_by('-nombre')[:5]
    template = loader.get_template('visitas_granada/listado.html')
    context = {
        'lista_visitas': lista_visitas,
    }
    return HttpResponse(template.render(context, request))




# Leave the rest of the views (detail, results, vote) unchanged
