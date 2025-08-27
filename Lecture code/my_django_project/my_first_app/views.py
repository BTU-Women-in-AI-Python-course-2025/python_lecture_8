from django.http import HttpResponse
from django.views import View


def home(request):
    return HttpResponse("Welcome to the Home Page!")

def not_found(request):
    return HttpResponse("404!")


class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")


class NotFoundView(View):
    def get(self, request):
        return HttpResponse("404!")
