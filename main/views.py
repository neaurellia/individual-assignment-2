from django.shortcuts import render

def show_main(request):
    context = {
        'App Name' : 'MIAU',
        'Name': 'Catherine Aurellia',
        'Class': 'PBP KKI'
    }

    return render(request, "main.html", context)