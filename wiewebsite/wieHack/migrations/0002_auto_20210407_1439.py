# Generated by Django 2.2.3 on 2021-04-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wieHack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domains',
            name='abstract',
            field=models.FileField(default=None, null=True, upload_to='domain_abstracts'),
        ),
    ]