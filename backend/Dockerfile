FROM python:3.6.15-slim
WORKDIR /server
COPY requirements.txt /server/requirements.txt
COPY server.py /server/server.py
RUN pip install -r requirements.txt
CMD ["python","server.py"]