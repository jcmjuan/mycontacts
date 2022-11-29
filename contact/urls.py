from django.urls import path
from .import views


urlpatterns = [
    path('',views.Home.as_view(), name = 'home'),
    path('Contact/Detail/<int:pk>/',views.ContactDetail.as_view(), name = 'contactdetail'),
    path('contact/search/',views.search, name = 'search'),
    path('Create/Contact/',views.CreateContact.as_view(), name = 'createcontact'),
    path('Contact/Update/<int:pk>/',views.ContactUpdate.as_view(), name = 'contactupdate'),
    path('Contact/Delete/<int:pk>/',views.ContactDelete.as_view(), name = 'contactDelete'),
    path('Create/Account/',views.CreateAccount.as_view(), name = 'signup'),
]