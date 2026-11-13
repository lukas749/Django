from django.shortcuts import render, HttpResponse

def ahoj(request):
    return HttpResponse("Ahoj svet!")

def o_mne(request):
    kontext = {
        "meno": "Lukáš",
        "vek": 17,
        "zaluby": ["skola", "matematika", "hokej"],
    
    }
    return render(request, "ulohy/o_mne.html", kontext)

def rozvrh(request):
    hodiny = [
        {"cislo": 1, 'predmet': "Programovanie"},
        {"cislo": 2, 'predmet': "Programovanie"},
        {"cislo": 3, 'predmet': "Programovanie"},
        {"cislo": 4, 'predmet': "Prax"},
        {"cislo": 5, 'predmet': "Prax"},
        {"cislo": 6, 'predmet': "Anglický Jazyk"},
                                                
    ]
    return render(request, 'ulohy/rozvrh.html', {'den' : 'Pondelok', "hodiny" : hodiny})

def pozdrav(request):
     meno = request.GET.get("meno","") # .get nájde a vráti hodnotu prvku s indexom(kľúčom) meno, ak ho nenájde vloží prázdny string
     return render(request, "ulohy/pozdrav.html",{"meno": meno})

def sucet(request):
    vysledok = None
    if request.method == "POST":
        a  = int(request.POST["a"])
        b  = int(request.POST["b"])
        vysledok = a + b
    return render(request, 'ulohy/sucet.html', {"vysledok": vysledok})

def kalkulacka(request):
    vysledok = None
    if request.method == "POST":
        cislo_1  = int(request.POST["cislo_1"])
        cislo_2  = int(request.POST["cislo_2"])
        znamienko = request.POST["znamienko"]
        if znamienko == "+":
            vysledok = cislo_1 + cislo_2
        elif znamienko == "-":
            vysledok = cislo_1 - cislo_2
        else:
            vysledok = cislo_1 * cislo_2
    return render(request, 'ulohy/kalkulacka.html', {"vysledok": vysledok} )

def obdlznik(request):
    vysledok = None
    if request.method == "POST":
        strana_a = float(request.POST["strana_a"])
        strana_b = float(request.POST["strana_b"])
        vyber = request.POST["vyber"]
        if vyber == "obsah":
            vysledok = round(strana_a * strana_b, 2)
        else:
            vysledok = round(2*(strana_a + strana_b),2)
    return render(request, 'ulohy/obdlznik.html', {"vysledok": vysledok})