from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .models import URLS


# Create your views here.


def firebase_view(request):
    if request.method == 'POST':
        downloadURL = request.POST['url']
        url = URLS.objects.create(
            imageURL=downloadURL,
        )
        url.save()
        messages.success(request, "File upload in Firebase Storage successful")
        return redirect('firebase_view')
    else:
        return render(request, "firebase_app/firebase.html", {})


def images_view(request):
    urls = URLS.objects.all()
    context = {
        'urls': urls,
    }
    return render(request, "firebase_app/images.html", context)
