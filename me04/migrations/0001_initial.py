# Generated by Django 4.1 on 2022-08-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='AD')),
                ('last_name', models.CharField(max_length=30, verbose_name='SOYAD')),
                ('age', models.IntegerField(verbose_name='YAŞ')),
                ('country', models.CharField(choices=[('TR', 'Turkey'), ('US', 'America'), ('DE', 'Germany'), ('FR', 'France')], default='TR', max_length=2, verbose_name='ÜLKE')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Profil fotografı')),
                ('register', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt tarihi')),
            ],
        ),
    ]