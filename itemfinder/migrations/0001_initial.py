# Generated by Django 3.1.1 on 2020-09-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('source', models.CharField(choices=[('Raid', 'Raid'), ('Dungeon', 'Dungeon')], max_length=7)),
                ('source_name', models.CharField(max_length=25)),
                ('strength', models.BooleanField()),
                ('agility', models.BooleanField()),
                ('intelect', models.BooleanField()),
                ('haste', models.IntegerField()),
                ('crit', models.IntegerField()),
                ('vers', models.IntegerField()),
                ('mastery', models.IntegerField()),
                ('image_url', models.CharField(max_length=250)),
                ('wowhead_url', models.CharField(max_length=250)),
            ],
        ),
    ]
