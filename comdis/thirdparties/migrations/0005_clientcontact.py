# Generated by Django 3.1.7 on 2021-03-09 03:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('thirdparties', '0004_auto_20210308_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=25)),
                ('Created', models.DateTimeField(default=django.utils.timezone.now)),
                ('CreatedBy', models.CharField(default='SERVER', max_length=50)),
                ('Updated', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('UpdatedBy', models.CharField(default='SERVER', max_length=50, null=True)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='thirdparties.client')),
            ],
            options={
                'db_table': 'ClientContact',
            },
        ),
    ]