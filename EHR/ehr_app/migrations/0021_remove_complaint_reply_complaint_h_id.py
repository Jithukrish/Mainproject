# Generated by Django 4.1.7 on 2023-04-13 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ehr_app', '0020_remove_feedback_email_remove_feedback_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='reply',
        ),
        migrations.AddField(
            model_name='complaint',
            name='H_id',
            field=models.ForeignKey(default=79, on_delete=django.db.models.deletion.CASCADE, to='ehr_app.hospital'),
            preserve_default=False,
        ),
    ]
