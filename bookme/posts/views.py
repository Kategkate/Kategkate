from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView

from posts.forms import SearchForm, ApartCreateForm
from posts.models import Apartment


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


class ApartListView(ListView):
    template_name = 'apartments/apartment.html'
    paginate_by = 10
    model = Apartment
    context_object_name = 'item_list'

    def get_queryset(self):
        tag = self.request.GET.get('tag', None)
        if tag:
            return super(ApartListView, self).get_queryset().filter(tags__name=tag)
        return super(ApartListView, self).get_queryset()


class ApartDetailView(DetailView):
    """
    This class is for the detailed review of the Apartment.
    """

    template_name = 'apartments/apartment-detail.html'
    model = Apartment
    context_object_name = 'item'


class ApartmentCreateView(CreateView):
    """
    This class is for the creation of the Apartment.
    """

    template_name = 'apartments/apartment-create.html'
    form_class = ApartCreateForm
    success_url = '/apartment'
    model = Apartment


class ApartmentEditView(UpdateView):
    """
    This class is for the searching of the Apartment.
    """

    template_name = 'apartments/apartment-edit.html'
    form_class = SearchForm
    success_url = '/'
    model = Apartment
