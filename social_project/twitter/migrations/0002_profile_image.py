# Generated by Django 3.2 on 2022-05-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
