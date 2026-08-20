from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_v2", "0034_item_cost_and_time_of_day"),
    ]

   operations = [
        migrations.CreateModel(
            name="AbilityProsePast",
             fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("effect", models.CharField(max_length=6000)),
                ("short_effect", models.CharField(max_length=300)),
                (
                    "ability",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="abilityprosepast",
                        to="pokemon_v2.Ability",
                    ),
                ),
                (
                    "generation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="abilityprosepast",
                        to="pokemon_v2.Generation",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="abilityprosepast_language",
                        to="pokemon_v2.language",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

