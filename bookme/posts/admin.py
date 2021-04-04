from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from .models import Host, Traveller, Apartment, Rent, Roomtype, Tag

from ckeditor.widgets import CKEditorWidget


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)
admin.site.register(Host)
admin.site.register(Traveller)
admin.site.register(Apartment)
admin.site.register(Rent)
admin.site.register(Roomtype)
admin.site.register(Tag)

