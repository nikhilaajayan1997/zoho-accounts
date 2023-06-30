# Generated by Django 4.0.2 on 2023-06-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0015_chart_of_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chart_of_account',
            old_name='Currency',
            new_name='credit_no',
        ),
        migrations.AddField(
            model_name='chart_of_account',
            name='currency',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
