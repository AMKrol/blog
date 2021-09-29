from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Entry
from .forms import EntryForm


class HomepageView(generic.ListView):
    context_object_name = 'all_posts'
    template_name = 'blog/homepage.html'

    def get_queryset(self):
        return Entry.objects.order_by('-pub_date')[:5]


def get_new_post(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            is_published = form.cleaned_data['is_published']
            q = Entry(title=title, body=body,
                      is_published=is_published, pub_date=timezone.now())
            q.save()
            return HttpResponseRedirect('/blog/')
    else:
        form = EntryForm()
    return render(request, 'blog/entry_form.html', {'form': form})


def edit_post(request, pk=None):
    q = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            is_published = form.cleaned_data['is_published']
            q.title = title
            q.body = body
            q.is_published = is_published
            q.pub_date = timezone.now()
            q.save()
        return HttpResponseRedirect('/blog/')
    else:
        form = EntryForm(initial={
                     'title': q.title,
                     'body': q.body,
                     'is_published': q.is_published})
    return render(request, 'blog/edit_entry.html', {'form': form, 'id': pk})
