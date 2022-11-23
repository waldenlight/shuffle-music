from django.contrib import admin

# Register your models here.

from .models import Artist, Genre, Song, SongInstance

# admin.site.register(Song)
# admin.site.register(Artist)
admin.site.register(Genre)
# admin.site.register(SongInstance)

# Define the admin class


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


# Register the admin class with the associated model
admin.site.register(Artist, ArtistAdmin)

# Register the Admin classes for Song using the decorator


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'display_genre')

# Register the Admin classes for SongInstance using the decorator


@admin.register(SongInstance)
class SongInstanceAdmin(admin.ModelAdmin):
    pass
