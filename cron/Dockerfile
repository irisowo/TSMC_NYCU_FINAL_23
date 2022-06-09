FROM python:3.7
RUN apt-get update && apt-get -y install cron vim
WORKDIR /sample_crawler

RUN pip3 install pandas
RUN pip3 install pytrends
RUN pip3 install pytest
RUN pip3 install pytest-cov

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
COPY . .

RUN echo $PYTHONPATH
EXPOSE 4000

# run crond as main process of container
CMD ["cron", "-f"]