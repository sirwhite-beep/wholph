# Generated by Django 3.1.2 on 2020-10-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20201029_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='christymodel',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=10),
        ),
        migrations.AlterField(
            model_name='emmamodel',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=10),
        ),
        migrations.AlterField(
            model_name='imomodel',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=10),
        ),
        migrations.AlterField(
            model_name='robmodel',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=10),
        ),
    ]
