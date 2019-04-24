from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, UpdateView, ListView, \
    CreateView, DeleteView
from pwd_front.models import SiteSettings
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from pwd_front.models import Slider, Blurb, Paragraph, Page
from ..mixins import AjaxableResponseMixin, DeleteMessageMixin


# TODO: Implement a button "backup" in index admin page

class AdminIndex(LoginRequiredMixin, TemplateView):
    """Main view for administrate pwd_front pages."""
    login_url = '/admin/login/'
    # redirect_field_name = 'redirect_to'
    template_name = 'dashboard/front/site-admin.html'


class SiteSettingsUpdate(LoginRequiredMixin, UpdateView):
    template_name = "dashboard/front/form_page.html"
    model = SiteSettings
    fields = ['site_name',
              'company_name',
              'address',
              'phone_number',
              'fax_number',
              'email',
              'ga_analytics',
              'facebook_link',
              'linkedin_link', ]
    extra_context = {'page_name': _('Site preferences'),
                     'menu_pref': True, }

    def get_success_url(self):
        return reverse("dashboard:preferences-update",
                       kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.info(self.request, _('Your settings have been updated.'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request,
                      _('Check your form, something wrong just happened.'))
        return super().form_invalid(form)


# SLIDER


class SliderBaseView(LoginRequiredMixin):
    model = Slider
    extra_context = {'menu_slider': True, }
    fields = ['image', 'title', 'content', 'position', 'is_active']


class SliderListView(SliderBaseView, ListView):
    template_name = "dashboard/front/slider_list.html"


class SliderCreateView(SliderBaseView, AjaxableResponseMixin, CreateView):
    template_name = "dashboard/front/form_page.html"
    success_msg = _("Slider created")
    extra_context = {'page_name': _('New slide'),
                     'menu_slider': True, }
    success_url = reverse_lazy("dashboard:slider-list")


class SliderUpdateView(SliderBaseView, AjaxableResponseMixin, UpdateView):
    """
    Ajaxable view for updating Slider.

    Ajax is used in Slider ListView and allow to change on the fly
    ``is_active`` value.
    """
    template_name = "dashboard/front/form_page.html"
    success_msg = _("Slider updated")
    extra_context = {'page_name': _('Slider update'),
                     'menu_slider': True, }
    success_url = reverse_lazy("dashboard:slider-list")

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            self.fields = ['is_active']
        return super().post(request, *args, **kwargs)

    def delete_url(self):
        return reverse_lazy("dashboard:slider-delete",
                            kwargs={'pk': self.object.pk})


class SliderDeleteView(SliderBaseView, DeleteMessageMixin, DeleteView):
    success_msg = _("Slider deleted")
    success_url = reverse_lazy("dashboard:slider-list")
    extra_context = {'page_name': _('Delete a slider?'),
                     'menu_page': True, }


# BLURBS

class BlurbListView(LoginRequiredMixin, ListView):
    model = Blurb
    template_name = "dashboard/front/blurb_list.html"
    extra_context = {'menu_blurb': True, }


class BlurbCreateView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Blurb
    template_name = "dashboard/front/form_page.html"
    fields = ['la_icon', 'title', 'description', 'is_active']
    success_msg = _("Blurb created")
    success_url = reverse_lazy("dashboard:blurb-list")
    extra_context = {'page_name': _('New blurb'),
                     'menu_blurb': True, }


class BlurbUpdateView(LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Blurb
    template_name = "dashboard/front/form_page.html"
    fields = ['la_icon', 'title', 'description', 'is_active']
    success_msg = _("Blurb updated")
    extra_context = {'page_name': _('Blurb update'),
                     'menu_blurb': True}
    success_url = reverse_lazy("dashboard:blurb-list")

    def delete_url(self):
        return reverse_lazy("dashboard:blurb-delete",
                            kwargs={'pk': self.object.pk})


class BlurbDeleteView(LoginRequiredMixin, DeleteMessageMixin, DeleteView):
    model = Blurb
    success_msg = _("Blurb deleted")
    success_url = reverse_lazy("dashboard:blurb-list")
    extra_context = {'page_name': _('Delete a blurb?'),
                     'menu_blurb': True, }


# CONTENTS

class ContentListView(LoginRequiredMixin, AjaxableResponseMixin, ListView):
    model = Paragraph
    template_name = "dashboard/front/content_list.html"
    extra_context = {'page_name': _('Content list'),
                     'content_menu': True, }


class ContentCreateView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Paragraph
    template_name = "dashboard/front/form_page.html"
    fields = ['name', 'content', 'position']
    success_msg = _("Content created")
    success_url = reverse_lazy("dashboard:content-list")
    extra_context = {'page_name': _('New content'),
                     'content_menu': True, }


class ContentUpdateView(LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Paragraph
    template_name = "dashboard/front/form_page.html"
    fields = ['name', 'content', 'is_active', 'position']
    success_msg = _("Content updated")
    success_url = reverse_lazy("dashboard:content-list")
    extra_context = {'page_name': _('Content update'),
                     'content_menu': True, }

    def delete_url(self):
        return reverse_lazy("dashboard:content-delete",
                            kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            self.fields = ['is_active']
        return super().post(request, *args, **kwargs)


class ContentDeleteView(LoginRequiredMixin, DeleteMessageMixin, DeleteView):
    model = Paragraph
    template_name = "dashboard/front/form_page.html"
    success_msg = _("Content deleted")
    success_url = reverse_lazy("dashboard:content-list")
    extra_context = {'page_name': _('Delete a content?'),
                     'content_menu': True, }


# PAGES

class PageListView(LoginRequiredMixin, ListView):
    model = Page
    template_name = "dashboard/front/page_list.html"
    extra_context = {'menu_page': True, }


class PageUpdateView(LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Page
    template_name = "dashboard/front/form_page.html"
    fields = ['title', 'description', 'keywords', 'paragraphs', 'blurbs']
    success_msg = _("Page updated")
    success_url = reverse_lazy("dashboard:page-list")
    extra_context = {'page_name': _('Page update'),
                     'menu_page': True, }
