from django.urls import path
from .views import (AdminIndex,
                    SiteSettingsUpdate,
                    SliderListView,
                    BlurbListView,
                    PageListView,
                    ContentListView,
                    SliderUpdateView,
                    BlurbUpdateView,
                    ContentUpdateView,
                    PageUpdateView,
                    SliderCreateView,
                    BlurbCreateView,
                    ContentCreateView,
                    SliderDeleteView,
                    BlurbDeleteView,
                    ContentDeleteView,
                    )

app_name = 'pwd_front_admin'

urlpatterns = [
    # Admin Urls
    path("", AdminIndex.as_view(
        template_name="site_admin/admin/site-admin.html"), name="site-admin"),

    path("preferences/<int:pk>/", SiteSettingsUpdate.as_view(),
         name="preferences-update"),
    path("slider-list/", SliderListView.as_view(), name="slider-list"),
    path("blurb-list/", BlurbListView.as_view(), name="blurb-list"),
    path("page-list/", PageListView.as_view(), name="page-list"),
    path("content-list/", ContentListView.as_view(), name="content-list"),

    # Update Views
    path("slider-update/<int:pk>/", SliderUpdateView.as_view(), name="slider-update"),
    path("blurb-update/<int:pk>/", BlurbUpdateView.as_view(), name="blurb-update"),
    path("page-update/<int:pk>/", PageUpdateView.as_view(), name="page-update"),
    path("content-update/<int:pk>/", ContentUpdateView.as_view(), name="content-update"),

    # Delete Views
    path("slider-delete/<int:pk>/", SliderDeleteView.as_view(), name="slider-delete"),
    path("blurb-delete/<int:pk>/", BlurbDeleteView.as_view(), name="blurb-delete"),
    path("content-delete/<int:pk>/", ContentDeleteView.as_view(), name="content-delete"),

    # Create Views
    path("slider-create/", SliderCreateView.as_view(), name="slider-create"),
    path("blurb-create/", BlurbCreateView.as_view(), name="blurb-create"),
    path("content-create/", ContentCreateView.as_view(), name="content-create"),
]
