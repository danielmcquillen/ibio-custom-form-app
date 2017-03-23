from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibio_custom_reg_form', '0002_auto_20170321_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extrainfo',
            name='slack_username',
        ),
    ]
