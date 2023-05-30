from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(Skill)



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'read']
    list_filter = ['read']
    readonly_fields = ['subject', 'name', 'message', 'email']
    search_fields = ['name']
    ordering = ['created_at']
admin.site.register(ContactMessage, ContactMessageAdmin)



class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    min_num = 3
    max_num = 20
    extra = 5

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
admin.site.register(Project, ProjectAdmin)


admin.site.register(Service)

