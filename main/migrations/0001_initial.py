# Generated by Django 4.0.2 on 2023-01-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=1500)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
