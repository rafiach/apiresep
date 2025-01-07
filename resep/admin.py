
# Register your models here.
from django.contrib import admin
from .models import Produk, Resep, Keranjang

admin.site.register(Produk)
admin.site.register(Resep)
admin.site.register(Keranjang)

from django.contrib import admin
from .models import Kategori, Transaksi

# admin.py
from django.contrib import admin
from .models import Transaksi

@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_Produk', 'jumlah', 'totalHarga', 'timestamp', 'ispay')  # Pastikan semua field ada di model

# Mendaftarkan model Kategori di Admin
@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_kategori', 'image_res')  # Pastikan 'name' dan 'imageRes' ada di model