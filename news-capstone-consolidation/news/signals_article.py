import sys

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article


def _is_running_tests() -> bool:
    # Django test runner always includes "test" in sys.argv
    return "test" in sys.argv


@receiver(post_save, sender=Article)
def notify_on_article_approval(sender, instance: Article, created, **kwargs):
    # Skip notifications during automated tests
    if _is_running_tests():
        return

    # Only act when an article is approved
    if not instance.approved:
        return

    recipients = set()

    # Notify readers subscribed to the publisher
    if instance.publisher:
        for reader in instance.publisher.subscribers.all():
            if reader.email:
                recipients.add(reader.email)

    # Notify readers subscribed to the journalist
    if instance.journalist:
        for reader in instance.journalist.journalist_subscribers.all():
            if reader.email:
                recipients.add(reader.email)

    if not recipients:
        return

    send_mail(
        subject=f"New article published: {instance.title}",
        message=f"{instance.title}\n\n{instance.content}\n",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=list(recipients),
        fail_silently=False,
    )

    # X (Twitter) post placeholder
    print(f"[X POST] New article published: {instance.title}")
