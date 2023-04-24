# Generated by Django 4.1.7 on 2023-03-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehr_app', '0003_doctor_lattitude_doctor_logitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='lattitude',
            field=models.FloatField(default=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='logitude',
            field=models.FloatField(default=6),
            preserve_default=False,
        ),
    ]
