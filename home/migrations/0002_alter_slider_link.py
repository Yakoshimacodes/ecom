# Generated by Django 5.0.2 on 2024-02-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
