FROM python:3.8

RUN python3 -m venv ccblog-env

COPY manage.py .

COPY get-pip.py .

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py" ]

