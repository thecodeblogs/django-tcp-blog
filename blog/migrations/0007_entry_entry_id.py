# Generated by Django 3.0.3 on 2020-03-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entry_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
