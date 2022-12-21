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


EXPOSE 8000

CMD poetry run ./manage.py runserver 0.0.0.0:8000
