# Generated by Django 5.1 on 2024-08-28 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_alter_group_number1_alter_group_number2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='number4',
        ),
    ]
