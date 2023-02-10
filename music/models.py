from django.db import models
from django.utils.translation import gettext_lazy as _

class Artist(models.Model):
    artistName = models.CharField(_("Artist Name"), max_length=50)
    created = models.DateTimeField(_("Artist created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest artist update"), auto_now=True)


    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")

    def __str__(self):
        return self.artistName

class Album(models.Model):
    artist = models.ForeignKey("Artist", verbose_name=_("Artist Album"), on_delete=models.CASCADE)
    albumName = models.CharField(_("Album Name"), max_length=50)
    created = models.DateTimeField(_("Album created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest album update"), auto_now=True)

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")

    def __str__(self):
        return self.albumName
    
class Song(models.Model):
    album = models.ForeignKey("Album", verbose_name=_("Song Album"), on_delete=models.CASCADE)
    songThumbnail = models.ImageField(_("Song Thumbnail"),upload_to='thumbnail/', help_text=".jpg, .png, .jpeg, .gif, .svg supported")
    song = models.FileField(_("Song"), upload_to='songs/', help_text=".mp3 supported only",)
    songName = models.CharField(_("Song Name"), max_length=50)
    created = models.DateTimeField(_("Song created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest song update"), auto_now=True)

    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

    def __str__(self):
        return self.songName


