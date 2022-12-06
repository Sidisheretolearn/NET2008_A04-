FROM python:3.10

ADD NET2008_A04.py .

RUN pip install

CMD ["python", "./NET2008_A04"]






