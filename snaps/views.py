from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Album, Snap
from .pyfunctions import false_string, album_exists

def index(request):
    return render(request, 'snaps/index.html/')

@login_required(login_url=reverse_lazy('login'))
def upload(request):
    if request.method == "POST":
        error = ""
        name = request.POST['title']
        caption = request.POST['caption']
        album = request.POST['album']
        #  -- validations --
        if not false_string(name):
            error = "Invalid charecters in title"
        elif not false_string(caption):
            error = "Invalid charecters in caption"

        if 'new_album' in request.POST and request.POST['new_album'] == 'True' :

            if album == None:
                album = album_exists('General Upload')
            
            elif album_exists(album) != False:
                album = album_exists(album)
            
            elif false_string(album):
                Album.objects.create(name=album, author=request.user.username)
                album = Album.objects.get(name=album)

            else:
                error = "Invalid charecters in Album name"

        else:
            if album == "":
                album = album_exists('General Upload')
            else:    
                album = album_exists(album)
                if album == False:
                    error = """
                    Invalid Album name/ Album does not exists ->
                    (Tip: Check the 'New Album' to create one on the fly!)"""
        
        # creating new snap
        myfile = request.FILES['file']
       
        uploaded_image = Snap.objects.create(image=myfile, author=request.user.username, name=name, caption=caption)

        if error:
            return render(request, 'snaps/upload.html', {'title':'upload error', 'error':error})
        else:
            return render(request, 'snaps/image.html', {'title':'upload success', 'image':uploaded_image.image.url})
         
    else:    
        return render(request, 'snaps/upload.html', {'title':'upload'})


@login_required(login_url=reverse_lazy('login')) 
def profile(request):
    pass


def albums(request):
    if request.method == "POST":
        pass
    else: 
        pass
