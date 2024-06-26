# Generated by Django 5.0.2 on 2024-02-27 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logs', '0002_topic_entry_alter_entry_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='entry',
        ),
        migrations.AddField(
            model_name='entry',
            name='entries',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Logs.entry'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='entry',
            field=models.CharField(max_length=200),
        ),
    ]
