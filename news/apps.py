from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_roles_and_permissions(sender, **kwargs):
    # Keep these imports inside the function so Django is fully loaded first.
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from .models import Article

    reader_group, _ = Group.objects.get_or_create(name="Reader")
    editor_group, _ = Group.objects.get_or_create(name="Editor")
    journalist_group, _ = Group.objects.get_or_create(name="Journalist")

    article_ct = ContentType.objects.get_for_model(Article)

    view_article = Permission.objects.get(
        codename="view_article",
        content_type=article_ct,
    )
    add_article = Permission.objects.get(
        codename="add_article",
        content_type=article_ct,
    )
    change_article = Permission.objects.get(
        codename="change_article",
        content_type=article_ct,
    )
    delete_article = Permission.objects.get(
        codename="delete_article",
        content_type=article_ct,
    )

    # Reader: can only read articles
    reader_group.permissions.set([view_article])

    # Editor: can review and manage content, but not create it
    editor_group.permissions.set([
        view_article,
        change_article,
        delete_article,
    ])

    # Journalist: full control over their own content
    journalist_group.permissions.set([
        view_article,
        add_article,
        change_article,
        delete_article,
    ])


class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "news"

    def ready(self):
        # Run after migrations to make sure groups & permissions always exist
        post_migrate.connect(create_roles_and_permissions, sender=self)

        # Load signals (kept here so Django registers them on startup)
        from . import signals  # noqa: F401
        from . import signals_article  # noqa: F401
