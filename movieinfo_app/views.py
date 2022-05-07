from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from movieinfo_app.models import Actor


class ActorList(LoginRequiredMixin, PermissionRequiredMixin, View):
    page_kwarg = 'page'
    paginate_by = 2  # 25 instructors per page
    template_name = 'movieinfo_app/actor_list.html'
    permission_required = 'movieinfo_app.view_actor'

    def get(self, request):
        actors = Actor.objects.all()
        paginator = Paginator(
            actors,
            self.paginate_by
        )
        page_number = request.GET.get(
            self.page_kwarg
        )
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'actor_list': page,
        }
        return render(
            request, self.template_name, context)



