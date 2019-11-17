import os


class config(object):
    SECRET_KY = os.environ.get('SECRET_KEy') or "secret_string"
