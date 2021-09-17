from core.models import User


def user_jon():
    ze = User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )
    return ze

def usuarios_cientistas():
    User.objects.create_user(username='newton')
    User.objects.create_user(username='einstein')
    User.objects.create_user(username='descartes')
