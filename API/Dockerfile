FROM python:3.7

ENV FLASK_APP=main.py

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 10000

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "10000"]
