# Generated by Django 5.0.6 on 2024-06-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0004_alter_libro_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
