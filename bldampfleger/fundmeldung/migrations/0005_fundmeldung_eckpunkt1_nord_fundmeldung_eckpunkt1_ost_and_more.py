# Generated by Django 5.0.6 on 2024-07-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundmeldung', '0004_alter_fundmeldung_auffindungsart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundmeldung',
            name='eckpunkt1_nord',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='eckpunkt1_ost',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='eckpunkt2_nord',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='eckpunkt2_ost',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='eckpunkt3_nord',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='eckpunkt3_ost',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='eckpunkt4_nord',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='eckpunkt5_ost',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fundmeldung',
            name='einmessungsart',
            field=models.CharField(max_length=100, null=True),
        ),
    ]