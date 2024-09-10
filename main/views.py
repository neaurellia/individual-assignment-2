from django.shortcuts import render

def show_main(request):
    context = {
        'id': 'Catherine Aurellia - KKI',
        'name': 'MIAU',
        'price': '50.000',
        'description': 'All karaoke packages are priced at Rp. 50.000/hour'
    }

    return render(request, "main.html", context)