# Generated by Django 4.2.1 on 2023-05-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("realstate", "0002_biensimmobilier_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="biensimmobilier",
            name="prix",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=99999, null=True
            ),
        ),
    ]
