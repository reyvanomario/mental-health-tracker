from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275613',
        'name': 'Reyvano Mario Sianturi',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)