# Generated by Django 3.1.6 on 2021-03-16 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidsignups', '0002_auto_20210316_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raid',
            name='code',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
