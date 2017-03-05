from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.utils import timezone
from urllib.parse import quote_plus
from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_detail(request, slug=None):  # retrieve
    instance = get_object_or_404(Post, slug=slug)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string
    }
    return render(request, "post_detail.html", context)


def index(request):  # list items

    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page

    # page = request.GET.get('page')
    # try:
    #     queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     queryset = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     queryset = paginator.page(paginator.num_pages)
    context = {
        "obj_list": queryset_list,
        "title": "List",
    }
    return render(request, "index.html", context)


def post_list(request):  # list items
    queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "obj_list": queryset,
        "title": "List",
    }
    return render(request, "post_list.html", context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=slug)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("posts:list")
