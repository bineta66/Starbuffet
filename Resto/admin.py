from django.contrib import admin
from .models import Traiteur

@admin.register(Traiteur)
class TraiteurAdmin(admin.ModelAdmin):
    list_display = ('nomcomplet', 'email', 'telephone', 'est_actif')
    list_filter = ('est_actif',)
    search_fields = ('nomcomplet', 'email')

    fieldsets = (
        ("Informations principales", {
            'fields': ('nomcomplet', 'specialites', 'description')
        }),
        ("Contact", {
            'fields': ('adresse', 'email', 'telephone')
        }),
        ("Autres", {
            'fields': ('image', 'est_actif')
        }),
    )