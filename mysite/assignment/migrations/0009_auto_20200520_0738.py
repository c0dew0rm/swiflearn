# Generated by Django 3.0.6 on 2020-05-20 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0008_auto_20200519_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='className',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_question', to='assignment.Class'),
        ),
    ]
