from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AgreagarIncidenteForm

from .models import *

##Vista de prueba
class TestView(TemplateView):
    template_name = 'prueba.html'
 
##Listado de todos los incidentes
class ListadoIncidentes(ListView):
    template_name = 'listado-incidentes.html'
    paginate_by = 6 #Numero de elementos por paginas
    
    def get_queryset(self):
        lista = Incidente.objects.filter(usuario=self.request.user.id).order_by('-id')
        return lista

    ##Metodo para requerir autenticacion
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(ListView, self).dispatch(*args, **kwargs)

##Vista para actualizar los incidentes
class ActualizarIncidente(UpdateView):
    template_name = "actualizar-incidente.html"
    model = Incidente
    
    form_class=AgreagarIncidenteForm ##Formulario personalizado
    success_url = reverse_lazy('incidentes')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        return super().post(request, *args, **kwargs)

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

##Vista para eliminar un incidente
class EliminarIncidente(DeleteView):
    model = Incidente
    template_name = "eliminar-incidente.html"
    success_url = reverse_lazy('incidentes')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)

##Vista para agregar un nuevo incidente
class AgregarIncidente(CreateView):
    template_name = "agregar-incidente.html"
    model = Incidente
    
    form_class=AgreagarIncidenteForm
    success_url = reverse_lazy('incidentes')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

##Vista de login
def Login(request):

    if request.user.is_authenticated:
        return redirect('incidentes')
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('incidentes')
            else:
                messages.warning(request,"Error al ingresar a sistema")          

        return render(request,'login.html',{'titulo':'Iniciar sesion'})

##Cerrar sesion
def Logout(request):
    logout(request)
    return redirect('login')