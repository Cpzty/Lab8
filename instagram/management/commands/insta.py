from django.core.management.base import BaseCommand
from instagram.models import User
from instagram.models import Post
from instagram.models import PostedBy
from instagram.models import LikedBy

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
                while(login != False):
                    loggedinmenu()
                    logged_in_opcion = input('ingrese una opcion: ')
                    if(logged_in_opcion =='1'):
                        make_post(login)
                    if(logged_in_opcion =='2'):
                        for post in Post.objects.all():
                            print('pk={0} - titulo: {1} -contenido: {2}'.format(post.id,post.titulo,post.post_text))
                        post_id = input('¿a que post le desea dar like?: ')
                        post_designado = Post.objects.get(pk =str(post_id))
                        likeado= LikedBy(user_id=login,post_id=post_designado)
                        likeado.save()
                    if(logged_in_opcion =='3'):
                        for post in Post.objects.filter(pk=login.id):
                            print('pk={0} - titulo: {1} -contenido: {2}'.format(post.id,post.titulo,post.post_text))
                        post_id2 = input('¿Que post desea borrar?: ')
                        post_designado = Post.objects.get(pk =str(post_id2))
                        post_designado.delete()
                    if(logged_in_opcion =='4'):
                        login=False
                        
                        
                    
            
