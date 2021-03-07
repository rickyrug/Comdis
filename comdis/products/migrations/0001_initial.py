# Generated by Django 3.1.7 on 2021-03-07 20:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20210307_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Created', models.DateTimeField(default=django.utils.timezone.now)),
                ('CreatedBy', models.CharField(default='SERVER', max_length=50)),
                ('Updated', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('UpdatedBy', models.CharField(default='SERVER', max_length=50, null=True)),
                ('Classification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.classification')),
                ('Uom', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.uom')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]