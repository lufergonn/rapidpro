FROM python:3.9

SHELL ["/bin/bash", "-c"]

COPY . /app
WORKDIR /app

RUN apt update -y && apt upgrade -y
RUN apt install -y --no-install-recommends libgdal-dev gettext ffmpeg

RUN pip install poetry

RUN curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt install nodejs

RUN poetry install --without dev

# RUN npm install
RUN npm install -g yarn
RUN npm install -g less
RUN yarn install

# RUN poetry run ./manage.py migrate

RUN poetry run ./manage.py collectstatic --noinput --verbosity=0
RUN poetry run ./manage.py compress --extension=".haml" --settings=temba.settings_compress

# Ro-indexer
RUN wget https://github.com/nyaruka/rp-indexer/releases/download/v7.3.7/rp-indexer_7.3.7_linux_amd64.tar.gz
RUN tar -xvf rp-indexer_7.3.7_linux_amd64.tar.gz rp-indexer
RUN  rm -rf rp-indexer_7.3.7_linux_amd64.tar.gz

# To Mailroom
RUN wget -P /tmp/ https://github.com/nyaruka/mailroom/releases/download/v7.5.36/mailroom_7.5.36_linux_amd64.tar.gz
RUN tar -xvf /tmp/mailroom_7.5.36_linux_amd64.tar.gz -C /tmp/
RUN /tmp/mailroom -db=postgres://temba:temba@db:5432/temba?sslmode=disable -redis=redis://redis:6379/10 -log-level=info > mailroom.log &



EXPOSE 8000

CMD poetry run ./manage.py runserver 0.0.0.0:8000
