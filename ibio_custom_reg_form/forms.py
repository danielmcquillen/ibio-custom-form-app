from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['user_agreement_ibio_study'].error_messages = {
            "required": u"I agree to participate in the iBiology Courses study.",
            "invalid": u"You must agree in order to participate in iBiology Courses.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('user_agreement_ibio_study',)
