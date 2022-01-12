FROM python:3.8

COPY requirements.txt entrypoint.py ./

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "./entrypoint.py"]
