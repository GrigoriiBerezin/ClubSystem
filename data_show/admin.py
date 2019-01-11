from django.contrib import admin

from data_show import models

# Register your models here.
admin.site.empty_value_display = 'Unknown'
admin.site.list_max_show_all = 10


# inline and admin model for Club
class FilesInline(admin.TabularInline):
    model = models.File
    extra = 0


@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = (
        'name',
        'source',
        'club_head',
    )
    readonly_fields = ('date_ymd',)
    inlines = [
        FilesInline,
    ]


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    pass


# inlines and admin model for Student
class ContactInline(admin.TabularInline):
    model = models.Contact
    extra = 1


class ClubLeaderInline(admin.TabularInline):
    model = models.Club
    verbose_name = 'club to lead'
    fields = ('name', 'source')
    fk_name = 'club_head'
    extra = 0


class ClubManagerInline(admin.TabularInline):
    model = models.Club
    verbose_name = 'club to manage'
    fields = ('name', 'source')
    fk_name = 'manager'
    extra = 0


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'telephone',
    )
    fields = (
        ('first_name', 'last_name'),
        ('email', 'telephone'),
        'status',
    )
    list_filter = ('status',)
    inlines = [
        ClubLeaderInline,
        ClubManagerInline,
        ContactInline,
    ]
