FROM python:3.8-alpine
ADD . / 
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* 
CMD ["python", "main.py"]