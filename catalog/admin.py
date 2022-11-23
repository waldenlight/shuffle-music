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
    fields = ['first_name', 'last_name']


# Register the admin class with the associated model
admin.site.register(Artist, ArtistAdmin)

# Not necessary, unless different media formats introduced


class SongsInstanceInline(admin.TabularInline):
    model = SongInstance


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'display_genre')
    # Not necessary, unless different media formats introduced
    inlines = [SongsInstanceInline]

# Register the Admin classes for SongInstance using the decorator


@admin.register(SongInstance)
class SongInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'release_date')

    fieldsets = (
        (None, {
            'fields': ('song', 'label', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'release_date')
        }),
    )
