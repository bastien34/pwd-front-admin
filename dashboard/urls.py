from django.urls import path, include
from .front.views import AdminIndex
from .front.urls import urlpatterns as front_admin_urls


app_name = "dashboard"

urlpatterns = [

    # Dashboard should be change to a dashboard core view index page
    path("", AdminIndex.as_view(
        template_name="dashboard/front/site-admin.html"), name="index"),
    path("front/", include(front_admin_urls)),

]
