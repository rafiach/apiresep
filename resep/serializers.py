from rest_framework import serializers
from .models import Produk, Keranjang, Transaksi

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class KeranjangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keranjang
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = '__all__'
