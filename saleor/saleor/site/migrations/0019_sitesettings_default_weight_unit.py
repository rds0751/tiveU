# Generated by Django 2.0.3 on 2018-08-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0018_sitesettings_homepage_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='default_weight_unit',
            field=models.CharField(choices=[('kg', 'kg'), ('lb', 'lb'), ('oz', 'oz'), ('g', 'g')], default='kg', max_length=10),
        ),
    ]
