from django.shortcuts import render,redirect
from .models import ContactList
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm

# for LoginRequired those are used 
# LoginRequiredMixin used for class based 
from django.contrib.auth.mixins import LoginRequiredMixin
# login_required used for function base 
from django.contrib.auth.decorators import login_required

# Q used for filter() multipole valude search()
from django.db.models import Q

from django.urls import reverse_lazy



# Create your views here.
class Home(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = ContactList
    context_object_name = 'contact'
    
    def get_queryset(self):
        contact = super().get_queryset()
        return contact.filter(manager=self.request.user)

class ContactDetail(LoginRequiredMixin,DetailView):
    template_name = 'detail.html'
    model = ContactList
    context_object_name = 'contact'

@login_required
def search(request):
    if request.GET:
        search_query = request.GET['search_query']
        search_result = ContactList.objects.filter(
            Q(nome__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(telefone__iexact=search_query) |
            Q(genero__icontains=search_query) |
            Q(categoria__icontains=search_query)
        )
        context = {
            'search_query':search_query,
            'contact':search_result.filter(manager=request.user)
        }
        return render(request,'search.html',context)
    else:
        return redirect('/')

class CreateContact(LoginRequiredMixin,CreateView):
    template_name = 'createcontact.html'
    model = ContactList
    fields = ['nome','email','telefone','genero','categoria','imagem']
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.manager=self.request.user
        instance.save()
        messages.success(self.request,'Contato criado com sucesso!')
        return redirect('home')

class ContactUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'ContactUpdate.html'
    model = ContactList
    context_object_name = 'contact'
    fields = ['nome','email','telefone','genero','categoria','imagem']
    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request,'Contato atualizado com sucesso!')
        return redirect('contactdetail',instance.pk)

class ContactDelete(LoginRequiredMixin,DeleteView):
    template_name = 'ContactDelete.html'
    model = ContactList
    context_object_name = 'contact'
    success_url = '/'
    def delete(self,request,*args,**kwargs):
        messages.success(self.request,'Contato excluído com sucesso!')
        return super().delete(self,request,*args,**kwargs)

class CreateAccount(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')