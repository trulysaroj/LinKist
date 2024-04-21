from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link


# class-based view
class LinkListView(ListView):
    model = Link


class LinkCreateView(CreateView):
    model = Link
    fields = '__all__'
    success_url = reverse_lazy('link-list')


class LinkUpdateView(UpdateView):
    model = Link
    fields = ['title', 'url']
    success_url = reverse_lazy('link-list')
    # model_form -- same as template link_form.html


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')


def ProfileView(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()

    context = {
        'profile': profile,
        'links': links
    }

    return render(request, 'Linkist/profile.html', context)
