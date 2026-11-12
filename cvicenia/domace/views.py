from django.shortcuts import render, HttpResponse
def domace(request):
    kontext = {
        "meno": "Lukáš",
        "vek": 17,
        "oblubene_predmety": ["programovanie", "matematika", "prax"],
    
    }
    return render(request, "domace/vizitka.html", kontext)