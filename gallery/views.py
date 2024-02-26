from django.shortcuts import render, get_object_or_404, redirect
from gallery.models import Fotografia

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    return render(request, 'gallery/index.html', {'cards': fotografias })

def image(request, foto_id):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'gallery/image.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "value" in request.GET:
        nome_a_buscar = request.GET['value']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'gallery/buscar.html', {'cards': fotografias})