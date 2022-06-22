from cmath import log
from email.policy import default
from hashlib import md5
from logging import exception


senha = '1234567890abcdefghijklmnopqrstuvwxyz'


def login(username: default='estevao', senha: default='123'):
    try:
        if (username_load(username) and pass_load(senha)):
            print ('Login successful')
        pass    
    except ValueError:
        print ('Login failed')


def username_load(username):
    # IMPLEMENTAR select dos campos usuarios
    usuarios = ['carlos', 'joao', 'estevao']
    for user in usuarios:
        if username==user:
            return True
    
def pass_load(senha):
    # IMPLEMENTAR select da senha
    password = ['928f7bcdcd08869cc44c1bf24e7abec6', '1e05f8bcc204e8855b465dc21ccf0931']
    
    senha = md5(senha.encode('utf8')).hexdigest()
    for k in password:
        if senha == k:
            return True
    
login('caio', senha)