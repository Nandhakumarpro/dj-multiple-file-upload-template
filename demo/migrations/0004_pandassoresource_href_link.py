# Generated by Django 3.2.15 on 2022-10-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_pandassoresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='pandassoresource',
            name='href_link',
            field=models.URLField(blank=True, max_length=2550, null=True),
        ),
    ]
