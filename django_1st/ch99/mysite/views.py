from django.views.generic import TemplateView

#---- Related User Authenticatio
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin

#---- Template View
class HomeView(TemplateView) :
    template_name = 'home.html'

class UserCreateView(CreateView) :
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreationDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "만든 새끼 아니면 꺼져라."

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner :
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
