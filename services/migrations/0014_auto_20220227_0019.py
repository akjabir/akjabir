# Generated by Django 3.1.4 on 2022-02-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_auto_20220227_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='committeeinfo',
            old_name='address',
            new_name='permament_address',
        ),
        migrations.AddField(
            model_name='committeeinfo',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='committeeinfo',
            name='present_address',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]