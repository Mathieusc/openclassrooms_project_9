# Generated by Django 3.2.11 on 2022-02-28 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20220215_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.ticket'),
        ),
    ]
