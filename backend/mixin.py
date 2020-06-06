import base64

from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import get_template
from django.utils.translation import gettext_lazy as _


class TokenPackerMixin():

    def packing(self, token_code, email):
        auth_pack = token_code + '#' + email
        token = base64.b64encode(auth_pack.encode()).decode('ascii')
        return token

    def unpacking(self, token):
        auth_pack = base64.b64decode(token).decode()
        token_code = auth_pack.split('#')[0]
        email = auth_pack.split('#')[1]
        return token_code, email


class SendMailMixin(TokenPackerMixin, PasswordResetTokenGenerator):

    def make_subject_and_message(self, type, base_url, token):
        if type == 'regist':
            subject = _('[日本語８] Member registration confirmation mail')
            message = get_template('backend/email/regist_template.html').render(
                {
                    'base_url': base_url + 'active',
                    'token': token
                }
            )
        elif type == 'reset':
            subject = _('[日本語８] Password Initialization Mail')
            message = get_template('backend/email/reset_template.html').render(
                {
                    'base_url': base_url + 'reset_password',
                    'token': token
                }
            )
        return subject, message

    def get_base_url(self, request):
        scheme = request.is_secure() and "https" or "http"
        host = get_current_site(request)
        base_url = '{}://{}/'.format(scheme, host)
        return base_url

    def send_mail(self, request, user, type):
        base_url = self.get_base_url(request)
        token_code = super().make_token(user)
        token = super().packing(token_code, user.email)
        subject, message = self.make_subject_and_message(type, base_url, token)
        from_email = settings.EMAIL_HOST_EMAIL
        recipient_list = [user.email]
        send_mail(subject, None, from_email, recipient_list, False, None, None, None, message)


class LoginSuccessTxtMixin():

    def makeText(self, type):
        if type == 'active':
            return _('Your account has been activated.'), _('Please log in and use the service.')
        elif type == 'regist':
            return _('Membership has been completed.'), _('Please verify your e-mail and give your identity.')
        elif type == 'regist_password':
            return _('Your password has been changed!'), _('Please log in and use the service.')
        elif type == 'reset':
            return _('We have sent you a password reset mail!'), _('Please check your email and change your password.')
        elif type == 'non_active':
            return _('Your account cannot be activated.'), _('Please sign up again and authenticate yourself.')
        return None, None