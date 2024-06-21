from django.contrib import admin

from .models import Participation


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'survey')


admin.site.register(Participation, ParticipationAdmin)
