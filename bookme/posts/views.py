from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView


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


class ExperienceView(TemplateView):
    """
    This class is for the creation of the Experience Object.
    """
    template_name = 'experience.html'


class NewsroomView(TemplateView):
    """
    This class is for the creation of the News Object.
    """
    template_name = 'newsroom.html'
