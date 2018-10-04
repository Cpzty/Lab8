from django.core.management.base import BaseCommand

from instagram.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Cantidad antes:", User.objects.all().count())
        username = input("Username: ")
        contrasena = input("Contrasena: ")
        mi_usuario = User(username=username, contrasena=contrasena)
        mi_usuario.save()
        print("Cantidad despues:", User.objects.all().count())
