from django.urls import path
from .views import ProdukAPI, KeranjangAPI, TransaksiAPI
from .views import rekomendasi_view

urlpatterns = [
    path('produk/', ProdukAPI.as_view(), name='produk-api'),
    path('keranjang/', KeranjangAPI.as_view(), name='keranjang-api'),
    path('transaksi/', TransaksiAPI.as_view(), name='transaksi-api'),
    path('rekomendasi/', rekomendasi_view, name='rekomendasi'),
]



