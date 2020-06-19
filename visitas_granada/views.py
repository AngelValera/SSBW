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
import os
import json
import logging
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
            messages.success(request, "Nueva visita creada correctamente")
            logger.info("Nueva visita creada correctamente")
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
    visit = Visita.objects.get(pk=visita_id)  
    name = visit.nombre
    form = VisitaForm(instance=visit)    
    if request.method == 'POST':  # de vuelta con los datos
        form = VisitaForm(request.POST, request.FILES,
                          initial=visit.__dict__, instance=visit)  # bound the form
        if form.is_valid():
            if form.has_changed():                
                form.save()
            msg = "Visita "+name+" ha sido modificada correctamente"
            messages.success(request, msg )
            logger.info("Visita con id %s  ha sido modificada correctamente", visita_id)
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
    logger.info("Visita con id %s  ha sido eliminada correctamente", visita_id)
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
        logger.error("Error al obtener los likes de una visita que no existe: ")
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = LikesSerializer(visita)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LikesSerializer(visita, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
