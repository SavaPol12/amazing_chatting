from django.contrib import admin

from .models import Note, User


class UserAdmin(admin.ModelAdmin):
    pass


class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Note, NoteAdmin)
