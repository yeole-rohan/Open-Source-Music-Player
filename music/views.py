from django.shortcuts import render
from django.db.models import Q

from .models import Song

def index(request):
    allSongs = Song.objects.all().order_by('-last_updated')
    return render(request, template_name="music/index.html", context={"allSongs" : allSongs})


def search_songs(request): 
    template_path = 'music/search_result.html'
    
    search_query = request.GET.get('search', None)

    if search_query: 
        search_result = Song.objects.filter(
            Q(songName__icontains=search_query) | 
            Q(album__albumName__icontains=search_query) | 
            Q(album__artist__artistName__icontains=search_query)
        ).distinct()
    else: 
        search_result = Song.objects.all()
        
    context = {'search_result' : search_result, 'search_query' : search_query}
    return render(request, template_path, context)