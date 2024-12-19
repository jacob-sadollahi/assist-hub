from django.contrib import admin

from .models import Email, EmailAttachment, MailBindr
from .tasks import send_mail_task


class EmailAttachmentInline(admin.TabularInline):
    model = EmailAttachment
    extra = 1


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['subject', 'to', 'is_sent', 'created']
    list_filter = ['is_sent', 'created']
    readonly_fields = ['token']
    inlines = [
        EmailAttachmentInline,
    ]
    actions = ['force_send']
    search_fields = ['to', 'subject']

    def force_send(self, request, queryset):
        for email in queryset.all():
            send_mail_task.delay(pk=email.pk, force_send=True)

    force_send.short_description = "Force send emails"


@admin.register(MailBindr)
class MailBindrAdmin(admin.ModelAdmin):
    search_fields = [
        'to', 'variables',
    ]
    list_display = [
        'id', 'to', 'created',
    ]
    list_filter = [
        'created',
    ]
