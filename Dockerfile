FROM python:3.7
RUN pip install XlsxWriter
RUN pip install flask
RUN pip install flask-cors
RUN mkdir /uploads
RUN mkdir /exceloutput
WORKDIR /root
CMD export FLASK_APP=api.py && flask run --host=0.0.0.0