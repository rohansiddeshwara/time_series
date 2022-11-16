FROM python:3.9

RUN apt-get update


RUN apt install -y git

RUN git clone https://github.com/rohanSSiddeshwara/time_series.git

WORKDIR /time_series

RUN pip install nsetools fastapi uvicorn pandas numpy requests

RUN uvicorn daily_data:app --reload --host 0.0.0.0 --port 8000

CMD [ "python","script.py" ]