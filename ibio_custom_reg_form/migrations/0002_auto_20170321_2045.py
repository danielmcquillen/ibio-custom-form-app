from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibio_custom_reg_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_agreement_ibio_study',
            field=models.BooleanField(default=False, verbose_name=b'User agreement for iBiology Courses Study'),
        ),
    ]
