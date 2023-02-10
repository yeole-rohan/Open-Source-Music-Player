from django.shortcuts import render
from .models import Song

def index(request):
    allSongs = Song.objects.all()
    return render(request, template_name="index.html", context={"allSongs" : allSongs})
