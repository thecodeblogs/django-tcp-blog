# Generated by Django 3.1.2 on 2021-01-19 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_auto_20201010_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryenvelope',
            name='entry',
            field=models.JSONField(),
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entry_envelope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.entryenvelope')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.JSONField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
