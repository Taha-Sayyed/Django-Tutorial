from django.contrib import admin
from .models import ChaiVariety,ChaiReview,ChaiCertificate,Stores

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model=ChaiReview
    extra=1

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=['name','type','date_added']
    inlines=[ChaiReviewInline]

class StoresAdmin(admin.ModelAdmin):
    list_display=['name','location']
    filter_horizontal=('chai_varities',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=['chai','certificate_number','issued_date','valid_untill']

admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(Stores,StoresAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)


















