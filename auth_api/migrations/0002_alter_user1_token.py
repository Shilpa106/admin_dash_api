# Generated by Django 3.2.7 on 2021-09-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='token',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
