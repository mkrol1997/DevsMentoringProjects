from django.shortcuts import render, redirect
from .forms import UploadImageForm
from .models import UploadedImage


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadImageForm()
    return render(request, 'image_upload/upload_image.html', {'form': form})


def list_images(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_upload/list_images.html', {'images': images})
