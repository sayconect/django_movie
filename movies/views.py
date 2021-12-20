from django import template
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.

class MovieList(ListView):
    model = Movie
    template_name = 'movies/movies.html'
    context_object_name = 'movies'
    paginate_by = 4

    def get_queryset(self):
        return Movie.objects.filter(draft=False)


class MovieListByCategory(ListView):
    model = Movie
    template_name = 'movies/movies.html'
    context_object_name = 'movies'
    allow_empty = False
    paginate_by = 4


    def get_queryset(self):
        return Movie.objects.filter(category__url = self.kwargs['categ_slug'])


class MovieListByFilter(ListView):
    model = Movie
    template_name = 'movies/movies.html'
    context_object_name = 'movies'
    paginate_by = 4


    def get_queryset(self):
        a = self.request.GET.copy()
        
        print(list(a.lists()))
        print(self.request.GET.getlist('year'))
        if self.request.GET.get('year') and self.request.GET.get('genre'):
            movies= Movie.objects.filter(year__in=self.request.GET.getlist('year'),
                                        genre__url__in=self.request.GET.getlist('genre'))

        else:
            movies= Movie.objects.filter(Q(year__in=self.request.GET.getlist('year'))|
                                    Q(genre__url__in=self.request.GET.getlist('genre'))).distinct()
        return movies


class MoviesBySearch(ListView):
    model = Movie
    template_name = 'movies/movies.html'
    context_object_name = 'movies'
    paginate_by = 1
    allow_empty = False

    def get_queryset(self):
        return Movie.objects.filter(title__icontains = self.request.GET.get('search'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = f"search={self.request.GET.get('search')}&" # це ми робмо для тогог щоб у випадку якщо результат займає дві сторірки при переході на наступну параметре search не пропадав
        return context


class SingleMovie(DetailView):
    model = Movie
    template_name = 'movies/single_movie.html'
    context_object_name = 'movie'
    slug_field = 'url'

                            

class AddReview(CreateView):
    form_class = ReviewModelForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        movie = Movie.objects.get(id=self.kwargs['pk'])
        self.object.movie = movie
        self.object.save()
        return redirect(movie.get_absolute_url())


class ActorInfo(DetailView):
    model = ActorAndDirector
    template_name = 'movies/actor.html'
    context_object_name = 'actor'
    slug_field = 'name'
        