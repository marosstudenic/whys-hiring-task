# Generated by Django 4.1.6 on 2023-02-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonToElasticParser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='content_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]