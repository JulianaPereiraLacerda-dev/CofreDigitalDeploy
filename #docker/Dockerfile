FROM python:3.11-slim  
# Criando usuário não-root (segurança) 
RUN useradd --create-home --shell /bin/bash appuser
 
# Definindo diretório de trabalho 
WORKDIR /app 
 
COPY app/requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY app/ .
USER appuser 
EXPOSE ${PORT:-5000} 
