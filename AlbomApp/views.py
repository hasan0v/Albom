from django.shortcuts import render, redirect, HttpResponse
from .models import Photo
from django.template import RequestContext

# Create your views here.

def gallery(request):
    # category = request.GET.get('category')
    # if category is None:
    #     photos = Photo.objects.all()

    # else:
    #     photos = Photo.objects.filter(category__name=category)
    photos = Photo.objects.all()
    # print(photos)
    # categories = Category.objects.all()
    context = {'photos':photos}
    return render(request, 'photos/gallery.html', {'photos':photos})

def ViewPhoto(request, pk):
        photo = Photo.objects.get(id=pk)
        return render(request, 'photos/photo.html', {'photo':photo})



def AddPhoto(request):

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        print(data)
        photo = Photo.objects.create(
            image = image,
            description = data['description'],

        )
        return redirect('gallery')




    return render(request, 'photos/add.html')