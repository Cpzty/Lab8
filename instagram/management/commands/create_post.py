from django.core.management.base import BaseCommand

from instagram.models import User
from instagram.models import Post

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        post = input("Ingrese su post: ")
