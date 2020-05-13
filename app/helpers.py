import os
from passlib.hash import sha256_crypt
from jogoteca import app


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo


def deleta_arquivo(id):
    arquivo = recupera_imagem(id)

    if not arquivo:
        pass

    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))


def encripta_senha(senha):
    return sha256_crypt.encrypt(senha)


def verifica_senha(senhaDoUsuario, senhaDoBanco):
    return sha256_crypt.verify(senhaDoUsuario, senhaDoBanco)
