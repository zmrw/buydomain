# Generated by Django 2.2 on 2021-11-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='域名类型')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255, verbose_name='域名')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('expired_date', models.DateTimeField(blank=True, null=True, verbose_name='域名释放时间')),
                ('register_date', models.DateTimeField(blank=True, null=True, verbose_name='域名注册时间')),
                ('domain_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='domain.DomainType', verbose_name='域名后缀')),
            ],
            options={
                'verbose_name': '域名',
                'verbose_name_plural': '域名',
            },
        ),
    ]
