# Generated by Django 3.1.4 on 2021-10-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20211002_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='logo',
            field=models.ImageField(upload_to='company_info'),
        ),
    ]
