from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class LogoutMessageMixin:
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _("Logout successful."))
        return super().dispatch(request, *args, **kwargs)
