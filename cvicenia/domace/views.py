from django.shortcuts import render
def domace(request):
    kontext = {
        'meno': 'Lukáš',
        'priezvisko': 'Mäkký',
    }
    return render(request, "domace/domace.html", kontext)