# Generated by Django 4.2.4 on 2023-10-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_teacher_alter_contact_email_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='marksobtained',
            field=models.IntegerField(default=0),
        ),
    ]
