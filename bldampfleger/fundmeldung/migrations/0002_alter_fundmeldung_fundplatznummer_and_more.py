# Generated by Django 5.0.6 on 2024-07-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundmeldung', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundmeldung',
            name='fundplatznummer',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fundmeldung',
            name='hausnummer',
            field=models.IntegerField(null=True),
        ),
    ]
