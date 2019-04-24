from django.http import JsonResponse
from django.contrib import messages


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form, delete_url to view.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    @property
    def success_msg(self):
        return NotImplemented

    @property
    def delete_url(self):
        return

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            messages.success(self.request, self.success_msg)
            return response

    def get(self, request, *args, **kwargs):
        self.extra_context.update(
            {'delete_url': self.delete_url})
        response = super().get(request, *args, **kwargs)
        return response


class DeleteMessageMixin:
    """
    Mixin to add messages to DeleteView.
    """

    template_name = "site_admin/admin/object_confirm_delete.html"

    @property
    def success_msg(self):
        return NotImplemented

    def get_success_url(self):
        response = super().get_success_url()
        messages.success(self.request, self.success_msg)
        return response
