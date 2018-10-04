from instagram.models import User
from instagram.models import Post
from instagram.models import PostedBy

def menu():
    print('presione 1 para crear un usuario')
    print('presione 2 para ver todos los usuarios')
    print('presione 3 para acceder a la app')
    print('presione 4 para salir')

def loggedinmenu():
    print('presione 1 para crear un post')
    print('presione 2 para likear un post')
    print('presione 3 para borrar un post')
    print('presione 4 para salir')


def create_user():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input("Ingrese su email: ")
    username = input("Ingrese su username: ")
    mi_usuario = User(nombre=nombre,apellido=apellido,email=email,username=username)
    mi_usuario.save()
    
def show_all_users():
    for user in User.objects.all():
        print("id: {0}, nombre: {1}, apellido: {2}, email: {3}, username: {4}".format(user.id,user.nombre,user.apellido,user.email,user.username))

def ingresar_app():
    username = input("Ingrese su username: ")
    email = input("Ingrese su email: ")
    try:
        my_user = User.objects.get(username=username,email=email)
        print('log in exitoso\n')
        
    except:
        print('no existe tal usuario y email')
        my_user = False
    return my_user

def make_post(login):
    titulo = input('ingrese el titulo del post: ')
    post_text = input('ingrese el contenido del post: ')
    mi_post = Post(titulo=titulo,post_text=post_text)
    mi_post.save()
    user_id_and_post_id = PostedBy(user_id=login,post_id=mi_post)
    user_id_and_post_id.save()
    
