# Generated by Django 4.0.3 on 2023-05-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0002_alter_status_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
