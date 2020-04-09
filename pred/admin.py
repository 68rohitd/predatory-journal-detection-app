from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import *
from .models import Journaltable, Journaltable2

class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id')


@admin.register(Journaltable)
class Journal(ImportExportModelAdmin):
    pass

@admin.register(Journaltable2)
class Journal2(ImportExportModelAdmin):
    pass