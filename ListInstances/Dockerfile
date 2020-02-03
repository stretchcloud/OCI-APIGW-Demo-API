FROM python:3.7-slim
WORKDIR /home/app

COPY requirements.txt .
RUN apt-get update -y && apt-get install -y curl && pip install --upgrade pip && pip install -r requirements.txt && bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh --accept-all-defaults)"

RUN addgroup --system app && adduser --system --ingroup app --no-create-home app && mkdir /home/app/.oci
COPY list_instances.py .
COPY shapes.py .
COPY object-upload.py .
COPY entrypoint.sh .
COPY config /home/app/.oci/
COPY oci_api_key.pem /home/app/.oci/
RUN chown -R app:app ./ && chmod 777 entrypoint.sh
USER app

CMD ["./entrypoint.sh"]