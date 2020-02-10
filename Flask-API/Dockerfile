FROM python:3.7-slim
WORKDIR /home/app

RUN mkdir /home/app/.oci
COPY requirements.txt .
COPY config /home/app/.oci/
COPY oci_api_key.pem /home/app/.oci/
COPY data-import.sh .
COPY object-download.py .
COPY FlaskApp.py .


RUN apt-get update -y &&\
apt-get install -y curl &&\
pip install --upgrade pip &&\
pip install -r requirements.txt &&\
curl -L -O https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh &&\
chmod 777 install.sh &&\
./install.sh --accept-all-defaults &&\
addgroup --system app &&\
adduser --system --ingroup app --no-create-home app &&\
apt-get install -y sqlite &&\
python object-download.py &&\
chmod 777 data-import.sh &&\
./data-import.sh


EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["FlaskApp.py"]