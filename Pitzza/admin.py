from django.contrib import admin

from .models import PitzzaExtra, PitzzaType, Pitzza, PitzzaThrough
# Register your models here.



class PitzzaTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'piecesNum', 'price',)
    pass
admin.site.register(PitzzaType, PitzzaTypeAdmin)



class PitzzaExtraAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'price',)
    pass
admin.site.register(PitzzaExtra, PitzzaExtraAdmin)

class PitzzaThroughInline(admin.TabularInline):
    model = Pitzza.pExtras.through


class PitzzaAdmin(admin.ModelAdmin):
    #list_display = ('__str__','pType',)
    inlines = [
        PitzzaThroughInline,
    ]
    pass
admin.site.register(Pitzza,PitzzaAdmin)