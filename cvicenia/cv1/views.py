from django.shortcuts import render

def cv1_index(request):
    kontext = {
        "meno": "Lukáš",
    }
    return render(request, "cv1/cv1_index.html", kontext)

def cv1_obchod(request):
    produkty = [
            {"nazov": "jogurt", "cena": 1.99},
            {"nazov": "šunka", "cena": 5.99},
            {"nazov": "marlenka", "cena":7.49},
            {"nazov": "banány", "cena": 2.99},                             
        ]
    max_cena = request.GET.get("max_cena","").strip()
    chyba = None
    
    if max_cena != "":
        try : 
            limit = float(max_cena.replace(",", "."))
            produkty =[p for p in produkty if p["cena"] == limit]
        except ValueError:
            chyba = "neplatne cislo"

    return render(request, 'cv1/obchod.html', {"produkty" : produkty, "max_cena" : max_cena, "chyba" : chyba,})

#|floatformat:2

def cv1_body(request):
    if request.method == "POST":
        body  = float(request.POST["body"]),
        maximum  = float(request.POST["maximum"]),
        percenta = body / maximum * 100
    if percenta >= 90:
        znamka = 1
    elif 90 > percenta >= 75:
        znamka = 2
    elif 75 > percenta >= 50:
        znamka = 3
    elif 50 > percenta >= 30:
        znamka = 4
    elif percenta < 30:
        znamka = 5
    return render(request, 'cv1/body.html', {"znamka" : znamka, "percenta" : percenta})