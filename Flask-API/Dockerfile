FROM python:3.7-slim
WORKDIR /home/app

ADD * /home/app

RUN apt-get update -y &&\ 
addgroup --system app &&\
adduser --system --ingroup app --no-create-home app &&\
pip install --upgrade pip &&\
pip install -r requirements.txt &&\
apt-get install -y sqlite &&\
python list_instances.py &&\
chmod +x data-import.sh &&\
./data-import.sh &&\
rm -rf Dockerfile


EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["FlaskApp.py"]