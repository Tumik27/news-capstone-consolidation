from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User, Publisher, Article


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Role & Subscriptions", {
            "fields": (
                "role",
                "subscribed_publishers",
                "subscribed_journalists",
                "independent_articles",
            )
        }),
    )

    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "approved", "publisher", "journalist", "created_at")
    list_filter = ("approved", "publisher")
    search_fields = ("title", "content")
    actions = ["approve_articles"]

    @admin.action(description="Approve selected articles")
    def approve_articles(self, request, queryset):
        # Approve via save() so signals fire (email + X posting)
        for article in queryset:
            article.approved = True
            article.save()
