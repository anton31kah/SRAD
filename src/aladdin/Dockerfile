FROM python:3.8

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

EXPOSE 8010

COPY ./aladdin.py /app/aladdin.py

WORKDIR /app
CMD ["uvicorn", "aladdin:app", "--host", "0.0.0.0", "--port", "8010"]