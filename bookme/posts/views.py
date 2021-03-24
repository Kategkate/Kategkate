from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    turn_on_block = False
    # многострочный перенос строки с аргументами
    return render(
        request,
        'index.html',
        {
            'turn_on_block': turn_on_block
        }
    )


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
