"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
#foi feito o importe do include acima
#Imports abaixo para as imagens - Faça também a instalação do Pillow - pip install Pillow
from django.conf import settings
from django.conf.urls.static import static
#tinymce
from tinymce import urls as tinymce_urls

#import das views, função index e contato criadas no core/views
from core.views import index, contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('tinymce/', include(tinymce_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Configuração acima para cadastro de imagens -> + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)