# Generated by Django 3.2.9 on 2021-11-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_auto_20211130_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]