from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'categ_slug':self.url})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    

class ActorAndDirector(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='actors/')


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('actor', kwargs={'slug':self.name})
    
    class Meta:
        verbose_name = 'Actors and Directors'
        verbose_name_plural = 'Actors and Directors'


class Genere(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Genere'
        verbose_name_plural = 'Generes'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default='')
    descriptions = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    year = models.PositiveSmallIntegerField(default=2019)
    country = models.CharField(max_length=30)
    director = models.ManyToManyField(ActorAndDirector, related_name='movie_director' )
    actor = models.ManyToManyField(ActorAndDirector, related_name='movie_actor' ) 
    genre = models.ManyToManyField(Genere, related_name='movie_genre')
    primyer = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text='Input summ on dolars')
    fees_in_usa = models.IntegerField(default=0, help_text='Input summ on dolars')
    fees_in_word = models.IntegerField(default=0, help_text='Input summ on dolars')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(unique=True, max_length=150)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug':self.url})

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = "Movies"

class MovieShot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_shot/')
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE, blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie shot'
        verbose_name_plural = 'Movie shots'

class RaitingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Raiting star'
        verbose_name_plural = 'Raiting stars'

class Raiting(models.Model):
    ip = models.CharField(max_length=15, verbose_name='Ip adress')
    star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE, verbose_name='star')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='movie')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Raiting'
        verbose_name_plural = 'Raiting'

class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    Text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self',on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
