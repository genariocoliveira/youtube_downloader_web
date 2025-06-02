import os
from pathlib import Path

class Config:
    # Usa a chave secreta do ambiente ou gera uma nova
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave-secreta-padrao-para-desenvolvimento')
    
    # Diretório de downloads
    DOWNLOADS_DIR = os.environ.get('DOWNLOADS_DIR', os.path.join(Path.home(), 'Downloads'))
    
    # Configurações do servidor
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))
    
    # Configurações de debug
    DEBUG = os.environ.get('FLASK_ENV') == 'development'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONCURRENT_DOWNLOADS_ANONYMOUS = 1 # Limite para usuários não logados
    MAX_CONCURRENT_DOWNLOADS_LOGGED_IN = 5 # Limite para usuários logados