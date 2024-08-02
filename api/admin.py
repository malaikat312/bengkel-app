from django.contrib import admin
from .models import Bengkel, Layanan

@admin.register(Bengkel)
class BengkelAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat', 'deskripsi', 'get_layanan', 'latitude', 'longitude', 'nomer_hp')
    list_filter = ('layanan',)
    search_fields = ('nama', 'alamat', 'deskripsi')

    def get_layanan(self, obj):
        return ", ".join([layanan.nama for layanan in obj.layanan.all()])
    get_layanan.short_description = 'Layanan'

@admin.register(Layanan)
class LayananAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga')
    search_fields = ('nama',)