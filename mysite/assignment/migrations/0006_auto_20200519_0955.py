# Generated by Django 3.0.6 on 2020-05-19 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0005_auto_20200518_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtaken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.UserProfile'),
        ),
    ]
