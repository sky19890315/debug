from django.contrib import admin
from TestModel.models import Test, Contact, Tag


# Register your models here.
# admin.site.register([Test, Contact, Tag])


class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')
    list_display = ('name', 'age', 'email')
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name','email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]
    )
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])