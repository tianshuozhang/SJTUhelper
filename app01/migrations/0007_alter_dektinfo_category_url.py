# Generated by Django 4.2.5 on 2023-10-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0006_alter_dektinfo_category_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dektinfo",
            name="category_url",
            field=models.TextField(),
        ),
    ]
