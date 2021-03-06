# Generated by Django 3.1.4 on 2022-04-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_allinfo_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(blank=True, max_length=100)),
                ('work_image', models.FileField(blank=True, upload_to='work_image')),
                ('order', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'work gallary',
                'verbose_name_plural': 'add work gallary',
            },
        ),
    ]
