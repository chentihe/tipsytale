from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from .models import Post, Country, Type, Variety


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')

def index(request):
    post_list = Post.objects.all().order_by('-id')
    return render(request, 'index.html',{'post_list': post_list})

class PostDetailView(generic.DetailView):
    model = Post
    slug_field = 'slug'  # DetailView's default value: optional
    slug_url_kwarg = 'slug'   # Should match the name of the slug field on the model
    template_name = 'wine_blog/post_detail.html'

class CountryListView(generic.ListView):
    model = Country
    template_name = 'wine_blog/country_list.html'  # Specify your own template name/location
    def get_context_data(self, *args, **kwargs):
        context = super(CountryListView, self).get_context_data(*args, **kwargs)
        context['country_detail'] = Post.objects.all()
        return context

class CountryDetailView(generic.DetailView):
    model = Country
    slug_field = 'slug'  # DetailView's default value: optional
    slug_url_kwarg = 'slug'   # Should match the name of the slug field on the model
    def get_context_data(self, *args, **kwargs):
        context = super(CountryDetailView, self).get_context_data(*args, **kwargs)
        context['country_list'] = Country.objects.all()
        return context

class TypeListView(generic.ListView):
    model = Type
    template_name = 'wine_blog/type_list.html'  # Specify your own template name/location
    def get_context_data(self, *args, **kwargs):
        context = super(TypeListView, self).get_context_data(*args, **kwargs)
        context['type_detail'] = Post.objects.all()
        return context

class TypeDetailView(generic.DetailView):
    model = Type
    slug_field = 'slug'  # DetailView's default value: optional
    slug_url_kwarg = 'slug'   # Should match the name of the slug field on the model
    def get_context_data(self, *args, **kwargs):
        context = super(TypeDetailView, self).get_context_data(*args, **kwargs)
        context['type_list'] = Type.objects.all()
        return context

class VarietyListView(generic.ListView):
    model = Variety
    template_name = 'wine_blog/variety_list.html'
    def get_context_data(self, *args, **kwargs):
        context = super(VarietyListView, self).get_context_data(*args, **kwargs)
        context['variety_detail'] = Post.objects.all()
        return context


class VarietyDetailView(generic.DetailView):
    model = Variety
    slug_field = 'slug'  # DetailView's default value: optional
    slug_url_kwarg = 'slug'   # Should match the name of the slug field on the model
    def get_context_data(self, *args, **kwargs):
        context = super(VarietyDetailView, self).get_context_data(*args, **kwargs)
        context['variety_list'] = Variety.objects.all()
        return context