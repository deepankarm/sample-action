FROM python:3.8

COPY requirements.txt entrypoint.py ./

RUN ls -l && pip install -r ./requirements.txt

ENTRYPOINT ["python", "./entrypoint.py"]
