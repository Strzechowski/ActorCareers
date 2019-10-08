from django.shortcuts import render, redirect
from praca_inzynierska.models import Announcement
from django.core.files.storage import FileSystemStorage
from .forms import PhotoForm
from .models import Photo
from django.templatetags.static import static

def index(request):
    context = {}
    return render(request, "index.html", context)

def announcement(request):
    announcements = Announcement.objects.all().order_by('-created_on')
    context = {
        "announcements": announcements
    }
    return render(request, "announcement.html", context)

def announcement_detail(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    context = {
        'announcement': announcement
    }
    return render(request, 'announcement_detail.html', context)

def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo_instance = form.save(commit=False)
            photo_instance.user = request.user
            photo_instance.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {
        'form': form
    })

def delete_photo(request, pk):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=pk)
        photo.delete()
    return redirect('photo_list')

def photo_list(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'photo_list.html', {
        'photos': photos
    })