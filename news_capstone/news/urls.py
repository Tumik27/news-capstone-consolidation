from django.urls import path

from .api_views import PublisherArticlesView, JournalistArticlesView

urlpatterns = [
    path("api/publishers/<int:publisher_id>/articles/", PublisherArticlesView.as_view(), name="publisher-articles"),
    path("api/journalists/<int:journalist_id>/articles/", JournalistArticlesView.as_view(), name="journalist-articles"),
]
