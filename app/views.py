import time
from jogoteca import db, app
from models import Jogo, Usuario
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from dao import JogoDao, UsuarioDao
from helpers import deleta_arquivo, recupera_imagem, encripta_senha, verifica_senha

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    listaJogos = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=listaJogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima_pagina=url_for('novo')))

    else:
        return render_template('criar.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo = jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    uploadPath = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{uploadPath}/capa{jogo.id}-{timestamp}.jpg')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    jogo = jogo_dao.busca_por_id(id)

    nome_imagem = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando app', jogo=jogo, capa_jogo=nome_imagem)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console, request.form['id'])
    arquivo = request.files['arquivo']
    uploadPath = app.config['UPLOAD_PATH']
    timestamp = time.time()

    deleta_arquivo(jogo.id)
    arquivo.save(f'{uploadPath}/capa{jogo.id}-{timestamp}.jpg')

    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    deleta_arquivo(id)

    jogo_dao.deletar(id)
    flash('Jogo removido com sucesso')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima_pagina = request.args.get('proxima_pagina')
    return render_template('login.html', proxima_pagina=proxima_pagina)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:

        usuario = usuario_dao.buscar_por_id(request.form['usuario'])

        if not usuario:
            flash('Usuario inexistente no sistema')
            return redirect('login')

        senhaDoUsuario = request.form['senha']
        senhaDoBanco = usuario.senha

        if verifica_senha(senhaDoUsuario, senhaDoBanco):
            session['usuario_logado'] = request.form['usuario']
            flash(request.form['usuario'] + ' logou com sucesso')
            proxima_pagina = request.form['proxima_pagina']
            return redirect(proxima_pagina)

        else:
            flash('Não logado. Senha incorreta')
            return redirect('login')
    else:
        return redirect(url_for('index'))


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')


@app.route('/criar_usuario', methods=['POST',])
def criar_usuario():
    nomeDeUsuarioDoFormulario = request.form['usuario']
    nomeCompletoDoFormulario = request.form['nomeCompleto']
    senha1DoFormulario = request.form['senha1']
    senha2DoFormulario = request.form['senha2']

    if senha1DoFormulario != senha2DoFormulario:
        flash('Senhas não coincidem')
        return redirect('cadastrar')

    if usuario_dao.buscar_por_id(nomeDeUsuarioDoFormulario):
        flash(f'Usuario {nomeDeUsuarioDoFormulario} já existe no sistema')
        return redirect('cadastrar')

    senhaEncriptada = encripta_senha(senha1DoFormulario)

    usuario = Usuario(nomeDeUsuarioDoFormulario, nomeCompletoDoFormulario, senhaEncriptada)
    usuario_dao.criarUsuario(usuario)

    flash(f'Usuario foi criado com sucesso')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado')
    return redirect('/')


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
