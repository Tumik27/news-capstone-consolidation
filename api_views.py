from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer


class PublisherArticlesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, publisher_id: int):
        # Only return approved articles
        qs = Article.objects.filter(publisher_id=publisher_id, approved=True).order_by("-created_at")
        return Response(ArticleSerializer(qs, many=True).data)


class JournalistArticlesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, journalist_id: int):
        # Only return approved articles
        qs = Article.objects.filter(journalist_id=journalist_id, approved=True).order_by("-created_at")
        return Response(ArticleSerializer(qs, many=True).data)
