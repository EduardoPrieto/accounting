# Generated by Django 3.2.5 on 2022-03-03 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('cash_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='accounting_break',
            new_name='AccountingBreak',
        ),
    ]
