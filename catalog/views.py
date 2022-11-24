from django.views import generic
from django.shortcuts import render

# Create your views here.
from .models import Song, Artist, SongInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_songs = Song.objects.all().count()
    num_instances = SongInstance.objects.all().count()

    # Available songs (status = 'a')
    num_instances_available = SongInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_artists = Artist.objects.count()

# Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_songs': num_songs,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_artists': num_artists,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class SongListView(generic.ListView):
    model = Song

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SongListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class SongDetailView(generic.DetailView):
    model = Song
    paginate_by = 10
