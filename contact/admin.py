from django.contrib import admin
from .models import ContactList
from django.contrib.auth.models import Group

class ContactManage(admin.ModelAdmin):
    list_display = ('id','nome','email','telefone','categoria','manager')
    list_editable = ('telefone','categoria')
    list_display_links = ('id','nome')
    search_fields = ('nome','email','telefone','categoria')
    list_filter = ('genero','datetime')
    list_per_page = 10
    

# Register your models here.
admin.site.register(ContactList,ContactManage)


admin.site.unregister(Group)

