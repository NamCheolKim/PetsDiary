from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "This command created superuser"

    def handle(self, *args, **options):

        admin = User.objects.get_or_none(username="admin")

        if not admin:
            User.objects.create_superuser(
                "admin@petsdiary.com", "petsdiary0@gmail.com", "noel3907"
            )
            self.stdout.write(self.style.SUCCESS(f"SuperUser create"))
        else:
            self.stdout.write(self.style.SUCCESS(f"SuperUser Exist"))
