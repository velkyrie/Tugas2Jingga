# Generated by Django 4.1 on 2022-09-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_task_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.TextField(),
        ),
    ]
