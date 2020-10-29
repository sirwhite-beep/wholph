# Generated by Django 3.1.2 on 2020-10-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_christymodel_imomodel_robmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='christymodel',
            name='comment',
            field=models.CharField(choices=[('a', 'Pass'), ('b', 'Fail')], max_length=10),
        ),
        migrations.AlterField(
            model_name='christymodel',
            name='grade',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('f', 'F')], max_length=10),
        ),
        migrations.AlterField(
            model_name='emmamodel',
            name='comment',
            field=models.CharField(choices=[('a', 'Pass'), ('b', 'Fail')], max_length=10),
        ),
        migrations.AlterField(
            model_name='emmamodel',
            name='grade',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('f', 'F')], max_length=10),
        ),
        migrations.AlterField(
            model_name='imomodel',
            name='comment',
            field=models.CharField(choices=[('a', 'Pass'), ('b', 'Fail')], max_length=10),
        ),
        migrations.AlterField(
            model_name='imomodel',
            name='grade',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('f', 'F')], max_length=10),
        ),
        migrations.AlterField(
            model_name='robmodel',
            name='comment',
            field=models.CharField(choices=[('a', 'Pass'), ('b', 'Fail')], max_length=10),
        ),
        migrations.AlterField(
            model_name='robmodel',
            name='grade',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('f', 'F')], max_length=10),
        ),
    ]
