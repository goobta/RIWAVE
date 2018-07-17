FROM python:3

RUN apt-get update && \
		apt-get upgrade && \
		apt-get install -y python3-pyqt5 && \
		apt-get clean

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
CMD python __main_RI_Election__.py
