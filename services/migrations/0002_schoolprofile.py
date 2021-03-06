# Generated by Django 3.1.4 on 2021-10-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=160)),
                ('slugan', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('web_address', models.CharField(blank=True, max_length=200)),
                ('logo', models.ImageField(upload_to='images/company_info')),
                ('facebook_id', models.CharField(blank=True, max_length=200)),
                ('twitter_id', models.CharField(blank=True, max_length=200)),
                ('google_id', models.CharField(blank=True, max_length=200)),
                ('youtube_id', models.CharField(blank=True, max_length=200)),
                ('linkedin_id', models.CharField(blank=True, max_length=200)),
                ('copyright_name', models.CharField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'School Profile',
                'verbose_name_plural': 'School Info',
            },
        ),
    ]
