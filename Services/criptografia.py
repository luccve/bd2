from cmath import log
from email.policy import default
from hashlib import md5
from logging import exception


class Criptografia ():

    def dict_senhas(self):
        self.users = {"admin": ["admin", "202cb962ac59075b964b07152d234b70"], "user": [
            "user", "202cb962ac59075b964b07152d234b70"]}

    def login(self, nome, senha):
        if nome == "" or senha == "":
            return False

        else:
            self.senha = md5(senha.encode('utf8')).hexdigest()
            for s in self.users.values():
                if s[1] == self.senha and self.users.get(nome):
                    return True
                else:
                    return False

    def tipo_login(self, nome):
        if nome == "admin":
            return True
        else:
            return False
