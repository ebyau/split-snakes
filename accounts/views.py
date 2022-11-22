from django.shortcuts import render,redirect
from .forms import UploadForm
from .models import Audio

# Create your views here.

def home(request):
    audio = Audio.objects.all()
    return render(request, 'dashboard.html', {'audio':audio})


def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request, 'form.html', {'form': UploadForm})
