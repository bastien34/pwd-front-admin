from django.urls import path
from . import views


urlpatterns = [
    # Admin index
    path("", views.AdminIndex.as_view(
        template_name="dashboard/front/site-admin.html"), name="index"),

    path("preferences/<int:pk>/", views.SiteSettingsUpdate.as_view(),
         name="preferences-update"),
    path("slider-list/", views.SliderListView.as_view(), name="slider-list"),
    path("blurb-list/", views.BlurbListView.as_view(), name="blurb-list"),
    path("page-list/", views.PageListView.as_view(), name="page-list"),
    path("content-list/", views.ContentListView.as_view(), name="content-list"),

    # Update Views
    path("slider-update/<int:pk>/", views.SliderUpdateView.as_view(), name="slider-update"),
    path("blurb-update/<int:pk>/", views.BlurbUpdateView.as_view(), name="blurb-update"),
    path("page-update/<int:pk>/", views.PageUpdateView.as_view(), name="page-update"),
    path("content-update/<int:pk>/", views.ContentUpdateView.as_view(), name="content-update"),

    # Delete Views
    path("slider-delete/<int:pk>/", views.SliderDeleteView.as_view(), name="slider-delete"),
    path("blurb-delete/<int:pk>/", views.BlurbDeleteView.as_view(), name="blurb-delete"),
    path("content-delete/<int:pk>/", views.ContentDeleteView.as_view(), name="content-delete"),

    # Create Views
    path("slider-create/", views.SliderCreateView.as_view(), name="slider-create"),
    path("blurb-create/", views.BlurbCreateView.as_view(), name="blurb-create"),
    path("content-create/", views.ContentCreateView.as_view(), name="content-create"),
]
