from django.contrib import admin

from regular_exam.my_web.models import Profile, Fruit


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',)


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
