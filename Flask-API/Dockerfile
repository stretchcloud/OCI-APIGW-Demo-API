FROM python:3.7-slim
WORKDIR /home/app

ADD * /home/app/

RUN apt-get update -y &&\ 
addgroup --system app &&\
adduser --system --ingroup app --no-create-home app &&\
pip install --upgrade pip &&\
pip install -r requirements.txt &&\
apt-get install -y sqlite &&\
chmod +x data-import.sh &&\
./data-import.sh &&\
rm -rf Dockerfile list_instances.py


EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["FlaskApp.py"]