# YouTube Audio Downloader

Um aplicativo web simples para baixar áudios de vídeos do YouTube em formato MP3.

## Funcionalidades

- Download de áudio de vídeos do YouTube
- Conversão automática para MP3
- Interface simples e intuitiva
- Qualidade de áudio otimizada (192kbps)

## Requisitos

- Python 3.8 ou superior
- FFmpeg instalado no sistema
- Dependências Python listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/youtube_downloader_web.git
cd youtube_downloader_web
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Instale o FFmpeg:
- Windows: Baixe do [site oficial](https://ffmpeg.org/download.html) e adicione ao PATH
- Linux: `sudo apt-get install ffmpeg`
- Mac: `brew install ffmpeg`

## Configuração

1. Crie um arquivo `config.py` na raiz do projeto:
```python
import os

class Config:
    SECRET_KEY = 'sua-chave-secreta-aqui'
    DOWNLOADS_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')
```

2. Ajuste a chave secreta para um valor seguro.

## Uso

1. Inicie o servidor:
```bash
python app.py
```

2. Abra seu navegador e acesse `http://localhost:5000`

3. Cole a URL do vídeo do YouTube e clique em "Baixar Áudio"

## Estrutura do Projeto

```
youtube_downloader_web/
├── app.py              # Aplicação principal
├── config.py           # Configurações
├── extensions.py       # Extensões Flask
├── requirements.txt    # Dependências
├── static/            # Arquivos estáticos
│   └── style.css      # Estilos CSS
└── templates/         # Templates HTML
    ├── base.html      # Template base
    └── index.html     # Página inicial
```

## Tecnologias Utilizadas

- Flask: Framework web
- yt-dlp: Biblioteca para download de vídeos do YouTube
- FFmpeg: Conversão de áudio
- Flask-Moment: Formatação de datas

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Aviso Legal

Este projeto é apenas para fins educacionais. Respeite os direitos autorais e as políticas do YouTube ao usar este aplicativo. 