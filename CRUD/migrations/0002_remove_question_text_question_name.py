# Generated by Django 4.0.4 on 2022-04-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(default='noname', max_length=100),
            preserve_default=False,
        ),
    ]
