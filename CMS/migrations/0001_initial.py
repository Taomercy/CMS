# Generated by Django 2.2.2 on 2020-07-18 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('illegal_situation', models.TextField()),
                ('commercial_housing_situation', models.TextField()),
                ('rental_status', models.TextField()),
                ('object_class', models.TextField()),
                ('vehicle_condition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appellation', models.TextField()),
                ('name', models.TextField()),
                ('domicile', models.TextField()),
                ('work_units', models.TextField()),
                ('id_number', models.TextField(unique=True)),
                ('income', models.TextField()),
                ('social_security', models.TextField()),
                ('political_landscape', models.TextField()),
                ('health', models.TextField()),
                ('phone_number', models.TextField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CMS.Family')),
            ],
        ),
        migrations.CreateModel(
            name='HandleAffairsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True)),
                ('event', models.TextField()),
                ('agent', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CMS.Person')),
            ],
        ),
    ]
