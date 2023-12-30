# Generated by Django 4.2.7 on 2023-12-30 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('transactions', '0002_alter_transactionmodel_transaction_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyTransferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'Loan Paid'), (5, 'Transfer')], null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers', to='accounts.userbankaccountmodel')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receives', to='accounts.userbankaccountmodel')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
