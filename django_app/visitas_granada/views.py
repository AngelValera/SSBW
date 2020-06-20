# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from visitas_granada.models import Visita, Comentario, VisitaForm
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import viewsets, permissions
from visitas_granada.serializers import ComentarioSerializer, VisitaSerializer, LikesSerializer
from rest_framework.parsers import JSONParser
from visitas_granada.permisions import IsOwnerOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from decouple import config
import os
import requests
import json
import logging
import datetime
logger = logging.getLogger(__name__)

# Leave the rest of the views (detail, results, vote) unchanged
def index(request):
    lista_visitas = Visita.objects.order_by('-likes')
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
    lista_visitas = Visita.objects.order_by('nombre')
    num_comentarios = Comentario.objects.all().count()
    num_visitas = Visita.objects.all().count()
    try:
        mi_visita = Visita.objects.get(id=visita_id)
    except Visita.DoesNotExist:
        msg = "Error al obtener el detalle de una visita: La visita con id " + visita_id + " no existe."
        logger.error(msg)
        notify_bot('error', msg)
        return HttpResponse(status=404)
    comentarios = Comentario.objects.filter(visita=mi_visita) 
    lugar_buscar = mi_visita.nombre.replace(" ", "+") + "+Granada"
    ubi = 'https://nominatim.openstreetmap.org/search?q={}&format=json'.format(lugar_buscar)
    result = requests.get(ubi)
    logger.warning(result.text)    
    data = json.loads(result.text)
    if data:
        lat = data[0]['lat']
        lon = data[0]['lon']
    else:
        logger.warning("Visita no ubicada, ubicamos la visita en Granada")
        lat = '37.183054'
        lon = '-3.6021928'
    template = loader.get_template('visitas_granada/detalle_visita.html')
    context = {        
        'lista_visitas': lista_visitas,
        'mi_visita': mi_visita, 
        'comentarios': comentarios,
        'num_comentarios': num_comentarios,
        'num_visitas': num_visitas,
        'lat': lat,
        'lon': lon,
    }    
    return HttpResponse(template.render(context, request))


@login_required
@staff_member_required
def add_visita(request): 
    lista_visitas = Visita.objects.order_by('nombre')
    num_comentarios = Comentario.objects.all().count()
    num_visitas = Visita.objects.all().count()
    form = VisitaForm()
    if request.method == 'POST':  # de vuelta con los datos
        form = VisitaForm(request.POST, request.FILES)  # bound the form
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            msg = "Nueva visita creada correctamente"
            messages.success(request, msg)
            notify_bot('info',msg)            
            return redirect('index')    
    template = loader.get_template('visitas_granada/add_visita.html')
    context = {
        'form': form,
        'num_comentarios': num_comentarios,
        'num_visitas': num_visitas,
        'lista_visitas': lista_visitas,
    }
    return HttpResponse(template.render(context, request))


@login_required
@staff_member_required
def edit_visita(request, visita_id):
    lista_visitas = Visita.objects.order_by('nombre')
    num_comentarios = Comentario.objects.all().count()
    num_visitas = Visita.objects.all().count()    
    try:
        visit = Visita.objects.get(pk=visita_id)
        name = visit.nombre
    except Visita.DoesNotExist:
        msg = "Error al editar una visita: La visita con id " + visita_id + " no existe."
        logger.error(msg)
        notify_bot('error', msg)
        return HttpResponse(status=404)    
    form = VisitaForm(instance=visit)    
    if request.method == 'POST':  # de vuelta con los datos
        form = VisitaForm(request.POST, request.FILES,
                          initial=visit.__dict__, instance=visit)  # bound the form
        if form.is_valid():
            if form.has_changed():                
                form.save()
            msg = "Visita "+name+" ha sido modificada correctamente"
            messages.success(request, msg )
            notify_bot('info',msg)                       
            return redirect('index')
    template = loader.get_template('visitas_granada/edit_visita.html')
    context = {
        'form': form,
        'visit': visit,
        'num_comentarios': num_comentarios,
        'num_visitas': num_visitas,
        'lista_visitas': lista_visitas,
    }
    return HttpResponse(template.render(context, request))


@login_required
@staff_member_required
def delete_visita(request, visita_id):
    visit = Visita.objects.get(pk=visita_id)
    name = visit.nombre
    visit.delete()
    msg = "Visita "+name+" ha sido eliminada correctamente"
    messages.success(request, msg)
    notify_bot('info',msg)    
    return redirect('index')


class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all().order_by('id')
    serializer_class = VisitaSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('id')
    serializer_class = ComentarioSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

@csrf_exempt
def get_likes(request, visita_id):
    try:
        visita = Visita.objects.get(id=visita_id)
    except Visita.DoesNotExist:        
        msg = "Error al obtener los likes: La visita con id " + visita_id +" no existe."
        logger.error(msg)
        notify_bot('error', msg)
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = LikesSerializer(visita)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LikesSerializer(visita, data=data)
        if serializer.is_valid():
            serializer.save()
            msg = "Likes de la visita "+visita.nombre+' actualizado.'
            notify_bot('info',msg)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


def notify_bot(level, notify):
    telegram_token = config('TOKEN')
    telegram_chat_id = config('ID')
    dt = datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')   
    msg = "<i>{datetime}</i><pre>\n{notify}</pre>".format(notify=notify, datetime=dt)    
    # Almacenamos también el mensaje en el fichero de log
    if level == 'error':
        logger.error(notify)
    elif level == 'warning':
        logger.warning(notify)
    else:
        logger.info(notify)

    if telegram_token != "None" and telegram_chat_id != "None":
        payload = {
            'chat_id': telegram_chat_id,
            'text': msg,
            'parse_mode': 'HTML'
        }
        result = requests.post("https://api.telegram.org/bot{token}/sendMessage".format(
            token=telegram_token),
            data=payload).content
