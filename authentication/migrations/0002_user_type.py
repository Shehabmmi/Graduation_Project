# Generated by Django 4.1.1 on 2023-01-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('ST', 'Student'), ('DR', 'Doctor'), ('AD', 'Admin')], default='ST', max_length=2),
        ),
    ]
