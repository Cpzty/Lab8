from django.core.management.base import BaseCommand

from instagram.models import User
 

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        username = input("Username: ")
        contrasena = input("Contrasena: ")
        try:
            my_user = User.objects.get(username=username,contrasena=contrasena)
            print('log in exitoso')
        except:
            print('no existe tal usuario y contrasena')
        
    
