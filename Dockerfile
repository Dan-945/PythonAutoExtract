FROM python:3.12
# TODO: create mount points for watch and copy to folders and log folder
# TODO: test with service that only writes to log once a minute
# TODO: install on dockermachine

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app
ADD ./dockertest.py .
VOLUME ["./Watch", "/Watch"]
VOLUME ["./ExtractFolder", "/ExtractFolder"]
VOLUME ["./LogFolder", "/LogFolder"]
#COPY ./Watch /Watch
#COPY ./ExtractFolder /ExtractFolder
#COPY ./LogFolder /LogFolder
#RUN pip install -r requirements.txt

CMD ["python", "./dockertest.py"]





######################### auto exctract
#COPY requirements.txt /opt/app/requirements.txt
#WORKDIR /opt/app
#RUN pip install -r requirements.txt
#COPY . /opt/app
#ADD ./autoExtract.py .
#VOLUME ["./Watch", "/Watch"]
#VOLUME ["./ExtractFolder", "/ExtractFolder"]
#VOLUME ["./LogFolder", "/LogFolder"]
##COPY ./Watch /Watch
##COPY ./ExtractFolder /ExtractFolder
##COPY ./LogFolder /LogFolder
##RUN pip install -r requirements.txt
#
#CMD ["python", "./autoExtract.py"]