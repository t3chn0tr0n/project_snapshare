from .models import Album


def false_string(string):
    danger_chars = ['[', '[', '*', '&', '|', '<', '>', '\\']
    for x in danger_chars:
        if x in string:
            return False
        else:
            return True

def album_exists(album_key):
    all_albums = Album.objects.all()
    for each_album in all_albums:
        if each_album.name.lower() == album_key.lower():
            return each_album
    return False
