# Generated by Django 2.1.1 on 2018-09-20 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20180914_0515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'staff'},
        ),
        migrations.AlterModelOptions(
            name='employeetype',
            options={'verbose_name': 'role'},
        ),
    ]
