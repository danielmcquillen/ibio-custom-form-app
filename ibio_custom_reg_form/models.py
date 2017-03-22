from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains an extra field that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)

    user_agreement_ibio_study = models.BooleanField(
        verbose_name="User agreement for iBiology Courses Study",
        default=False,
        blank=False
    )

    slack_username = models.CharField(
        verbose_name="Student's Slack username",
        default=False,
        blank=True,
        max_length=255
    )

