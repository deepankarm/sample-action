FROM python:3.8

COPY entrypoint.py /usr/bin/entrypoint.py

RUN pip install requests

ENTRYPOINT ["python", "/usr/bin/entrypoint.py"]
