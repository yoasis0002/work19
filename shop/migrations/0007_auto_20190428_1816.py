# Generated by Django 2.2 on 2019-04-28 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-item__id', '-id']},
        ),
    ]
