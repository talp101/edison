from django.views.generic import TemplateView


class AuthUsersView(TemplateView):
    template_name = 'auth_users.html'