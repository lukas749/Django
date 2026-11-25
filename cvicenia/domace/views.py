from django.shortcuts import render, HttpResponse
def domace(request):
    kontext = {
        "meno": "Lukáš",
        "vek": 17,
        "oblubene_predmety": ["programovanie", "matematika", "prax"],
    
    }
    return render(request, "domace/vizitka.html", kontext)

def du3_teplota(request):
    vysledok = None

    if request.method == "POST":
        teplota = float(request.POST.get("teplota").replace(",", "."))
        smer = request.POST.get("smer")
        if smer == "CtoF":
            vysledok = teplota * 9 / 5 + 32
            jednotka = "°F"
        else:
            vysledok = (teplota - 32) * 5 / 9
            jednotka = "°C"
        vysledok = f"{vysledok:.1f} {jednotka}"
        
    return render(request, "domace/du3_teplota.html", {"vysledok": vysledok})
