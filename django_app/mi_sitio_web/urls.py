"""mi_sitio_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from visitas_granada import views
from rest_framework import routers

router_visita = routers.DefaultRouter()
router_visita.register(r'visitas', views.VisitaViewSet)

router_commentario = routers.DefaultRouter()
router_commentario.register(r'comentarios', views.ComentarioViewSet)


urlpatterns = [        
    path('', views.index, name='index'),
    path('visita/<int:visita_id>/', views.detalle_visita, name='detalle'),
    path('add_visita/', views.add_visita, name='add_visita'),
    path('edit_visita/<int:visita_id>/', views.edit_visita, name='edit_visita'),
    path('delete_visit/<int:visita_id>', views.delete_visita, name='delete_visita'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api_visitas/', include(router_visita.urls)),
    path('api_visitas/', include(router_commentario.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api_visitas/likes/<int:visita_id>/', views.get_likes, name='likes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
