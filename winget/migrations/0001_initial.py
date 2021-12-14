# Generated by Django 3.2.10 on 2021-12-14 08:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(help_text='Unique identifier for the package (e.g. XP9KHM4BK9FZ7Q).', max_length=128)),
                ('name', models.CharField(help_text='Package name (e.g. Visual Studio Code).', max_length=256, validators=[django.core.validators.MinLengthValidator(2)])),
                ('publisher', models.CharField(help_text='Package publisher (eg. Microsoft Corporation)', max_length=256, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(help_text='Package description (e.g. "Free code editor.")', max_length=256, validators=[django.core.validators.MinLengthValidator(3)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant')),
            ],
            options={
                'unique_together': {('tenant', 'identifier')},
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, help_text="The package's version (eg. 1.2.3.4).", max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winget.package')),
            ],
            options={
                'unique_together': {('package', 'version')},
            },
        ),
        migrations.CreateModel(
            name='Installer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('architecture', models.CharField(choices=[('x86', 'x86'), ('x64', 'x64'), ('arm', 'arm'), ('arm64', 'arm64')], max_length=5)),
                ('type', models.CharField(choices=[('msix', 'msix'), ('msi', 'msi'), ('appx', 'appx'), ('exe', 'exe'), ('zip', 'zip'), ('inno', 'inno'), ('nullsoft', 'nullsoft'), ('wix', 'wix'), ('burn', 'burn'), ('pwa', 'pwa'), ('msstore', 'msstore')], max_length=8)),
                ('file', models.FileField(upload_to='')),
                ('sha256', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator('^[a-fA-F0-9]{64}$')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winget.version')),
            ],
            options={
                'unique_together': {('version', 'architecture', 'type')},
            },
        ),
    ]
