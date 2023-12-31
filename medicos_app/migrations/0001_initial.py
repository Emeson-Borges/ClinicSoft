# Generated by Django 5.0 on 2023-12-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Medicos",
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
                ("crm", models.CharField(max_length=20, unique=True)),
                ("telefone", models.CharField(max_length=15)),
                ("cbo", models.CharField(max_length=10)),
                ("especializacao", models.CharField(max_length=255)),
                ("setor_id", models.IntegerField()),
            ],
            options={
                "verbose_name": "Medico",
                "verbose_name_plural": "Medicos",
                "db_table": "medicos",
                "managed": True,
            },
        ),
    ]
