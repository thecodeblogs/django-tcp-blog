# Generated by Django 3.1.2 on 2021-01-24 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0023_auto_20210122_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('session_uid', models.UUIDField(blank=True, null=True)),
                ('telemetry', models.JSONField()),
                ('name', models.TextField()),
                ('family', models.TextField()),
                ('version', models.TextField()),
                ('major', models.IntegerField()),
                ('minor', models.IntegerField()),
                ('patch', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
