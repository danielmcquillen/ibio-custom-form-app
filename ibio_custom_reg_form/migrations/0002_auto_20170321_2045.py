from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibio_custom_reg_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='slack_username',
            field=models.CharField(default=False, max_length=255, verbose_name=b"Student's Slack username", blank=True),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='user_agreement_ibio_study',
            field=models.BooleanField(default=False, verbose_name=b'User agreement for iBiology Courses Study'),
        ),
    ]
