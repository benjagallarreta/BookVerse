# Generated by Django 5.0.6 on 2024-06-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0006_usuario_foto_perfil_alter_libro_editorial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]