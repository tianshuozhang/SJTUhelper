# Generated by Django 4.2.3 on 2023-08-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_department_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='data',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]
