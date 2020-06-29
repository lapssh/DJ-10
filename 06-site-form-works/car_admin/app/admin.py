from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    search_fields = ['brand', 'model']
    list_display = ('brand', 'model', 'review_count')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title')
    search_fields = ['car__brand', 'car__model', 'title']
    list_filter = ('car', 'title')


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
