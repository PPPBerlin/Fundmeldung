# Generated by Django 5.0.6 on 2024-07-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundmeldung', '0007_remove_fundmeldung_einmessungsart'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundmeldung',
            name='einmessungsart',
            field=models.CharField(choices=[('1', 'Schrittmaß'), ('2', 'Bandmaß'), ('3', 'Digitale Kartengrundlage'), ('4', 'Schätzung'), ('5', 'Vermessungsgerät'), ('6', 'HandGPS/Smartphone')], default='3', max_length=1),
        ),
    ]