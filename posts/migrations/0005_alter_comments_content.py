# Generated by Django 4.2 on 2023-04-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_postsmodel_content_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=401),
        ),
    ]
