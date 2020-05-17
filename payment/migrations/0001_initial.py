# Generated by Django 3.0.6 on 2020-05-17 19:28

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.01, max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]