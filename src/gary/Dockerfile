FROM python:3.8

RUN apt install python3-lxml

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

EXPOSE 8020

COPY ./gary.py /app/gary.py

WORKDIR /app
CMD ["uvicorn", "gary:app", "--host", "0.0.0.0", "--port", "8020"]
