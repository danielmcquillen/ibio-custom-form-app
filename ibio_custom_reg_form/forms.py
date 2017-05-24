from .models import ExtraInfo
from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe


# TODO: What restrictions should be placed on Slack username?

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['user_agreement_ibio_study'].error_messages = {
            "required": u"You must agree to participate in the iBiology Courses study.",
            "invalid": u"You must agree in order to participate in iBiology Courses.",
        }

    user_agreement_ibio_study = forms.BooleanField(required=True,
                                                   label=mark_safe('I agree to participate in the iBiology Courses study. <a href="https://courses.ibiology.org/about#study" target="_blank">What\'s this?</a>'))

    class Meta(object):
        model = ExtraInfo
        fields = ('user_agreement_ibio_study',)
