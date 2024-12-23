# Generated by Django 5.0.6 on 2024-07-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundmeldung', '0008_fundmeldung_einmessungsart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linksammlung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('link', models.URLField()),
                ('beschreibung', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='ergenzungLiG',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fundmeldung',
            name='bodenart',
            field=models.CharField(choices=[('1', 'Sand'), ('2', 'Lehm'), ('3', 'Ton'), ('4', 'Mergel'), ('5', 'lehmiger Sand'), ('6', 'Torf')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='fundmeldung',
            name='gelaendenutzung',
            field=models.CharField(choices=[('1', 'Straße/Weg/Platz'), ('2', 'Acker'), ('3', 'Garten'), ('4', 'Grube'), ('5', 'Wiese'), ('6', 'bebautes Grundstück'), ('7', 'Ödland'), ('8', 'Wald'), ('9', 'Moor'), ('10', 'Gewässer')], default='2', max_length=2),
        ),
        migrations.AlterField(
            model_name='fundmeldung',
            name='lageimgelaende',
            field=models.CharField(choices=[('1', 'Höhenlage'), ('2', 'Niederung'), ('3', 'Hang (abfallend nach ...)'), ('4', 'Ebene'), ('5', 'am See/Fluss...'), ('6', 'im See/Fluss')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='fundmeldung',
            name='lagezumortskern',
            field=models.CharField(choices=[('1', 'nördlich'), ('2', 'östlich'), ('3', 'südlich'), ('4', 'westlich'), ('5', 'nordöstlich'), ('6', 'südöstlich'), ('7', 'südwestlich'), ('8', 'nordwestlich')], default='1', max_length=1),
        ),
    ]
