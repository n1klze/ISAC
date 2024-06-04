from django.contrib import admin

from .models import Assembler, Driver, Mechanic, Technician, Welder, Worker

# Register your models here.
admin.site.register(Worker)
admin.site.register(Driver)
admin.site.register(Mechanic)
admin.site.register(Technician)
admin.site.register(Welder)
admin.site.register(Assembler)
