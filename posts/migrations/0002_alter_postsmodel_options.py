# Generated by Django 4.2 on 2023-04-09 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postsmodel',
            options={'ordering': ('-created_at',)},
        ),
    ]
