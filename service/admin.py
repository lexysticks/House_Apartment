from django.contrib import admin
from . models import Property,Rent,shortlet,Buy,Land
# Register your models here.
admin.site.register([Property])
admin.site.register(Rent)
admin.site.register(Buy)
admin.site.register(shortlet)
admin.site.register(Land)