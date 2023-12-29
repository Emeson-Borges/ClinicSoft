# Generated by Django 5.0 on 2023-12-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("dt_nascimento", models.DateField()),
                ("rua", models.CharField(max_length=255)),
                ("telefone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("numero", models.CharField(max_length=10)),
                ("bairro", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("rg", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "Paciente",
                "verbose_name_plural": "Pacientes",
                "db_table": "pacientes",
                "managed": True,
            },
        ),
    ]