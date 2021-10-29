from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class StaffAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is a staff member."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)
