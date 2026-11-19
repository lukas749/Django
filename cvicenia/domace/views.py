from django.shortcuts import render, HttpResponse
def domace(request):
    kontext = {
        "meno": "Lukáš",
        "vek": 17,
        "oblubene_predmety": ["programovanie", "matematika", "prax"],
    
    }
    return render(request, "domace/vizitka.html", kontext)

def teplota(request):
    vysledok = None

    if request.method == "POST":
        teplota = float(request.POST["teplota"])
        hodnota = request.POST["hodnota"]

        if hodnota == "fahrenheit":
            vysledok = (teplota * 9/5) + 32

        elif hodnota == "celsius":
            vysledok = (teplota - 32) * 5/9

        else:
            vysledok = teplota

    vysledok = round(vysledok, 1)
    return render(request, 'teplota.html', {"vysledok": vysledok, "hodnota": hodnota})