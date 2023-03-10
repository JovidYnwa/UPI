FROM python:3.11.0

SHELL ["/bin/bash", "-c"]

#Eviromental variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#updating pip
RUN pip install --upgrade pip

#
RUN apt-get update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

#Creating new user upiuser in this case
RUN useradd -rms /bin/bash upiuser && chmod 777 /opt /run 

#Creating working directory
WORKDIR /upi

#Creating twho more directories for static and media files
RUN mkdir /upi/static && mkdir /upi/media && chown -R upiuser /upi && chmod 775 /upi

#
COPY --chown=upiuser:upi . .

RUN pip3 install -r requirements.txt

USER upiuser


CMD ["gunicorn", "-b", "0.0.0.0:8000", "upi.wsgi"]
