# Generated by Django 3.0.3 on 2020-10-09 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_profile_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]