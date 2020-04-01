# Generated by Django 3.0.3 on 2020-03-30 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_auto_20200330_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myschoolprofil',
            name='myschool',
        ),
        migrations.AddField(
            model_name='myschoolprofil',
            name='myschool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MySchoolUser_set', to='Backend.MySchoolUser'),
        ),
    ]
