FROM python:3.12.1
WORKDIR /app
COPY requirements.txt req.txt
RUN pip3 install -r req.txt
COPY . .
EXPOSE 5000
CMD ["python3", "app.py"]