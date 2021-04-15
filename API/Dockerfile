FROM python:3.7

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 10000

COPY . .

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "10000"]
