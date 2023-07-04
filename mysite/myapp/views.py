from django.shortcuts import render

# Create your views here.


def index(request):
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, "myapp/partials/paragraph.html")
    return render(request, "myapp/dashboard.html")
