from django.contrib import admin
from .models import Entrada
from .models import Saida
from .models import Toner
from .models import Departamento


# Register your models here.
admin.site.register(Toner)
admin.site.register(Departamento)
admin.site.register(Entrada)
admin.site.register(Saida)




