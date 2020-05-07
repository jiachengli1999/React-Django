from django.shortcuts import render

# point to template
def index(request):
    return render(request, 'frontend/index.html')
