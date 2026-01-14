"""
Database models for the News application.

This module defines the core data models used in the system,
including users, publishers, and articles.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Publisher(models.Model):
    """Represents a news publisher or media house."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        """Return the publisher name as its string representation."""
        return self.name


class User(AbstractUser):
    """
    Custom user model with role-based behaviour.

    Users can be readers, editors, or journalists, each with
    different responsibilities and permissions within the system.
    """

    class Role(models.TextChoices):
        """Defines the available roles for users."""

        READER = "READER", "Reader"
        EDITOR = "EDITOR", "Editor"
        JOURNALIST = "JOURNALIST", "Journalist"

    role = models.CharField(max_length=20, choices=Role.choices)

    # Reader fields: subscriptions to publishers and journalists
    subscribed_publishers = models.ManyToManyField(
        Publisher,
        blank=True,
        related_name="subscribers",
    )
    subscribed_journalists = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="journalist_subscribers",
    )

    # Journalist fields: independent publications
    independent_articles = models.ManyToManyField(
        "Article",
        blank=True,
        related_name="independent_authors",
    )


class Article(models.Model):
    """Represents a news article written by a journalist."""

    title = models.CharField(max_length=255)
    content = models.TextField()

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name="articles",
        null=True,
        blank=True,
    )

    journalist = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="articles",
        null=True,
        blank=True,
    )

    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return the article title as its string representation."""
        return self.title
