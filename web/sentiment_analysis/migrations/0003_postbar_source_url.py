# Generated by Django 2.1 on 2018-09-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment_analysis', '0002_auto_20180903_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='postbar',
            name='source_url',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]