"""
Serializers for the News application.

This module defines serializers used to transform Article model
instances into JSON representations and validate incoming data.
"""

from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for the Article model."""

    publisher = serializers.StringRelatedField()
    journalist = serializers.StringRelatedField()

    class Meta:
        """Metadata options for ArticleSerializer."""

        model = Article
        fields = [
            "id",
            "title",
            "content",
            "approved",
            "publisher",
            "journalist",
            "created_at",
        ]
