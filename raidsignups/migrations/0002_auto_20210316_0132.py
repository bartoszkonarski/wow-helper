# Generated by Django 3.1.6 on 2021-03-16 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidsignups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raider',
            name='playerclass',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raider',
            name='playerspec',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
