FROM python:3.9

RUN apt-get update
RUN apt-get -y install cron

RUN apt install -y git

RUN git clone https://github.com/rohanSSiddeshwara/time_series.git

WORKDIR /time_series

RUN pip install nsetools

CMD ["python", "daily_data.py"]

# Add the cron job
RUN crontab -l | { cat; echo "* * * * * python ./time_series/daily_data.py"; } | crontab -

# Run the command on container startup
CMD cron