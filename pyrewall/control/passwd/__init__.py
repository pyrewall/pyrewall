from getpass import getpass
from pyrewall.core.dependency_injection import di
from pyrewall.core.models.user.update_user import UpdateUser
from pyrewall.core.services.user_service import UserService

def passwd(args):
    with di.di_scope():
        user_service = di.get_instance(UserService)
        username = args.username

        user = user_service.get_user_by_username(username)

        if user is None:
            print(f'User "{username}" does not exist.')
            return

        print(f'Change the password for "{username}"')
        new_password = getpass()
        confirm_password = getpass('Confirm: ')
        if new_password != confirm_password:
            print('Passwords do not match')
            return
        if len(new_password) == 0:
            print('Invalid new password')
            return
        
        user_service.update_user(user.id, UpdateUser(
            password=new_password
        ))

        print('Password updated.')