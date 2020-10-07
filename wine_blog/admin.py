from django.contrib import admin
from .models import Post, Type, Country, Variety

# Register your models here.

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'type', 'display_variety', 'created_at')

admin.site.register(Type)
admin.site.register(Country)
admin.site.register(Variety)