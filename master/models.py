from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Siswa(models.Model):
    kelas_choices = (
        ('XI RPL 1', 'XI RPL 1'),
        ('XI RPL 2', 'XI RPL 2'),
        ('XI RPL 3', 'XI RPL 3'),
        ('XI TKJ 1', 'XI TKJ 1'),
        ('XI TKJ 2', 'XI TKJ 2'),
        ('XI TKJ 3', 'XI TKJ 3'),
        ('XI TKJ 4', 'XI TKJ 4'),
    )

    program_choices = (
        ('Teknik Komputer & Jaringan', 'Teknik Komputer & Jaringan'),
        ('Rekayasa Perangkat Lunak', 'Rekayasa Perangkat Lunak'),
    )

    NIS = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=8, choices=kelas_choices)
    program_ahli = models.CharField(max_length=26, choices=program_choices)

    def __unicode__(self):
        return self.nama

class Instansi(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __unicode__(self):
        return self.nama
