# Generated by Django 3.1.1 on 2020-11-27 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0016_auto_20201126_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='institution',
            field=models.CharField(db_index=True, help_text='Institution visited', max_length=250, null=True),
        ),
    ]
