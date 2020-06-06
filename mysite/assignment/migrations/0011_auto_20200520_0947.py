# Generated by Django 3.0.6 on 2020-05-20 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0010_auto_20200520_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtaken',
            name='classTaken',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_info', to='assignment.Class'),
        ),
        migrations.AlterField(
            model_name='classtaken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_student_class', to='assignment.UserProfile'),
        ),
    ]