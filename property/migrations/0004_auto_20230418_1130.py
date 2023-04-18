# Generated by Django 2.2.24 on 2023-04-18 08:30

from django.db import migrations


PIVOTAL_YEAR = 2015


# def fill_new_building_with_construction_year(apps, schema_editor):
#     Flat = apps.get_model('property', 'Flat')
#     for flat in Flat.objects.all():
#         if flat.construction_year is not None:
#             flat.new_building = (flat.construction_year >= PIVOTAL_YEAR)
#             flat.save()

def fill_new_building_with_construction_year(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=PIVOTAL_YEAR).update(new_building=True)
    Flat.objects.filter(construction_year__lt=PIVOTAL_YEAR).update(new_building=False)


def clear_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_with_construction_year, clear_new_building),
    ]
