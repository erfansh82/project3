# Generated by Django 3.2 on 2023-04-18 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('days', models.IntegerField(default=0)),
                ('minimum_winrate', models.IntegerField(default=0)),
                ('maximum_winrate', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('forex_signal_limit', models.IntegerField(default=0)),
                ('crypto_signal_limit', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default='show', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ActivePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broker_referral', models.TextField()),
                ('choose_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premiumplan.createplan')),
            ],
        ),
    ]
