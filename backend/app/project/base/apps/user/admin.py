from django.contrib import admin
from django.contrib.admin.templatetags.admin_list import _boolean_icon
from django.contrib.auth.admin import UserAdmin

from project.settings import _
from project.base.apps.user.models import Profile, Email, User


class UserProfileInline(admin.StackedInline):
    model = Profile


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'middle_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]
    list_display = [
        'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'display_email'
    ]
    search_fields = [
        'username', 'first_name', 'last_name'
    ]

    inlines = [UserProfileInline, EmailInline]

    def display_email(self, user):
        return user.email

    def get_inline_instances(self, request, obj=None):
        if obj:
            return super(CustomUserAdmin, self).get_inline_instances(request, obj)
        return []

    display_email.short_description = 'E-Mail'
    display_email.allow_tags = True


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'user', 'main_email', 'get_expired', 'created', 'validated',
    ]
    search_fields = [
        'user__first_name', 'user__last_name', 'email', 'main_email', 'validated',
    ]
    autocomplete_fields = [
        'user'
    ]

    def get_expired(self, obj):
        return _boolean_icon(obj.expired)

    get_expired.short_description = 'Expired'


admin.site.register(User, CustomUserAdmin)
