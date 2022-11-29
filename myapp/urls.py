
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('contact.urls')),
    path('',include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

# custome admin controle panale
admin.site.site_header = 'Bem-vindo ao MyContacts'
admin.site.site_title = 'Contatos'
admin.site.index_title = 'Projeto Contatos'
