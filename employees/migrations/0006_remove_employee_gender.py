# Generated by Django 2.1.1 on 2018-10-01 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20181001_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
    ]
