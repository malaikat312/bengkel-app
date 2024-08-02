from django.db import models

class Bengkel(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)
    deskripsi = models.TextField()
    layanan = models.ManyToManyField('Layanan', related_name='bengkels')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    nomer_hp = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

class Layanan(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama
