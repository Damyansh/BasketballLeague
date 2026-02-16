from django.contrib import admin

from common.models import Award


# Register your models here.
@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', )
    filter_horizontal = ('players',)