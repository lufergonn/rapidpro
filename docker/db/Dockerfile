FROM postgres:13


RUN apt update -y && apt upgrade -y && \
    apt -y install gnupg2 wget

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list


RUN apt -y install postgis postgresql-13-postgis-3

# RUN psql -d $POSTGRES_DB -U $POSTGRES_USER -c "CREATE EXTENSION postgis;"
# RUN psql -d $POSTGRES_DB -U $POSTGRES_USER -c "CREATE EXTENSION postgis_topology;"
# RUN psql -d $POSTGRES_DB -U $POSTGRES_USER -c "CREATE EXTENSION hstore;"
# RUN psql -d $POSTGRES_DB -U $POSTGRES_USER -c 'CREATE EXTENSION "uuid-ossp";'
