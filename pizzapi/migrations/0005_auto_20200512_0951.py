# Generated by Django 3.0.6 on 2020-05-12 09:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pizzapi', '0004_auto_20200512_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
         migrations.RemoveField(
            model_name='order',
            name='UUID',
        ),
        migrations.AddField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
