# Generated by Django 2.1.8 on 2019-07-03 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("contacts", "0103_auto_20190703_2011")]

    operations = [migrations.RemoveField(model_name="contact", name="is_test")]