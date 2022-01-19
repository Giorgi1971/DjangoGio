# Generated by Django 3.2.8 on 2021-10-27 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_alter_author_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('created_date', models.DateField(auto_now=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.author')),
            ],
        ),
        migrations.CreateModel(
            name='CroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ManyToManyField(to='group.Group')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.author')),
            ],
        ),
    ]