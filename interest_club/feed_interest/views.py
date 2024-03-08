from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import JsonResponse
from django.db.models import Q
from .models import Interest_Group, GroupPost


def index(request):
    """Выводит все группы и их посты"""
    feed = Interest_Group.objects.all()
    groups = Interest_Group.objects.all()
    group = GroupPost.objects.filter(group__in=groups).order_by("-created_at")
    context = {
        "feeds": feed,
        "group": group
    }
    return render(request, 'feed_interest/index.html', context)


class SearchResultsView(ListView):
    """Поиск по названию группы"""
    model = Interest_Group
    context_object_name = 'groups'
    template_name = 'feed_interest/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Interest_Group.objects.filter(group_name__icontains=query)
        else:
            return Interest_Group.objects.all()


class PostDetailView(DetailView, LoginRequiredMixin):
    """Показываем посты в группе"""
    model = Interest_Group
    template_name = 'feed_interest/group_inside.html'
    context_object_name = 'group_post'
    raise_exception = True

    def get_queryset(self):
        group_id = self.kwargs['pk']
        return Interest_Group.objects.filter(pk=group_id)
