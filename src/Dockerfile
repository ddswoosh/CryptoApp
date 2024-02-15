FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

ADD gui.py .
ADD main.py .
ADD auth.py .

RUN pip install requests pyqt5

CMD ["python", "./gui.py"]
