# Generated by Django 2.2.10 on 2021-02-04 16:38

import pyotp

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import temba.utils.text


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orgs", "0074_auto_20201214_1714"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="backuptoken",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="backuptoken",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="backuptoken",
            name="modified_by",
        ),
        migrations.RemoveField(
            model_name="backuptoken",
            name="modified_on",
        ),
        migrations.AddField(
            model_name="backuptoken",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="backup_tokens",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="backuptoken",
            name="created_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="backuptoken",
            name="settings",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="backups", to="orgs.UserSettings"
            ),
        ),
        migrations.AlterField(
            model_name="backuptoken",
            name="token",
            field=models.CharField(default=temba.utils.text.generate_token, max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name="backuptoken",
            name="used",
            field=models.BooleanField(default=False),
        ),
        migrations.RenameField(
            model_name="backuptoken",
            old_name="used",
            new_name="is_used",
        ),
        migrations.AlterField(
            model_name="usersettings",
            name="otp_secret",
            field=models.CharField(default=pyotp.random_base32, max_length=18, null=True, verbose_name="OTP Secret"),
        ),
    ]
