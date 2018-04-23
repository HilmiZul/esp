from django.contrib import admin

from master.models import Siswa, Instansi

# Register your models here.
class SiswaAdmin(admin.ModelAdmin):
    list_display = ['NIS', 'nama', 'kelas']
    list_filter = ('kelas', 'program_ahli')
    search_fields = ['NIS', 'nama']
    list_per_page = 20

class InstansiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat']
    search_fields = ['nama', 'alamat']
    list_per_page = 20

admin.site.register(Siswa, SiswaAdmin)
admin.site.register(Instansi, InstansiAdmin)
