# Generated by Django 3.1.1 on 2020-11-21 19:15

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations
from django.contrib.postgres.search import SearchVector


def update_full_search(apps, schema_editor):
    model = apps.get_model('visitors', 'Visitor')
    model.objects.update(
        full_search=SearchVector(
            'full_name', 'id_number', 'host_name', 'institution',
            'entity', 'reason', 'office', 'meeting_place', 'host_title',
            'location'
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0012_developer_avatar_image_name'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='visitor',
            name='full_name_dni_host_name_idx',
        ),
        migrations.AddField(
            model_name='visitor',
            name='full_search',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='visitor',
            index=django.contrib.postgres.indexes.GinIndex(fields=['full_search'], name='full_search_idx'),
        ),
        migrations.RunPython(
            update_full_search, reverse_code=migrations.RunPython.noop
        ),
    ]
