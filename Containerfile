# podman build -f Containerfile -t winget

# mkdir -p /tmp/winget/media /tmp/winget/db
# podman run -p 8000:8000 -v /tmp/winget/media:/srv/media:rw -v /tmp/winget/db:/srv/db:rw -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_EMAIL=vagt56@jyskebank.dk -e DJANGO_SUPERUSER_PASSWORD=astrongpassword -it winget


FROM registry.access.redhat.com/ubi9/python-39:1-186

USER 0
RUN chown default /srv
USER default

ENV DEBUG=False
ENV HOST_NAME=*
# Keep the DB file in a separate directory, which can be shared as a volume.
ENV SQLITE_DB_FILE=/srv/db/db.sqlite3

WORKDIR /srv

COPY --chown=default:root . .

RUN mkdir `dirname $SQLITE_DB_FILE`


RUN pip install --no-cache-dir -Ur requirements/base-full.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8000

RUN chmod +x /srv/run/docker/start.sh

CMD ["/srv/run/docker/start.sh"]
