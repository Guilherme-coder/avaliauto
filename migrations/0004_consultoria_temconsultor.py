# Generated by Django 3.2.3 on 2021-08-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliauto', '0003_consultoria_modeloveiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultoria',
            name='temConsultor',
            field=models.CharField(default='N', max_length=1),
            preserve_default=False,
        ),
    ]
