# Generated by Django 3.1.1 on 2020-10-08 13:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]