import os

from utilities.config import UPDATE_WINDOWS_ENV

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')


def get_update_key():
    return os.getenv(UPDATE_WINDOWS_ENV)


def set_update_key(value):
    os.environ[UPDATE_WINDOWS_ENV] = value


def should_update():
    value = get_update_key()
    if value is None:
        # No updates have been done, do it, then set env value to 1
        set_update_key(1)
        return True
    elif value == 1:
        # still update, but set it to 2
        set_update_key(2)
        return True
    elif value == 2:
        # remove the key
        return False
    pass
