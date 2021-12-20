from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db.models import fields
from django.utils.safestring import mark_safe
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget




class MovieAdminForm(forms.ModelForm):
    descriptions = forms.CharField(label='Description', widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ['name', 'email']

class MovieShotInline(admin.TabularInline):
    model = MovieShot
    extra = 1
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="150" height="60"')
    get_image.short_description = 'photo'



class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('id','title','url', 'year', 'draft', 'get_image')
    list_display_links = ('title', 'id', 'url')
    list_filter = ('category',)
    list_editable = ['draft']
    search_fields = ('title', 'category__name') # категорія це обєкт тому треба робити так
    inlines = [MovieShotInline, ReviewInline]
    save_as = True
    save_on_top = True
    form = MovieAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')
    get_image.short_description = 'photo'


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'get_image')


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
    get_image.short_description = 'photo'

    readonly_fields = ['get_image']
admin.site.register(Category)
admin.site.register(Genere)
admin.site.register(Movie, MovieAdmin)
admin.site.register(ActorAndDirector, ActorAdmin)
admin.site.register(MovieShot)
admin.site.register(RaitingStar)
admin.site.register(Raiting)
admin.site.register(Review)

admin.site.site_title = 'Django moview'
admin.site.site_header = 'Django moview'