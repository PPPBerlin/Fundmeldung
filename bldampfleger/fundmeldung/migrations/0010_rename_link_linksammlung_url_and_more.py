# Generated by Django 5.0.6 on 2024-07-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundmeldung', '0009_linksammlung_fundmeldung_ergenzunglig_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linksammlung',
            old_name='link',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='linksammlung',
            name='beschreibung',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
