FROM python:3.6.15-slim
COPY googletrend.py /sample_crawler/googletrend.py
WORKDIR /sample_crawler
RUN pip install pandas
RUN pip install pytrends
CMD ["python","googletrend.py"]
# CMD ["python","crawler_sample.py"]