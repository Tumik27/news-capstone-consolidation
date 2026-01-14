from django.urls import path
from .api_views import PublisherArticlesView, JournalistArticlesView
from .views import home

urlpatterns = [
    path("", home, name="home"),

    path(
        "api/publishers/<int:publisher_id>/articles/",
        PublisherArticlesView.as_view(),
        name="publisher-articles",
    ),
    path(
        "api/journalists/<int:journalist_id>/articles/",
        JournalistArticlesView.as_view(),
        name="journalist-articles",
    ),
]
