# Generated by Django 3.2.8 on 2021-10-28 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_author_image'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='group.group')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.author')),
            ],
        ),
        migrations.DeleteModel(
            name='CroupMember',
        ),
    ]