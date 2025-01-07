from django.db import models
from django.contrib.auth.models import User  # Menggunakan model User default dari Django

from django.db import models
from django.contrib.auth.models import User  # Menggunakan User bawaan Django

# Model Kategori
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)
    image_res = models.ImageField(upload_to='kategori_images/', null=True, blank=True)

    def __str__(self):
        return self.nama_kategori

# Model Produk
class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    image_res = models.ImageField(upload_to='produk_images/', null=True, blank=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

# Model Keranjang
class Keranjang(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    total_harga = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Menghitung total harga otomatis
        self.total_harga = self.jumlah * self.produk.harga
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.jumlah} x {self.produk.nama} oleh {self.user.username}'

#Model Transaksi
class Transaksi(models.Model):
    id_Produk = models.ForeignKey(Produk, on_delete=models.CASCADE)  # Pastikan ada field id_Produk
    jumlah = models.IntegerField()
    totalHarga = models.DecimalField(max_digits=10, decimal_places=2)  # Pastikan ada field totalHarga
    timestamp = models.DateTimeField(auto_now_add=True)
    ispay = models.BooleanField(default=False)  # Pastikan ada field ispay

    def __str__(self):
        return f"Transaksi {self.id_Produk.name} - {self.timestamp}"


class Resep(models.Model):
    nama = models.CharField(max_length=100)  # Nama resep
    bahan = models.TextField()  # Bahan-bahan resep (pisahkan dengan koma jika perlu)
    langkah = models.TextField()  # Langkah-langkah pembuatan
    image = models.ImageField(upload_to='resep_images/', null=True, blank=True)  # Opsional: Tambah gambar resep

    def __str__(self):
        return self.nama