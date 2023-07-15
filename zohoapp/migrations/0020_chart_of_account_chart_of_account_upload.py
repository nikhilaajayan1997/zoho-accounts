# Generated by Django 4.1.7 on 2023-07-15 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0019_remove_chart_of_account_upload_account_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart_of_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(blank=True, max_length=255, null=True)),
                ('account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('credit_no', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_account', models.CharField(blank=True, max_length=255, null=True)),
                ('parent_account', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_no', models.CharField(blank=True, max_length=255, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('account_code', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('watchlist', models.CharField(blank=True, max_length=255, null=True)),
                ('attachment', models.ImageField(null=True, upload_to='image/')),
                ('create_status', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chart_of_Account_Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(blank=True, max_length=255, null=True)),
                ('account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('document', models.FileField(upload_to='docs/')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.chart_of_account')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
