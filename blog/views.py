from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


from .models import Entry
from .forms import EntryForm, LoginForm


class HomepageView(generic.ListView):
    context_object_name = 'all_posts'
    template_name = 'blog/homepage.html'

    def get_queryset(self):
        return Entry.objects.order_by('-pub_date')[:5]


@permission_required('blog.add_entry', login_url='/blog/login/')
def get_new_post(request):
    if request.method == 'POST':
        user = request.session['user']
        print(user)
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            is_published = form.cleaned_data['is_published']
            q = Entry(title=title, body=body,
                      is_published=is_published,
                      pub_date=timezone.now(), created_by=request.session['user'])
            q.save()
            return HttpResponseRedirect('/blog/')
    else:
        form = EntryForm()
    return render(request, 'blog/entry_form.html', {'form': form})


@permission_required('blog.change_entry', login_url='/blog/login/')
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


@permission_required('blog.delete_entry', login_url='/blog/login/')
def delete_post(request):
    if request.method == 'POST':
        id = request.POST['post_id']
        q = get_object_or_404(Entry, id=id)
        q.delete()
        return HttpResponseRedirect('/blog/')


def login_view(request):
    form = LoginForm()
    errors = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            request.session['user'] = username
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/blog/')
            else:
                errors = form.errors
    return render(request, "blog/login_form.html",
                  {'form': form, 'errors': errors})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/blog/')
