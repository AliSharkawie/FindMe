# Generated by Django 5.0.4 on 2024-05-10 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('found', '0003_alter_foundperson_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundperson',
            name='address',
            field=models.CharField(blank=True, default='egypt', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='foundperson',
            name='finder_name',
            field=models.CharField(default='ali', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='foundperson',
            name='name',
            field=models.CharField(blank=True, default='empty', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='foundperson',
            name='phone_number',
            field=models.CharField(default='empty', max_length=100, null=True),
        ),
    ]
