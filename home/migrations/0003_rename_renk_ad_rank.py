# Generated by Django 5.0.2 on 2024-02-24 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_slider_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='renk',
            new_name='rank',
        ),
    ]