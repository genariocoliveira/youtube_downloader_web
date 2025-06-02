import os
import uuid
from datetime import datetime
from flask import Flask, request, send_file, render_template, redirect, url_for, flash
import yt_dlp
import logging
from pathlib import Path

# Configuração de Logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Importar configurações do arquivo config.py
from config import Config
app.config.from_object(Config)

# Inicializar extensões
from extensions import moment
moment.init_app(app)

# Configurações para o yt-dlp (áudio)
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(Config.DOWNLOADS_DIR, '%(id)s.%(ext)s'),
    'noplaylist': True,
}

# Garante que o diretório de downloads exista
os.makedirs(Config.DOWNLOADS_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_audio():
    youtube_url = request.form['youtube_url']
    
    if not youtube_url:
        flash("Por favor, insira uma URL do YouTube.", "danger")
        return redirect(url_for('index'))

    if not ("youtube.com/watch" in youtube_url or "youtu.be/" in youtube_url):
        flash("URL do YouTube inválida.", "danger")
        return redirect(url_for('index'))

    return process_download(youtube_url)

def process_download(youtube_url):
    """
    Função para processar o download do áudio.
    """
    unique_filename = str(uuid.uuid4())
    temp_filepath = os.path.join(Config.DOWNLOADS_DIR, f"{unique_filename}.%(ext)s")
    
    current_ydl_opts = ydl_opts.copy()
    current_ydl_opts['outtmpl'] = temp_filepath

    try:
        with yt_dlp.YoutubeDL(current_ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            original_file_path_template = ydl.prepare_filename(info_dict)
            final_mp3_path = os.path.splitext(original_file_path_template)[0] + '.mp3'
            
            if not os.path.exists(final_mp3_path):
                logging.error(f"Erro: Arquivo MP3 não encontrado em {final_mp3_path} após download para {youtube_url}")
                raise FileNotFoundError("Arquivo MP3 não encontrado após o processamento.")
            
            download_name = f"{info_dict.get('title', 'audio')}.mp3"
            logging.info(f"Download concluído para {youtube_url}. Enviando arquivo: {download_name}")
            return send_file(final_mp3_path, as_attachment=True, download_name=download_name)

    except Exception as e:
        logging.error(f"Erro no download de {youtube_url}: {e}", exc_info=True)
        flash(f"Ocorreu um erro ao baixar o áudio: {e}", "danger")
        return redirect(url_for('index'))
    finally:
        # Tenta limpar o arquivo temporário, se existir
        if 'final_mp3_path' in locals() and os.path.exists(final_mp3_path):
            try:
                os.remove(final_mp3_path)
                logging.info(f"Arquivo temporário removido: {final_mp3_path}")
            except Exception as e:
                logging.error(f"Erro ao remover arquivo temporário {final_mp3_path}: {e}")

@app.route('/give-me-a-coffee')
def give_me_a_coffee():
    return redirect("https://www.buymeacoffee.com/SEU_USUARIO", code=302)

# Configuração para produção
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)