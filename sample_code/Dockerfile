# irisowo/crawler:v1
FROM python:3.6.15-slim
WORKDIR /sample_crawler
COPY . .
RUN pip install -r ./requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
CMD ["python","crawler_sample_and_trend.py"]