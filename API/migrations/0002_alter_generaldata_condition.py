# Generated by Django 4.2 on 2023-04-17 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaldata',
            name='condition',
            field=models.ImageField(upload_to=''),
        ),
    ]