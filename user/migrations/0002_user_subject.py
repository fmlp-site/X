# Generated by Django 2.1.3 on 2019-05-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_auto_20190503_1258'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subject',
            field=models.ManyToManyField(blank=True, related_name='subjects_taught', to='configuration.Subjects'),
        ),
    ]