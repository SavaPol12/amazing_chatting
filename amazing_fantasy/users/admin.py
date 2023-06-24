from django.contrib import admin
from .models import User, Note


class UserAdmin(admin.ModelAdmin):
    pass


class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Note, NoteAdmin)