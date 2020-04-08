from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import *
from .models import Journaltable

class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id')


@admin.register(Journaltable)
class Journal(ImportExportModelAdmin):
    pass
