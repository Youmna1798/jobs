# Generated by Django 5.0 on 2023-12-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_job_description_alter_newpage_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpage',
            name='apply',
            field=models.CharField(default='', max_length=255),
        ),
    ]