FROM python:3.12.7

# LABEL admin="misha" github="medin-misha"
# EXPOSE 8000:8000

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY ./ app/

WORKDIR app/
CMD ["gunicorn", "crm.wsgi", "--workers", "33", "--bind", "0.0.0.0:8000"]

