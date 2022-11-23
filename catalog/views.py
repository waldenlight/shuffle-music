from django.shortcuts import render

# Create your views here.
from .models import Song, Artist, SongInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_songs = Song.objects.all().count()
    num_instances = SongInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = SongInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_artists = Artist.objects.count()

    context = {
        'num_songs': num_songs,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_artists': num_artists,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)