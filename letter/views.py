from django.shortcuts import render, redirect

from master.models import Instansi
from letter.models import Permohonan

# Create your views here.
def form_letter(request):
    instansi = Instansi.objects.order_by('nama')
    return render(request, 'form_letter.html', {'instansi':instansi})

# CETAK
def form_cetak(request):
    if request.POST:
        get_req = request.POST['id_ins']
        if get_req is not None:
            meta_surat = Permohonan.objects.filter(nama_instansi_id=request.POST['id_ins'])
            instansi = Instansi.objects.get(id=request.POST['id_ins'])
            result = render(request, 'cetak.html', {'meta_surat':meta_surat, 'instansi':instansi})
        else:
            result = redirect('/')
    else:
        result = redirect('/')
    return result
