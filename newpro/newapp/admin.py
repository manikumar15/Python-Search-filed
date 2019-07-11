from django.contrib import admin
from .models import News,Python,Api,Html,Search

class Newsadmin(admin.ModelAdmin):
    list_display = ('Email',)

admin.site.register(News, Newsadmin)


admin.site.site_header = 'Personal Blog'

class Pythonadmin(admin.ModelAdmin):
    list_display = ('name','email','phone','message')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Python,Pythonadmin)

class Apiadmin(admin.ModelAdmin):
    list_display = ('name','email','phone','message')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Api,Apiadmin)

class Htmladmin(admin.ModelAdmin):
    list_display = ('name','email','phone','message')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Html,Htmladmin)

class Searchadmin(admin.ModelAdmin):
    list_display = ('course','faculty','timings','duration','timings')
admin.site.register(Search,Searchadmin)