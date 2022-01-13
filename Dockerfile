FROM python:3.8

COPY entrypoint.py /usr/bin/entrypoint.py

RUN pwd && ls -l && pip install requests

ENTRYPOINT ["python", "/usr/bin/entrypoint.py"]
