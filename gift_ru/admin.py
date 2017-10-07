from django.contrib import admin

from gift_ru.models import *


class HomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Home._meta.fields]

    class Meta:
        model = Home


admin.site.register(Home, HomeAdmin)


class SliderImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SliderImage._meta.fields]

    class Meta:
        model = SliderImage


admin.site.register(SliderImage, SliderImageAdmin)


class StepByAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StepBy._meta.fields]

    class Meta:
        model = StepBy


admin.site.register(StepBy, StepByAdmin)