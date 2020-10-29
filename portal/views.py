from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView, ListView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from portal.models import Emmamodel, Christymodel, Robmodel, Imomodel


class Loginview(FormView):
    form_class = AuthenticationForm
    template_name = 'portal/login.html'
    success_url = reverse_lazy('portal:emma')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class Logoutview (RedirectView):
    url = reverse_lazy('portal:logoutcon')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(self, request, args, **kwargs)


def logoutcon(request):
    return render(request, 'portal/logoutcon.html')


def view(request):
    return render(request, 'portal/portal_view.html')


#class Emmaview(LoginRequiredMixin, ListView):
 #   model = Emmamodel
  #  template_name = 'portal/portal_view2.html'
   # context_object_name = 'emma'
@login_required(login_url='portal:emmalog')
def emmaview(request):
    anyname = Emmamodel.objects.all()
    return render(request, 'portal/portal_view2.html', {'emma': anyname})




class Loginview2(FormView):
    form_class = AuthenticationForm
    template_name = 'portal/login2.html'
    success_url = reverse_lazy('portal:christy')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


@login_required(login_url='portal:christylog')
def christyview(request):
    anyname1 = Christymodel.objects.all()
    return render(request, 'portal/portal_view3.html', {'christy': anyname1})




class Loginview3(FormView):
    form_class = AuthenticationForm
    template_name = 'portal/login3.html'
    success_url = reverse_lazy('portal:rob')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


@login_required(login_url='portal:roblog')
def robview(request):
    anyname2 = Robmodel.objects.all()
    return render(request, 'portal/portal_view4.html', {'rob': anyname2})


class Loginview4(FormView):
    form_class = AuthenticationForm
    template_name = 'portal/login4.html'
    success_url = reverse_lazy('portal:imo')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


@login_required(login_url='portal:imolog')
def imoview(request):
    anyname3 = Imomodel.objects.all()
    return render(request, 'portal/portal_view5.html', {'imo': anyname3})


# Create your views here.
