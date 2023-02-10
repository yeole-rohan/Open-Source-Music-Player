from django.contrib import admin

from .models import Artist, Song, Album

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "artistName", "created", "last_updated")

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id", "album", "song", "songName", "songThumbnail", "created", "last_updated" )

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("artist", "albumName", "created", "last_updated")
