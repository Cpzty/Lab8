from django.core.management.base import BaseCommand
from instagram.models import User
from instagram.utils import * 
    

    
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        opcion = 0
        while(opcion != '4'):
            menu()
            opcion = input('ingrese una opcion: ')
            if(opcion=='1'):
                create_user()
            elif(opcion=='2'):
                show_all_users()
            elif(opcion=='3'):
                login=ingresar_app()
                while(login == True):
                    loggedinmenu()
                    logged_in_opcion = input('ingrese una opcion: ')
                        
                    
            
