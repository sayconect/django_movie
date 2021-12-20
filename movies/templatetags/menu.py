from django import template
from movies.models import Category, Movie, Genere
from django.db.models import F


register = template.Library()

@register.inclusion_tag('movies/menu_tag.html')
def show_menu(): # ми додавляємо арг тому що в нас є два одинакових вивода меню в футері і в хедері, і оцей class_menu ми передемов в темплейті в class відкрий menu_tag там буде з самого верху. або якшо далі хз то 7 відео парктичнох частини
    categories = Category.objects.all()
    return  {'categories': categories}


@register.inclusion_tag('movies/last_movies_tag.html')
def show_lastets_movie(count=5): # ми додавляємо арг тому що в нас є два одинакових вивода меню в футері і в хедері, і оцей class_menu ми передемов в темплейті в class відкрий menu_tag там буде з самого верху. або якшо далі хз то 7 відео парктичнох частини
    movies = Movie.objects.order_by('-primyer')[:count]
    return  {'movies': movies}


@register.inclusion_tag('movies/all_genre_tag.html')
def show_all_genres():
    genres = Genere.objects.all().only('name')
    return  {'genres': genres}

@register.inclusion_tag('movies/all_years_tag.html')
def show_all_years():
    years = Movie.objects.values('year').distinct().order_by('-year')
    return  {'years': years}