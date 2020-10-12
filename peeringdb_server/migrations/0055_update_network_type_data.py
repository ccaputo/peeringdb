# Generated by Django 2.2.16 on 2020-10-12 17:21

from django.db import migrations, models

def update_info_types(apps, schema_editor):
    Network = apps.get_model("peeringdb_server", "Network")
    
    for network in Network.handleref.all():
        if "route server" in network.name.lower():
            network.info_type = "Route Server"
        elif "route collector" in network.name.lower():
            network.info_type = "Route Collector"
        else:
            continue

        if network.status == "deleted":
            updated = network._meta.get_field("updated")
            updated.auto_now = False

        network.save()
        updated.auto_now = True


def unset_info_types(apps, schema_editor):
    Network = apps.get_model("peeringdb_server", "Network")
    
    for network in Network.handleref.all():
        if "route server" in network.name.lower():
            network.info_type = ""
        elif "route collector" in network.name.lower():
            network.info_type = ""
        else:
            continue

        if network.status == "deleted":
            updated = network._meta.get_field("updated")
            updated.auto_now = False

        network.save()
        updated.auto_now = True

class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb_server', '0054_add_network_types_and_prefix_description'),
    ]

    operations = [
        migrations.RunPython(update_info_types, unset_info_types)
    ]
