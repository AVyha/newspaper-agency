# Generated by Django 4.1.3 on 2022-11-11 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_redactor_workplace'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='redactor',
            options={'ordering': ['-years_of_experience']},
        ),
    ]