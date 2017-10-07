from django.contrib import admin

from works.models import *


class WorksImageInline(admin.TabularInline):
    model = WorksImage
    extra = 0


class WorksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Works._meta.fields]

    inlines = [WorksImageInline]

    class Meta:
        model = Works


admin.site.register(Works, WorksAdmin)


class WorksImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WorksImage._meta.fields]

    class Meta:
        model = WorksImage


admin.site.register(WorksImage, WorksImageAdmin)
