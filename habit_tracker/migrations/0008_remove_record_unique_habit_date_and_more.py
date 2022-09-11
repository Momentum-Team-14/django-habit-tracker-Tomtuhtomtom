# Generated by Django 4.1 on 2022-09-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0007_remove_record_unique_user_date_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='record',
            name='unique_habit_date',
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('entry_date', 'habit'), name='unique_habit_date'),
        ),
    ]
