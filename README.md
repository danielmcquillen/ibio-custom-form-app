# Based on OpenCraft's Custom Form App
# https://github.com/open-craft/custom-form-app

# This custom form Django App adds a few fields to the signup form that we need for iBiology Courses.
# Right now this means:
#   1. A checkbox to agree to iBiology Courses terms
*   2. A Slack user ID, so we can use the API to manage student's access to Slack channel

# To Use:

1. Install with `pip -e .` within this folder within the edx platform virtual environment.
2. Add "ibio_custom_reg_form" to the "ADDL_INSTALLED_APPS" array in `lms.env.json` (you may have to create it if it doesn't exist.)
3. Set "REGISTRATION_EXTENSION_FORM" to "ibio_custom_reg_form.forms.ExtraInfoForm" in `lms.env.json`.
4. Run migrations.
5. Start/restart the LMS.
