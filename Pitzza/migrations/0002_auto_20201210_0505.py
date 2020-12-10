# Generated by Django 3.1.4 on 2020-12-10 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pitzza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitzza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PitzzaThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieceIndex', models.IntegerField(verbose_name='piece index')),
                ('pExtras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pitzza.pitzzaextra')),
                ('pitzza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pitzza.pitzza')),
            ],
        ),
        migrations.AddField(
            model_name='pitzza',
            name='pExtras',
            field=models.ManyToManyField(through='Pitzza.PitzzaThrough', to='Pitzza.PitzzaExtra'),
        ),
        migrations.AddField(
            model_name='pitzza',
            name='pType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pitzza.pitzzatype'),
        ),
    ]
