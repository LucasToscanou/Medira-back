# Generated by Django 5.1.7 on 2025-03-29 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weight',
            new_name='WeightRecord',
        ),
    ]
