from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


ROLE_TO_GROUP = {
    User.Role.READER: "Reader",
    User.Role.EDITOR: "Editor",
    User.Role.JOURNALIST: "Journalist",
}


@receiver(post_save, sender=User)
def sync_user_group_with_role(sender, instance: User, **kwargs):
    # This keeps roles + groups in sync automatically.
    group_name = ROLE_TO_GROUP.get(instance.role)
    if not group_name:
        return

    target_group = Group.objects.get(name=group_name)

    role_groups = Group.objects.filter(name__in=["Reader", "Editor", "Journalist"])
    instance.groups.remove(*role_groups)

    instance.groups.add(target_group)
