# Generated by Django 2.1.3 on 2018-12-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=None, max_length=40, verbose_name='Author'),
            preserve_default=False,
        ),
    ]
