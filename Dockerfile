FROM python:3.12
#COPY requirements.txt /opt/app/requirements.txt
#WORKDIR /opt/app
#RUN pip install -r requirements.txt
#COPY . /opt/app
#ADD ./dockertest.py .
#VOLUME ["./Watch", "/Watch"]
#VOLUME ["./ExtractFolder", "/ExtractFolder"]
#VOLUME ["./LogFolder", "/LogFolder"]
##COPY ./Watch /Watch
##COPY ./ExtractFolder /ExtractFolder
##COPY ./LogFolder /LogFolder
##RUN pip install -r requirements.txt
#
#CMD ["python", "./dockertest.py"]


######################### auto exctract
# copy requirements file and install requirements
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt

# copies all files from cwd, overkill, should maybe just be the actual py script.
COPY . /opt/app
ADD ./autoExtract.py .
VOLUME ["./Watch", "/Watch"]
VOLUME ["./ExtractFolder", "/ExtractFolder"]
VOLUME ["./LogFolder", "/LogFolder"]
#COPY ./Watch /Watch
#COPY ./ExtractFolder /ExtractFolder
#COPY ./LogFolder /LogFolder
#RUN pip install -r requirements.txt

CMD ["python", "./autoExtract.py"]