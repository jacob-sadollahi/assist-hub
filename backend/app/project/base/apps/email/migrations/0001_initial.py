# Generated by Django 4.0 on 2022-09-12 16:26

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('to', models.TextField(verbose_name='To')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('compiled_template', models.TextField(blank=True, verbose_name='compiled_template')),
                ('bcc', models.TextField(blank=True, verbose_name='bcc')),
                ('is_sent', models.BooleanField(default=False, verbose_name='is_sent')),
                ('error', models.TextField(blank=True, null=True, verbose_name='error')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='token')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='EmailAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('file', models.FileField(upload_to='emails/attachments', verbose_name='file')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='email.email', verbose_name='email')),
            ],
            options={
                'verbose_name': 'Email attachment',
                'verbose_name_plural': 'Email Attachments',
            },
        ),
    ]