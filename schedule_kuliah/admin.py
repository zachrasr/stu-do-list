from django.contrib import admin
from .models import Matakuliah, Dosen, Jadwal

# Register your models here.

admin.site.register(Matakuliah)
admin.site.register(Dosen)
admin.site.register(Jadwal)