# Generated by Django 4.0.1 on 2022-02-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='NO SNIPPET HERE!', max_length=200),
        ),
    ]