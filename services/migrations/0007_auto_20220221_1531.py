# Generated by Django 3.1.4 on 2022-02-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20220214_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='content_for',
            field=models.CharField(choices=[('1', 'Our History'), ('2', 'Academic History'), ('3', 'At a Glance')], max_length=1),
        ),
    ]
