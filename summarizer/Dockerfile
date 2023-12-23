FROM python:3.9-slim

WORKDIR /learning_app
ADD . /learning_app

RUN pip install -r requirements.txt
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN python download.py

CMD ["python", "wsgi.py"]