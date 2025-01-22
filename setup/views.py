from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _("Logout realized succefully."))
        return super().dispatch(request, *args, **kwargs)
    