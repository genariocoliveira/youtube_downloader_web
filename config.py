import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_muito_segura' # Mude isso em produção!
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOWNLOADS_DIR = 'downloads' # Diretório para armazenar arquivos temporários
    MAX_CONCURRENT_DOWNLOADS_ANONYMOUS = 1 # Limite para usuários não logados
    MAX_CONCURRENT_DOWNLOADS_LOGGED_IN = 5 # Limite para usuários logados