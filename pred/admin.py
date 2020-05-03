from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import *
from .models import Journal, Parameter, Options, JournalDatabase


class JournalA(admin.ModelAdmin):
    list_display = ('journal_name', 'journal_link')


class ParameterA(admin.ModelAdmin):
    list_display = ('parameter_name',)


class OptionsA(admin.ModelAdmin):
    list_display = ('option_name', 'score', 'parameter')


class JournalDatabaseA(admin.ModelAdmin):
    list_display = ('journal', 'parameter', 'chosen_option')


admin.site.register(Journal, JournalA)
admin.site.register(Parameter, ParameterA)
admin.site.register(Options, OptionsA)
admin.site.register(JournalDatabase, JournalDatabaseA)
