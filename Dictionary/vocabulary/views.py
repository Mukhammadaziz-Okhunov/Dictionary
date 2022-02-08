from django.shortcuts import render
from .models import Togri, Notogri

def home(request):
    if request.method == 'POST':
        soz = request.POST["soz"]
        t_soz = Togri.objects.filter(soz=soz)
        if len(t_soz) > 0:
            notogri = Notogri.objects.filter(n_soz=soz)
            if len(notogri) > 0:
                t_soz = ["So'z ma'lumotlar omborida yo'q"]
                n_soz = ""
            else:
                t_soz = Togri.objects.filter(id=notogri[0].id)
                n_soz = Notogri.objects.filter(t_soz=t_soz[0])
        else:
            n_soz = Notogri.objects.filter(t_soz=t_soz[0])
        return render(request, 'result.html', {"ts": t_soz[0], "ns": n_soz})
    return render(request, "result.html")