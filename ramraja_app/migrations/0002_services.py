# Generated by Django 2.2 on 2021-01-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramraja_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('logo', models.ImageField(upload_to='')),
                ('head', models.CharField(max_length=50)),
                ('discripation', models.CharField(max_length=50)),
            ],
        ),
    ]
