from instagram.models import User

def menu():
    print('presione 1 para crear un usuario')
    print('presione 2 para ver todos los usuarios')
    print('presione 3 para acceder a la app')
    print('presione 4 para salir')

def loggedinmenu():
    print('presione 1 para crear un post')


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
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    try:
        my_user = User.objects.get(nombre=nombre,email=email)
        print('log in exitoso\n')
        login = True
    except:
        print('no existe tal usuario y email')
        login = False
    return login
